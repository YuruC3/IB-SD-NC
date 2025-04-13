import netflow, socket, json, time, os, influxdb_client, ipaddress
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from datetime import timedelta

# Netentry preconf
WHAT_THE_NETFLOW_PORT = 2055
WHAT_THE_NETFLOW_IP = "0.0.0.0"


# INFLUXDB config

token = "XXXXXX==" 
bucket = "NETFLOW-STAGING"
org = "staging"
url = "http://localhost:8086"
measurement = "testNetFlowPython"
LOCATION_TAG = "YUKIKAZE"
INFLX_SEPARATE_POINTS = 0.01

# Initialize InfluxDB client
inflxdb_client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

# Other preconf
bigDict = {}

while True:
    # Get netentry data ig?
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((WHAT_THE_NETFLOW_IP, WHAT_THE_NETFLOW_PORT))
    payload, client = sock.recvfrom(4096)  # experimental, tested with 1464 bytes
    p = netflow.parse_packet(payload)  # Test result: <ExportPacket v5 with 30 records>
    #print(p.entrys)  # Test result: 5
    
    
    for i, entry in enumerate(p.flows, 1):
        # prep dict
        #tmpEntry = str(entry)
        #tmpEntry = tmpEntry[22:-1]
        #tmpEntry2 = tmpEntry.replace("'", '"')
    
        #print(tmpEntry2)
        #print(entry
        #exit()
        #dictEntry = json.loads(tmpEntry2)
        #bigDict[i] = (dictEntry)
    
    
        # take data out from netentry 
        inEntry = entry.data
    
        # Convert IPs and time duration 
        # IPs
        inEntry["IPV4_SRC_ADDR"] = str(ipaddress.IPv4Address(inEntry["IPV4_SRC_ADDR"]))
        inEntry["IPV4_DST_ADDR"] = str(ipaddress.IPv4Address(inEntry["IPV4_DST_ADDR"]))
        
        # Convert time from ms to HH:MM:SS
        first = int(inEntry["FIRST_SWITCHED"])
        last = int(inEntry["LAST_SWITCHED"])
        
        inEntry["FIRST_SWITCHED_HR"] = str(timedelta(milliseconds=first))
        inEntry["LAST_SWITCHED_HR"] = str(timedelta(milliseconds=last))
    
    
        # Prep InfluxDB data
        inflxdb_Data_To_Send = (
            influxdb_client.Point(f"{measurement}-script")
            .tag("LOCATION", LOCATION_TAG)
            .field("dstAddr", inEntry["IPV4_DST_ADDR"])
            .field("srcAddr", inEntry["IPV4_SRC_ADDR"])
            .field("nextHop", inEntry["NEXT_HOP"])
            .field("inptInt", inEntry["INPUT"])
            .field("outptInt", inEntry["OUTPUT"])
            .field("inPackt", inEntry["IN_PACKETS"])
            .field("outPakt", inEntry["IN_OCTETS"])
            .field("frstSwtchd", inEntry["FIRST_SWITCHED"])
            .field("lstSwtchd", inEntry["LAST_SWITCHED"])
            .field("srcPort", inEntry["SRC_PORT"])
            .field("dstPort", inEntry["DST_PORT"])
            .field("tcpFlags", inEntry["TCP_FLAGS"])
            .field("proto", inEntry["PROTO"])
            .field("tos", inEntry["TOS"])
            .field("srcAS", inEntry["SRC_AS"])
            .field("dstAS", inEntry["DST_AS"])
            .field("srcMask", inEntry["SRC_MASK"])
            .field("dstMask", inEntry["DST_MASK"])
        )
        
        # idk
        write_api = inflxdb_client.write_api(write_options=SYNCHRONOUS)
    
        # Send data to InfluxDB
        write_api.write(bucket=bucket, org="staging", record=inflxdb_Data_To_Send)
        time.sleep(INFLX_SEPARATE_POINTS) # separate points by 1 second
    
        #i+=1
        #type(tmpEntry)
        #print(dictEntry)
        #print(tmpEntry.lstrip(20))
    
        print("----------------")
        bigDict[i] = (inEntry)

    # end while True

    print(f"{len(bigDict)} <--- This many entrys")


    # Clean up before another loop
    bigDict.clear()
    
    #print(bigDict)
