import netflow
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0", 2055))

payload, client = sock.recvfrom(4096)  # experimental, tested with 1464 bytes
p = netflow.parse_packet(payload)  # Test result: <ExportPacket v5 with 30 records>

print(p.header.version)  # Test result: 5


# Duplicate IP flow
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