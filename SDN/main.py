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
        src_ip = socket.inet_ntoa(flow.src_addr)
        dest_ip = socket.inet_ntoa(flow.dst_addr)
        cos = flow.tos
        byte_count = flow.dPkts * flow.dOctets

        if flow.input_iface == 1:
            handle_sus_traffic(src_ip, dest_ip)

        if cos == 3:
            handle_cos_traffic(src_ip, cos)

        if dest_ip == "172.126.100.1":
            handle_sus_traffic(src_ip, dest_ip)

        if byte_count > THRESHOLD_BYTES:
            handle_heavy_traffic(src_ip, byte_count)