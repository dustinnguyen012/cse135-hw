#!/usr/bin/python3
import json
import datetime
import os

print("Content-Type: application/json\r\n\r\n")

response = {
    "hello": "Hello World!",
    "team_member": "Dustin Nguyen",
    "language": "Python",
    "date_time": str(datetime.datetime.now()),
    "ip_address": os.environ.get('REMOTE_ADDR', 'N/A')
}

print(json.dumps(response, indent=4))

