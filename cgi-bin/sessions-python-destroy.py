#!/usr/bin/python3
import os
import http.cookies

SESSION_DIR = "/tmp/python-sessions"

# Read cookies
cookies = http.cookies.SimpleCookie()
cookie_header = os.environ.get('HTTP_COOKIE', '')
cookies.load(cookie_header)

if 'PYSESSID' in cookies:
    session_id = cookies['PYSESSID'].value
    session_file = os.path.join(SESSION_DIR, session_id + ".json")
    if os.path.exists(session_file):
        os.remove(session_file)

# Expire the cookie
print("Set-Cookie: PYSESSID=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/")
print("Location: /cgi-bin/sessions-python-1.py\r\n\r\n")
