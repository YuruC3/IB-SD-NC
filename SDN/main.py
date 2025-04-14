from netflowscript import *
from sdn_functions import *

#placeholder för netflowdelen
def netflow_data():
    print("...")


#loop som tar in netflow data och applicerar sedan nödvändiga åtgärder på switchen
#lägg till mer men inga konflikter
while True:
    netflow_data()
    flows = netflow_data()
    for flow in flows:
        #översätter från bytes till IP
        #src_ip = socket.inet_ntoa(flow.src_addr)
        #dest_ip = socket.inet_ntoa(flow.dst_addr)
        #tos = typeofservice

        src_ip = flow["IPV4_SRC_ADDR"]
        dest_ip = flow["IPV4_DST_ADDR"]
        classofservice = ["TOS"]
        byte_count = flow["IN_PACKETS"] * flow["IN_OCTETS"]
        first_switched = flow["FIRST_SWITCHED"]
        last_switched = flow["LAST_SWITCHED"]
        source_mask = flow["SRC_MASK"]
        dest_mask = flow["DST_MASK"]
        next_hop = flow["NEXT_HOP"]
        source_port = flow["SRC_PORT"]
        dest_port = flow["DST_PORT"]
        protocol = flow["PROTO"]
        input_interface = flow["INPUT"]
        output_interface = flow["OUTPUT"]


        if flow.input_iface == 1:
            handle_sus_traffic(src_ip, dest_ip)

        if classofservice == 3:
            handle_cos_traffic(src_ip, classofservice)

        if dest_ip == "172.126.100.1":
            handle_sus_traffic(src_ip, dest_ip)

        if byte_count > THRESHOLD_BYTES:
            handle_heavy_traffic(src_ip, byte_count)