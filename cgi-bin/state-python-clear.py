#!/usr/bin/python3
import os

SESSION_DIR = '/tmp/python-sessions'

def get_cookie(name):
    cookies = os.environ.get('HTTP_COOKIE', '')
    for c in cookies.split(';'):
        c = c.strip()
        if c.startswith(name + '='):
            return c.split('=', 1)[1]
    return None

session_id = get_cookie('PYSESSID')
if session_id:
    path = os.path.join(SESSION_DIR, session_id + '.json')
    if os.path.exists(path):
        os.remove(path)

print('Set-Cookie: PYSESSID=; path=/; expires=Thu, 01 Jan 1970 00:00:00 GMT')
print('Location: /cgi-bin/state-python-save.py')
print('Status: 302 Found')
print('Content-Type: text/html\r\n')
print('<html><body><p>Redirecting...</p></body></html>')
