#!/usr/bin/env python3

# Author: Ludek Suk
# You need to update the FIELD_NAMES and FIELD_DELIMITER to match your log type
# The sample_log.txt provided is a Palo Alto Threat Log

# Reference:
# https://stackoverflow.com/questions/54689242/convert-log-file-into-json-file-using-python

import json

FIELD_NAMES = ['receive_time', 'serial', 'type', 'subtype', 'time_generated', 'src', 'dst', 'natsrc', 'natdst', 'rule', 'srcuser', 'dstuser', 'app', 'vsys', 'from', 'to', 'inbound_if', 'outbound_if', 'sessionid', 'repeatcnt', 'sport', 'dport', 'natsport', 'natdport', 'flags', 'proto', 'action', 'misc', 'threatid', 'category', 'severity', 'direction', 'seqno', 'actionflags', 'srcloc', 'dstloc', 'contenttype', 'pcap_id', 'filedigest', 'cloud', 'url_idx', 'user_agent', 'filetype', 'xff', 'referer', 'sender', 'subject', 'recipient', 'reportid', 'dg_hier_level', 'vsys_name', 'device_name', 'src_uuid', 'dst_uuid', 'http_method', 'tunnel_id', 'monitortag', 'parent_session_id', 'parent_start_time', 'tunnel', 'contentver', 'assoc_id', 'ppid', 'http_headers']
FIELD_DELIMITER = ','


def log_lines_to_json(log_file, field_names, field_delimiter):
    result = []
    with open(log_file) as f:
        lines = f.readlines()
        for line in lines:
            fields = line.split(field_delimiter)
            result.append({field_name: fields[idx] for idx, field_name in enumerate(field_names)})
    return result

entries = log_lines_to_json('sample_log.txt', FIELD_NAMES, FIELD_DELIMITER)
for entry in entries:
     print(json.dumps(entry))
