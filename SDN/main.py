from sdn_functions import *

flowchoice = input("Would you like to use sflow or netflow?\n S=sflow\n N=netflow\n B=both\n> ")
if flowchoice.lower() == "s":
    from sflowCollection import sflowCollection
    flowCollection = sflowCollection()
elif flowchoice.lower() == "n":
    from netflowCollection import netflowCollection
    flowCollection = netflowCollection()
elif flowchoice.lower() == "b":
    from sflowCollection import sflowCollection
    from netflowCollection import netflowCollection
    flowCollection = sflowCollection() + netflowCollection()
else:
    print("Invalid choice. Please enter 'S' for sflow or 'N' for netflow.")
    exit()

#loop som tar in netflow data och applicerar sedan nödvändiga åtgärder på switchen

while True:
    flows = flowCollection
    for flow in flows:
       
        source_ip = flow["IPV4_SRC_ADDR"]
        dest_ip = flow["IPV4_DST_ADDR"]
        typeofservice = flow["TOS"]
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

#if-satser som styr switchen baserat på innehållet i flows
        if input_interface == 1:
            handle_sus_traffic(source_ip, dest_ip)

        if typeofservice == 3 or typeofservice == 5:
            handle_tos_traffic(source_ip, typeofservice)

        if dest_ip == "172.126.100.1":
            handle_sus_traffic(source_ip, dest_ip)

        if byte_count > THRESHOLD_BYTES:
            handle_heavy_traffic(source_ip, byte_count)