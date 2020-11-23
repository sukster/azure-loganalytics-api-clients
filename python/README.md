Update the correct fields and the delimiter in the log2json.py to match the specific log type
Convert the log file to json format by running: python3 log2json.py > pan-threat-log.json
Run this line to send the events to Azure Sentinel: python3 ala-python-data-producer.py -w workspace_id -k primary_key -l "pan_threat_log" -f pan-threat-log.json -v
