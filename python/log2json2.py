#!/usr/bin/env python3

# Author: Ludek Suk
# Update the FIELD_NAMES and FIELD_DELIMITER to match your log type
# The sample_log.txt provided with this script is a Palo Alto Threat Log
# Convert the log file to json format by running: python3 log2json.py > pan-threat-log.json

# Credits:
# https://stackoverflow.com/questions/54689242/convert-log-file-into-json-file-using-python

import json
import sys

FIELD_NAMES = ['Domain','Receive Time','Serial #','Type','Threat/Content Type','Config Version','Generate Time','Source address','Destination address','NAT Source IP','NAT Destination IP','Rule','Source User','Destination User','Application','Virtual System','Source Zone','Destination Zone','Inbound Interface','Outbound Interface','Log Action','Time Logged','Session ID','Repeat Count','Source Port','Destination Port','NAT Source Port','NAT Destination Port','Flags','IP Protocol','Action','URL/Filename','Threat/Content Name','Category','Severity','Direction','Sequence Number','Action Flags','Source Country','Destination Country','cpadding','contenttype','pcap_id','filedigest','cloud','url_idx','user_agent','filetype','xff','referer','sender','subject','recipient','reportid','DG Hierarchy Level 1','DG Hierarchy Level 2','DG Hierarchy Level 3','DG Hierarchy Level 4','Virtual System Name','Device Name','file_url','Source VM UUID','Destination VM UUID','http_method','Tunnel ID/IMSI','Monitor Tag/IMEI','Parent Session ID','Parent Session Start Time','Tunnel','thr_category','contentver','sig_flags','SCTP Association ID','Payload Protocol ID','http_headers','URL Category List','UUID for rule','HTTP/2 Connection','dynusergroup_name']
FIELD_DELIMITER = ','
LOG_FILE = str(sys.argv[1])

def log_lines_to_json(log_file, field_names, field_delimiter):
    result = []
    with open(log_file) as f:
        lines = f.readlines()
        for line in lines:
            fields = line.split(field_delimiter)
            result.append({field_name: fields[idx] for idx, field_name in enumerate(field_names)})
    return result

try:
    entries = log_lines_to_json(LOG_FILE, FIELD_NAMES, FIELD_DELIMITER)
    for entry in entries:
        print(json.dumps(entry))
except:
    print("========================== USAGE ==========================")
    print("Update the FIELD_NAMES and FIELD_DELIMITER to match your log type.")
    print("The sample_log.txt provided with this script is a Palo Alto Threat Log.")
    print("The correct syntax is: python3 log2json.py ../data-samples/sample_log.txt")
    sys.exit(1)