import subprocess, socket
from datetime import datetime, timezone
from sqlmodel import SQLModel, Field, create_engine, Session
from classess import data

# DB conf
DB_HOST = "192.168.1.63"
DB_PORT = 3306
DB_USER = "root"
DB_PWD = "221411"
DB_NAME = "Sflow_Data"
DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PWD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)

# header (hex) parser
def extract_ips_from_header_bytes_and_replace_with_something_more_humanReadable_plz_thanks(header_str):
    try:
        uber_unreadable_hex_thing = header_str.strip().split("-")
        header_Howmany_bytes = bytes([int(x, 16) for x in uber_unreadable_hex_thing])

        # If shorter than 34 bytes return empty
        if len(header_Howmany_bytes) < 34:
            return None, None, None, None, None

        ip_header_start = 14
        ip_header = header_Howmany_bytes[ip_header_start:]
        ip_header_lennthggh = (ip_header[0] & 0x0F) * 4

        src_ip = socket.inet_ntoa(ip_header[12:16])
        dst_ip = socket.inet_ntoa(ip_header[16:20])
        proto = ip_header[9]

        transport_header_start = ip_header_start + ip_header_lennthggh
        transport_header = header_Howmany_bytes[transport_header_start:]

        src_port = int.from_bytes(transport_header[0:2], byteorder='big')
        dst_port = int.from_bytes(transport_header[2:4], byteorder='big')

        return src_ip, dst_ip, src_port, dst_port, proto


    # nah
    except Exception as e:
        print(f"[!] Error decoding headerBytes: {e}")
        return None, None, None, None, None
    


# get shit together and return
def sflow_stream():
    print("Starting sflowtool stream...")
    proc = subprocess.Popen(["sflowtool", "-p", "6343"], stdout=subprocess.PIPE, text=True)

    current_sample = {}
    current_agent = "N/A"
    current_time = datetime.now(timezone.utc).isoformat()

    for line in proc.stdout:
        line = line.strip()
        if not line:
            continue

        if line.startswith("agent"):
            parts = line.split(None, 1)
            if len(parts) == 2:
                current_agent = parts[1].strip()

        elif line.startswith("localtime"):
            parts = line.split(None, 1)
            if len(parts) == 2:
                current_time = parts[1].strip()

        elif ": " in line:
            key, value = line.split(": ", 1)
            current_sample[key.strip()] = value.strip()

        elif line.startswith("headerBytes"):
            parts = line.split(None, 1)
            if len(parts) != 2:
                continue

            ermWhatThe_Header = parts[1].strip()    



for flow in sflow_stream():
    print(flow)            