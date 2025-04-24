import socket
import requests

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

# Checkar vilken port som används mest och vem som skickar mest data
analysis = {'ports' : {}, 'ips' : {}, 'total_packets_analyzed' : 0}
def analyze_netflow_data(analysis:dict, new_data:dict):
    k=0
    for key, ip in new_data.items():
        if ip['src_ip'] not in analysis['ips']:
            analysis['ips'][ip['src_ip']] = 1
        else:
            analysis['ips'][ip['src_ip']] += 1
        if ip['dst_port'] not in analysis['ports']:
            analysis['ports'][ip['dst_port']] = 1
        else:
            analysis['ports'][ip['dst_port']] += 1
        k += 1
    analysis["total_packets_analyzed"] += k
    for keys in analysis['ips']:
        if analysis['ips'][keys] > 0.8 * analysis["total_packets_analyzed"]:
            handle_heavy_traffic(keys, analysis['ips'][keys])
    return analysis

#cookie
def login_to_switch():
    global response
    login_url = f"{REST_BASE_URL}/login"
    response = session.post(login_url, json=AUTH, verify=False)
   


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

    r = requests.put(acl_url, json=acl_data, auth=AUTH, verify=False)
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