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
                      
# Add at the beggining to setup db connection                      
# DB conf
DB_HOST = "192.168.1.63"
DB_PORT = 3306
DB_USER = "root"
DB_PWD = "221411"
DATABSE_NAME = "Netflow_Data"

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PWD}@{DB_HOST}:{DB_PORT}/{DATABSE_NAME}"

# Init db engine
engine = create_engine(DATABASE_URL)

# read bellow
def InsertDataToMariaDB(inpData: data):
    with Session(engine) as session:
        session.add(inpData)
        if session.commit():
            return 0
        else:
            return 1
        



# Send to DB
InsertDataToMariaDB(tmpDbEntry)

# Clear tmpDbEntry
tmpDbEntry = data()