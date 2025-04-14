import socket
import struct
from datetime import timedelta
import netflow
import json
# DB
from sqlmodel import SQLModel, Field, create_engine, Session
from typing import Optional
from classes import *

# DB conf
DB_HOST = "192.168.1.63"
DB_PORT = 3306
DB_USER = "root"
DB_PWD = "221411"
DATABSE_NAME = "Netflow_Data"

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PWD}@{DB_HOST}:{DB_PORT}/{DATABSE_NAME}"

# Init db engine
engine = create_engine(DATABASE_URL)

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
        
        ip = int(tempEntry['IPV4_SRC_ADDR'])
        ip_address_fixed = socket.inet_ntoa(struct.pack('!I', ip)) 
        tempEntry['IPV4_SRC_ADDR'] = ip_address_fixed
        
        first = int(tempEntry['FIRST_SWITCHED'])
        last = int(tempEntry['LAST_SWITCHED'])
        firstreadable = str(timedelta(milliseconds=first))
        lastreadable = str(timedelta(milliseconds=last)) 
        tempEntry['FIRST_SWITCHED'] = firstreadable
        tempEntry['LAST_SWITCHED'] = lastreadable
        
        bigDict[i] = tempEntry
        i += 1


        # Database thing
        tmpDbEntry = data(
            IPV4_SRC_ADDR=inEntry["IPV4_SRC_ADDR"],
            IPV4_DST_ADDR=inEntry["IPV4_DST_ADDR"],
            NEXT_HOP=inEntry["NEXT_HOP"],
            INPUT=inEntry["INPUT"],
            OUTPUT=inEntry["OUTPUT"],
            IN_PACKETS=inEntry["IN_PACKETS"],
            IN_OCTETS=inEntry["IN_OCTETS"],
            FIRST_SWITCHED=inEntry["FIRST_SWITCHED"],
            LAST_SWITCHED=inEntry["LAST_SWITCHED"],
            SRC_PORT=inEntry["SRC_PORT"],
            DST_PORT=inEntry["DST_PORT"],
            TCP_FLAGS=inEntry["TCP_FLAGS"],
            PROTO=inEntry["PROTO"],
            TOS=inEntry["TOS"],
            SRC_AS=inEntry["SRC_AS"],
            DST_AS=inEntry["DST_AS"],
            SRC_MASK=inEntry["SRC_MASK"],
            DST_MASK=inEntry["DST_MASK"],
            DATE=date.today()
            )


        
    return bigDict
