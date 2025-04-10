import netflow
import socket
from sqlmodel import Field, Session, create_engine, select
from classes import *


# Example på socket listener START
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0", 2055))

payload, client = sock.recvfrom(4096)  # experimental, tested with 1464 bytes
p = netflow.parse_packet(payload)  # Test result: <ExportPacket v5 with 30 records>

print(p.header.version)  # Test result: 5
# Example på socket listener END


# Duplicate IP flow START
pkt = IP(len=16384, src='192.168.240.243', dst=ip,
        id=RandShort(), ttl=64)/TCP(sport=5000,
        dport=5000, flags="S", window=200,
        options=[('MSS', 1460), ('WScale', 2)])/CustomLayer(type=1, update=2)/"SENT"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:    
    s.connect((ip, 5000))
except socket.error:
    print("User not connected")

spkt = str(pkt)
s.send(spkt)
# Duplicate IP flow END


# DATABASe

# Prepare what to send
toSend = NetFlowTable(srcIPAddr=X1, destIPAddr=X2, srcPort=X3, \
                      destPort=X4, layerThreeProto=X5, \
                      classOfService=X6, inpInterface=X7)
                      
# Add at the beggining to setup db connection                      
engine = create_engine("sqlitmariadb+mariadbconnector://USER:PWD!@127.0.0.1:3306/DB_NAME")
SQLModel.metadata.create_all(engine)


# Send to DB
with Session(engine) as session:
    session.add(toSend)
    session.commit()                      