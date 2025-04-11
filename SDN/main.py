<<<<<<< HEAD
import socket
import requests
import netflow

# --- Configuration Constants ---
LISTEN_HOST = '0.0.0.0'
NETFLOW_PORT = 2055
THRESHOLD_BYTES = 1000000  # Threshold to trigger action (e.g., 1,000,000 bytes)

# Switch REST API Configurations
SWITCH_IP = '192.168.1.100'
REST_BASE_URL = f'http://{SWITCH_IP}/rest/v1'
AUTH = ("admin", "password")  # Replace with your admin credentials
VLAN_ID = 10  # Use the VLAN number carrying monitored traffic


# --- REST API Functions for Switch Control ---

def block_ip_on_switch(ip_to_block):
    """
    This function creates (or updates) an ACL rule on the Aruba switch to block traffic
    from the given IP address, and then applies that ACL to a VLAN.
    """
    acl_name = "BLOCK_HEAVY"
    acl_rule_id = 10  # Rule ID can be an arbitrary identifier

    print(f"[ACTION] Blocking IP {ip_to_block} on the switch.")

    # Step 1: Create or update ACL rule
    acl_url = f"{REST_BASE_URL}/acls/ip/{acl_name}/rules/{acl_rule_id}"
    acl_data = {
        "action": "deny",
        "src-ip-addr": ip_to_block,
        "protocol": "ip"
    }

    r = requests.put(acl_url, json=acl_data, auth=AUTH, verify=False)
    if r.status_code in [200, 201]:
        print(f"ACL rule applied successfully (HTTP {r.status_code}).")
    else:
        print(f"Failed to apply ACL rule (HTTP {r.status_code}). Response: {r.text}")

    # Step 2: Apply the ACL to the VLAN configuration
    vlan_url = f"{REST_BASE_URL}/vlans/{VLAN_ID}"
    vlan_data = {"acl_in_cfg": {"acl_name": acl_name}}

    r = requests.put(vlan_url, json=vlan_data, auth=AUTH, verify=False)
    if r.status_code in [200, 201]:
        print(f"ACL successfully applied to VLAN {VLAN_ID} (HTTP {r.status_code}).")
    else:
        print(f"Failed to apply ACL to VLAN (HTTP {r.status_code}). Response: {r.text}")


def apply_qos_to_ip(ip_to_limit):
    """
    Applies a QoS policy to the specified IP address. This is a sample function that
    assumes your switch has pre-configured QoS profiles (e.g. a rate-limiting profile).
    """
    qos_profile = "LIMITED_PROFILE"
    print(f"[ACTION] Applying QoS profile '{qos_profile}' to IP {ip_to_limit}.")

    qos_url = f"{REST_BASE_URL}/qos/policies/{qos_profile}/bindings"
    qos_data = {
        "ip": ip_to_limit,
        "action": "apply"
    }

    r = requests.put(qos_url, json=qos_data, auth=AUTH, verify=False)
    if r.status_code in [200, 201]:
        print(f"QoS policy applied successfully (HTTP {r.status_code}).")
    else:
        print(f"Failed to apply QoS policy (HTTP {r.status_code}). Response: {r.text}")


def handle_heavy_traffic(src_ip, byte_count):
    """
    Trigger actions based on heavy traffic flow from the given source IP.
    """
    print(f"[DETECTION] Heavy traffic detected from {src_ip} ({byte_count} bytes).")
    block_ip_on_switch(src_ip)
    apply_qos_to_ip(src_ip)


# --- NetFlow Receiver and Parser ---

def start_netflow_listener():
    """
    Listens on UDP port 2055 and parses incoming NetFlow v9 data.
    For flows exceeding the defined threshold, takes corresponding actions.
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((LISTEN_HOST, NETFLOW_PORT))
    print(f"NetFlow collector is listening on {LISTEN_HOST}:{NETFLOW_PORT}")

    decoder = netflow()
    while True:
        try:
            data, addr = sock.recvfrom(8192)  # 8 KB buffer size
        except Exception as e:
            print(f"Error receiving data: {e}")
            continue

        try:
            records = decoder.decode(data)
        except Exception as e:
            print(f"Error parsing NetFlow data: {e}")
            continue

        # Process each flow record
        for flow in records:
            # The specific attributes (e.g. src_addr, dst_addr, bytes) depend on the pyflow library.
            print(f"Flow: {flow.src_addr} -> {flow.dst_addr}, Bytes: {flow.bytes}")
            if flow.bytes >= THRESHOLD_BYTES:
                handle_heavy_traffic(flow.src_addr, flow.bytes)


if __name__ == '__main__':
    start_netflow_listener()
=======
1233
>>>>>>> 0aa039479d9ed3ec16aa1801915aa36397065a49
