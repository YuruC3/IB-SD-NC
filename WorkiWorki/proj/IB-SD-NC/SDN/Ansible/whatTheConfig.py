from typing import Annotated
import ansible_runner
from .sendmail import *
import datetime
from .dbSend import sendToDBModel
# Also possible to use subproces mod but nah

# MAIL VARS
SUBJECT = "IP BLOCK"
DEST_MAIL = ""

# DB VARS
DB_TABLE = "confBck"

# OTHER VARS
#CURRENT_CONF = ""

def whatTheConfig():
    #global CURRENT_CONF

    req_Q = ansible_runner.run(
        private_data_dir='.',   
        playbook='getRunConf.yml'
    )

    # https://ansible.readthedocs.io/projects/runner/en/stable/index.html
    if req_Q.rc != 0:
        print(f"Playbook failed. Return code {req_Q.rc}")
        return(req_Q.status)
    else:

        try:
            with open('swithcCongif.txt', 'r') as f:
                CURRENT_CONF = f.read()
            print("Success")
        except Exception as e:
            print("nuh uh", e)
            return(2)

        print("Playbook executed successfully.")
        print("Status:", req_Q.status)
        #print("Detailed output:")


        # Send mail | datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        sendmail(SUBJECT, f"Config backed up at {datetime.today().strftime('%Y-%m-%d %H:%M:%S')}", DEST_MAIL)

        # Prep dict for db
        dbOutDict = {"RUN_CONF": CURRENT_CONF}

        # Send info to db
        sendToDBModel(dbOutDict, DB_TABLE)

        return(req_Q.status)
            
        for someEvent in req_Q.events:
            print(someEvent['stdout'])

# Example usage
# get_current_config()
# print(CURRENT_CONF)


# How to use
# block_ip("198.51.100.22")
