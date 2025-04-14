import socket
import struct
from datetime import timedelta
import netflow
import json
# DB
from sqlmodel import SQLModel, Field, create_engine, Session
from typing import Optional
from classes import data

# DB conf
DB_HOST = "192.168.1.63"
DB_PORT = 3306
DB_USER = "root"
DB_PWD = "221411"
DATABSE_NAME = "Netflow_Data"

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PWD}@{DB_HOST}:{DB_PORT}/{DATABSE_NAME}"

# Init db engine
engine = create_engine(DATABASE_URL)

def InsertDataToMariaDB(inpData: data):
    with Session(engine) as session:
        session.add(inpData)
        if session.commit():
            return 0
        else:
            return 1

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
        
        ip = int(tempEntry['IPV4_DST_ADDR'])
        ip_address_fixed = socket.inet_ntoa(struct.pack('!I', ip)) 
        tempEntry['IPV4_DST_ADDR'] = ip_address_fixed
        
        ip = int(tempEntry['NEXT_HOP'])
        ip_address_fixed = socket.inet_ntoa(struct.pack('!I', ip)) 
        tempEntry['NEXT_HOP'] = ip_address_fixed
        
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
            IPV4_SRC_ADDR=tempEntry["IPV4_SRC_ADDR"],
            IPV4_DST_ADDR=tempEntry["IPV4_DST_ADDR"],
            NEXT_HOP=tempEntry["NEXT_HOP"],
            INPUT=tempEntry["INPUT"],
            OUTPUT=tempEntry["OUTPUT"],
            IN_PACKETS=tempEntry["IN_PACKETS"],
            IN_OCTETS=tempEntry["IN_OCTETS"],
            FIRST_SWITCHED=tempEntry["FIRST_SWITCHED"],
            LAST_SWITCHED=tempEntry["LAST_SWITCHED"],
            SRC_PORT=tempEntry["SRC_PORT"],
            DST_PORT=tempEntry["DST_PORT"],
            TCP_FLAGS=tempEntry["TCP_FLAGS"],
            PROTO=tempEntry["PROTO"],
            TOS=tempEntry["TOS"],
            SRC_AS=tempEntry["SRC_AS"],
            DST_AS=tempEntry["DST_AS"],
            SRC_MASK=tempEntry["SRC_MASK"],
            DST_MASK=tempEntry["DST_MASK"],
            DATE=date.today()
            )
        
        # Send to DB
        InsertDataToMariaDB(tmpDbEntry)
        tmpDbEntry = data()


        
    return bigDict
