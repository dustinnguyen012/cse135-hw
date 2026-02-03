#!/usr/bin/python3
import cgi
import os
import http.cookies
import hashlib
import time
import json

# Session file directory
SESSION_DIR = "/tmp/python-sessions"
os.makedirs(SESSION_DIR, exist_ok=True)

def get_session_id(cookies):
    if 'PYSESSID' in cookies:
        return cookies['PYSESSID'].value
    return None

def create_session_id():
    return hashlib.sha256(str(time.time()).encode()).hexdigest()

def load_session(session_id):
    path = os.path.join(SESSION_DIR, session_id + ".json")
    if os.path.exists(path):
        with open(path, 'r') as f:
            return json.load(f)
    return {}

def save_session(session_id, data):
    path = os.path.join(SESSION_DIR, session_id + ".json")
    with open(path, 'w') as f:
        json.dump(data, f)

# Read cookies
cookies = http.cookies.SimpleCookie()
cookie_header = os.environ.get('HTTP_COOKIE', '')
cookies.load(cookie_header)

# Get or create session
session_id = get_session_id(cookies)
if not session_id:
    session_id = create_session_id()

session_data = load_session(session_id)

# Handle form submission
form = cgi.FieldStorage()
if 'username' in form:
    session_data['username'] = form.getvalue('username')
    save_session(session_id, session_data)

# Set cookie and print headers
print(f"Set-Cookie: PYSESSID={session_id}; path=/")
print("Content-Type: text/html\r\n")

print(f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python Sessions - Page 1</title>
</head>
<body>
    <h1>Python Sessions - Page 1</h1>

    <form action="sessions-python-1.py" method="GET">
        <label>Enter Your Name: <input type="text" name="username" value=""></label><br><br>
        <input type="submit" value="Save Name to Session">
    </form>

    <br><hr><br>""")

if 'username' in session_data:
    print(f"<p><b>Name:</b> {session_data['username']}</p>")
else:
    print("<p><b>Name:</b> You do not have a name set</p>")

print("""
    <br>
    <p><a href="sessions-python-2.py">Go to Session Page 2</a></p>
    <p><a href="sessions-python-destroy.py">Destroy Session</a></p>
    <p><a href="/">Back to Homepage</a></p>
</body>
</html>""")
