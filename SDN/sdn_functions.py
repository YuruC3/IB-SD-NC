import socket
import requests
import datetime
from Ansible.sendmail import sendmail

admins = ['']

LISTEN_HOST = '0.0.0.0'
NETFLOW_PORT = 2055
THRESHOLD_BYTES = 1000000

#Config på switchen så vi kan kommunicera
#Ändra om det behövs
SWITCH_IP = '192.168.1.1'
REST_BASE_URL = f'http://{SWITCH_IP}/rest/v1'
AUTH = {"username": "admin", "password": "123"}
VLAN_ID = 10

response = ""

session = requests.Session()


# Behöver bearbetas
# Kör playbook
def run_ansible_playbook(playbook):
    r = ansible_runner.run(
        host_pattern='all',
        playbook=f'/ansible/{playbook}',
        inventory='hosts.ini',
        extravars={
            'switch_ip': SWITCH_IP,
            'rest_base_url': REST_BASE_URL,
            'auth': AUTH
        }
    )
#Check if it succeeds or fails.
    if r.rc != 0:
        print(f"[ERROR] Playbook {playbook} failed to run.")
    else:
        print(f"[SUCCESS] Playbook {playbook} ran successfully.")

# Checkar vilken port som används mest och vem som skickar mest data
analysis = {'packets' : {}, 'unique_src_ips' : {}, 'unique_dst_ports' : {}, 'total_packets_analyzed' : 0}

def analyze_netflow_data(analysis:dict, new_data:dict):
    temp = {}
    current_time = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=2)))

    for key, ip in analysis['packets'].items():
        if current_time - datetime.datetime.fromisoformat(ip['timestamp']) >= datetime.timedelta(hours=2):
            temp[key] = ip
    for ip in temp:
        analysis['unique_src_ips'][temp[ip]['src_ip']] -=1
        if analysis['unique_src_ips'][temp[ip]['src_ip']] <= 0:
            analysis['unique_src_ips'].pop(temp[ip]['src_ip'])
        analysis['unique_dst_ports'][temp[ip]['dst_port']] -=1
        if analysis['unique_dst_ports'][temp[ip]['dst_port']] <= 0:
            analysis['unique_dst_ports'].pop(temp[ip]['dst_port'])
        analysis['packets'].pop(ip)
        print ("removed: ", ip)
    temp.clear()
    for key, ip in new_data.items():
        analysis["total_packets_analyzed"] += 1
        analysis['packets'][analysis['total_packets_analyzed']] = ip
        print ("added: ", ip, "to analysis")
        if ip['src_ip'] not in analysis['unique_src_ips']:
            analysis['unique_src_ips'][ip['src_ip']] = 1
        else:
            analysis['unique_src_ips'][ip['src_ip']] += 1
        if ip['dst_port'] not in analysis['unique_dst_ports']:
            analysis['unique_dst_ports'][ip['dst_port']] = 1
        else:
            analysis['unique_dst_ports'][ip['dst_port']] += 1
    for keys in analysis['unique_src_ips']:
        if analysis['unique_src_ips'][keys] >= 5:
            handle_heavy_traffic(keys, analysis['unique_src_ips'][keys])
    return analysis

#cookie
def login_to_switch():
    global response
    login_url = f"{REST_BASE_URL}/login"
    response = session.post(login_url, json=AUTH, verify=False, timeout=5)
   


#QoS och IDS funktioner
#bara exempel, lägg till mer
def block_ip_on_switch(ip_to_block):

#ACL
    acl_name = "Block_1"
    acl_rule_id = 1

    acl_url = f"{REST_BASE_URL}/acls/ip/{acl_name}/rules/{acl_rule_id}"
    acl_data = {
        "action": "deny",
        "src-ip-addr": ip_to_block,
        "protocol": "ip"
    }

    r = requests.put(acl_url, json=acl_data, auth=AUTH, verify=False, timeout=5)
    if r.status_code in [200, 201]:
        print(f"Success")
    else:
        print(f"Failed to apply ACL rule (HTTP {r.status_code}). Response: {r.text}")


#Applying ACL to Vlan
    vlan_url = f"{REST_BASE_URL}/vlans/{VLAN_ID}"
    vlan_data = {"acl_in_cfg": {"acl_name": acl_name}}

    r = requests.put(vlan_url, json=vlan_data, auth=AUTH, verify=False)
    if r.status_code in [200, 201]:
        print(f"ACL successfully applied to VLAN {VLAN_ID} (HTTP {r.status_code}).")
    else:
        print(f"Failed to apply ACL to VLAN (HTTP {r.status_code}). Response: {r.text}")


#Apply QoS profile to IP
#Apply Qos policy
def apply_qos_to_ip(limit_ip):
    qos_profile = "Profile"
    print(f"[ACTION] Applying QoS profile '{qos_profile}' to IP {limit_ip}.")

    qos_url = f"{REST_BASE_URL}/qos/policies/{qos_profile}/bindings"
    qos_data = {
        "ip": limit_ip,
        "action": "apply"
    }

    r = requests.put(qos_url, json=qos_data, auth=AUTH, verify=False)
    if r.status_code in [200, 201]:
        print(f"QoS policy applied successfully (HTTP {r.status_code}).")
    else:
        print(f"Failed to apply QoS policy (HTTP {r.status_code}). Response: {r.text}")


def handle_heavy_traffic(source_ip, byte_count):
    print(f"[DETECTION] Heavy traffic detected from {source_ip} ({byte_count} bytes).")
    block_ip_on_switch(source_ip)
    apply_qos_to_ip(source_ip)


#kan användas för att blockera en ip som försöker att kommunicera med en annan specifik address
'''def handle_sus_traffic(source_ip, dest_ip):
'''    
def handle_sus_traffic(analyze_netflow_data):
    
    allowed_threshold = analyze_netflow_data["total_packets_analyzed"] * 0.5
    for ip, count in analyze_netflow_data.items():
        if count > allowed_threshold:
            block_ip_on_switch(ip)
            apply_qos_to_ip(ip)

#kan användas för att blockera en viss typ av service som inte är tillåten på nätverket (t.ex video)
def handle_tos_traffic(source_ip, classofservice):
    if classofservice == 3:     
        block_ip_on_switch(source_ip)
    elif classofservice == 5:  
        apply_qos_to_ip(source_ip)

#   ⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣤⣤⣤⣤⣤⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀ 
#⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀ 
#⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀  ⠈⢻⣿⣿⡄⠀⠀⠀⠀ 
#⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿    ⢿⣿⣿⣿⣄⠀⠀⠀ 
#⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀     ⠈⠙⢿⣷⡄⠀ 
#⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀ 
#⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀ 
#⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀ 
#⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀ 
#⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⠀ 
#⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀ 
#⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀ 
#⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀ 
#⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀ 
#⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⠀⢠⣿⣿⠀⠀⠀ 
#⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀ 
#⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀ 
#⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀ 
#⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀