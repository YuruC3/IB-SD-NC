import socket
import struct
from datetime import timedelta
import netflow
import json

def netflowColleciton():
    i=1
    bigDict = {}
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("0.0.0.0", 2055))
    payload, client = sock.recvfrom(4096)
    p = netflow.parse_packet(payload)
    for entry in p.flows:
        tempEntry = str(entry)
        tempEntry = tempEntry[22:-1]
        tempEntry = tempEntry.replace("'", '"')
        tempEntry = json.loads(tempEntry)
        
        ip = int(tempEntry['srcaddr'])
        ip_address_fixed = socket.inet_ntoa(struct.pack('!I', ip))  
        
        bigDict[i] = tempEntry
        i += 1
        
    return bigDict
