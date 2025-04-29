from sdn_functions import *
import time
from SFLOW.sflowcollect import *

analysis = {'ports' : {}, 'ips' : {}, 'total_packets_analyzed' : 0}

if __name__ == "__main__":
    while True:
        sflow_data = sflow_stream()
        if sflow_data:
            analysis = analyze_netflow_data(analysis, sflow_data)
        
        time.sleep(1)
        