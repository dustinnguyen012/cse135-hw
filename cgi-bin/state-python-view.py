#!/usr/bin/python3
import os, json

SESSION_DIR = '/tmp/python-sessions'

def get_cookie(name):
    cookies = os.environ.get('HTTP_COOKIE', '')
    for c in cookies.split(';'):
        c = c.strip()
        if c.startswith(name + '='):
            return c.split('=', 1)[1]
    return None

def load_session(sid):
    path = os.path.join(SESSION_DIR, sid + '.json')
    if os.path.exists(path):
        with open(path, 'r') as f:
            return json.load(f)
    return {}

session_id = get_cookie('PYSESSID')
session = load_session(session_id) if session_id else {}

if session:
    content = '''<table border="1" cellpadding="5">
        <tr><th>Field</th><th>Value</th></tr>
        <tr><td>Name</td><td>{}</td></tr>
        <tr><td>Message</td><td>{}</td></tr>
        <tr><td>Saved At</td><td>{}</td></tr>
    </table>'''.format(session.get('name',''), session.get('message',''), session.get('saved_at',''))
else:
    content = '<p>No data saved yet.</p>'

print('Content-Type: text/html\r\n')
print('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>State - Python - View</title>
</head>
<body>
    <h1>State Management - Python</h1>
    <h2>View Saved Data</h2>
    ''' + content + '''
    <br>
    <p><a href="/cgi-bin/state-python-save.py">Go Back and Save/Clear Data</a></p>
    <p><a href="/">Back to Homepage</a></p>
</body>
</html>''')
