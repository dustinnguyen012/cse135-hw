#!/usr/bin/python3
import os, json, sys, urllib.parse
from datetime import datetime

print("Content-Type: application/json\r\n\r\n")

method = os.environ.get('REQUEST_METHOD', 'GET')
data = {}

if method in ('GET', 'DELETE'):
    query_string = os.environ.get('QUERY_STRING', '')
    data = dict(urllib.parse.parse_qsl(query_string))
elif method in ('POST', 'PUT'):
    content_type = os.environ.get('CONTENT_TYPE', '')
    content_length = int(os.environ.get('CONTENT_LENGTH', 0))
    body = sys.stdin.read(content_length) if content_length > 0 else ''
    if 'application/json' in content_type:
        try:
            data = json.loads(body)
        except:
            data = {}
    else:
        data = dict(urllib.parse.parse_qsl(body))

response = {
    "echo": "Echo - Python",
    "method": method,
    "hostname": os.environ.get('HTTP_HOST', 'N/A'),
    "date_time": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    "user_agent": os.environ.get('HTTP_USER_AGENT', 'N/A'),
    "ip_address": os.environ.get('REMOTE_ADDR', 'N/A'),
    "received_data": data
}

print(json.dumps(response, indent=4))
