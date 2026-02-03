#!/usr/bin/python3
import os
import http.cookies
import json

SESSION_DIR = "/tmp/python-sessions"

def get_session_id(cookies):
    if 'PYSESSID' in cookies:
        return cookies['PYSESSID'].value
    return None

def load_session(session_id):
    path = os.path.join(SESSION_DIR, session_id + ".json")
    if os.path.exists(path):
        with open(path, 'r') as f:
            return json.load(f)
    return {}

# Read cookies
cookies = http.cookies.SimpleCookie()
cookie_header = os.environ.get('HTTP_COOKIE', '')
cookies.load(cookie_header)

session_id = get_session_id(cookies)
session_data = load_session(session_id) if session_id else {}

print("Content-Type: text/html\r\n\r\n")

print("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python Sessions - Page 2</title>
</head>
<body>
    <h1>Python Sessions - Page 2</h1>
    <hr>""")

if 'username' in session_data:
    print(f"<p><b>Name:</b> {session_data['username']}</p>")
    print("<p>Your session is persisting across pages!</p>")
else:
    print("<p><b>Name:</b> No session data found.</p>")
    print("<p>Go back to Page 1 and enter a name first!</p>")

print("""
    <br>
    <p><a href="sessions-python-1.py">Go back to Session Page 1</a></p>
    <p><a href="sessions-python-destroy.py">Destroy Session</a></p>
    <p><a href="/">Back to Homepage</a></p>
</body>
</html>""")
