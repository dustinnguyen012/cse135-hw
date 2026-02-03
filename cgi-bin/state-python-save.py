#!/usr/bin/python3
import os, json, sys, hashlib, time, urllib.parse
from datetime import datetime

SESSION_DIR = '/tmp/python-sessions'
os.makedirs(SESSION_DIR, exist_ok=True)

def get_cookie(name):
    cookies = os.environ.get('HTTP_COOKIE', '')
    for c in cookies.split(';'):
        c = c.strip()
        if c.startswith(name + '='):
            return c.split('=', 1)[1]
    return None

def create_session_id():
    return hashlib.sha256((str(time.time()) + str(os.getpid())).encode()).hexdigest()

def load_session(sid):
    path = os.path.join(SESSION_DIR, sid + '.json')
    if os.path.exists(path):
        with open(path, 'r') as f:
            return json.load(f)
    return {}

def save_session(sid, data):
    path = os.path.join(SESSION_DIR, sid + '.json')
    with open(path, 'w') as f:
        json.dump(data, f)

method = os.environ.get('REQUEST_METHOD', 'GET')
session_id = get_cookie('PYSESSID') or create_session_id()

if method == 'POST':
    content_length = int(os.environ.get('CONTENT_LENGTH', 0))
    body = sys.stdin.read(content_length) if content_length > 0 else ''
    params = dict(urllib.parse.parse_qsl(body))
    session = load_session(session_id)
    session['name'] = params.get('name', '')
    session['message'] = params.get('message', '')
    session['saved_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    save_session(session_id, session)
    print('Set-Cookie: PYSESSID=' + session_id + '; path=/')
    print('Location: /cgi-bin/state-python-view.py')
    print('Status: 302 Found')
    print('Content-Type: text/html\r\n')
    print('<html><body><p>Redirecting...</p></body></html>')
else:
    print('Set-Cookie: PYSESSID=' + session_id + '; path=/')
    print('Content-Type: text/html\r\n')
    print('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>State - Python - Save</title>
</head>
<body>
    <h1>State Management - Python</h1>
    <h2>Save Your Data</h2>
    <form action="/cgi-bin/state-python-save.py" method="POST">
        <label>Name: <input type="text" name="name"></label><br><br>
        <label>Message: <input type="text" name="message"></label><br><br>
        <input type="submit" value="Save Data">
    </form>
    <br>
    <form action="/cgi-bin/state-python-clear.py" method="POST">
        <input type="submit" value="Clear Data">
    </form>
    <br>
    <p><a href="/cgi-bin/state-python-view.py">View Saved Data</a></p>
    <p><a href="/">Back to Homepage</a></p>
</body>
</html>''')
