from typing import Annotated
import ansible_runner
from sendmail import *
from dbSend import sendToDBModel
# Also possible to use subproces mod but nah

# MAIL VARS
SUBJECT = "IP BLOCK"
DEST_MAIL = ""

# DB VARS
DB_TABLE = "ipBlocks"

def noIpPlease(inpIpAddress: Annotated[str, "IP address to block."]):
    extra_vars = {
        "blocked_ip": inpIpAddress
    }

    req_Q = ansible_runner.run(
        private_data_dir='.',   # or wherever your playbook/inventory is
        playbook='blockIpAcl.yml',
        extravars=extra_vars
    )

    # https://ansible.readthedocs.io/projects/runner/en/stable/index.html
    if req_Q.rc != 0:
        print(f"Playbook failed. Return code {req_Q.rc}")
        return(req_Q.status)
    else:
        print("Playbook executed successfully.")
        print("Status:", req_Q.status)
        print("Detailed output:")

        # Send mail
        sendmail(SUBJECT, f"{inpIpAddress} has been blocked", DEST_MAIL)

        # Prep dict for db
        dbOutDict = {"BLOCK_IP": inpIpAddress}

        # Send info to db
        sendToDBModel(dbOutDict, DB_TABLE)
        
        whatTheConfig()
        
        return(req_Q.status)
            
        for someEvent in req_Q.events:
            print(someEvent['stdout'])





# How to use
# block_ip("198.51.100.22")
