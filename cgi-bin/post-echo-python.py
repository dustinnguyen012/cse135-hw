#!/usr/bin/python3
import cgi
import os
import datetime

print("Content-Type: text/html\r\n\r\n")

form = cgi.FieldStorage()

print("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>POST Echo - Python</title>
</head>
<body>
    <h1>POST Echo - Python</h1>

    <h2>Submit Data via POST</h2>
    <form action="post-echo-python.py" method="POST">
        <label>Name: <input type="text" name="name" value="Dustin"></label><br><br>
        <label>Message: <input type="text" name="message" value="Hello via POST!"></label><br><br>
        <input type="submit" value="Submit POST">
    </form>
    <hr>""")

if os.environ.get('REQUEST_METHOD') == 'POST':
    print("<h2>Echoed Data:</h2>")
    print("<table border='1' cellpadding='5'>")
    print("<tr><th>Key</th><th>Value</th></tr>")
    for key in form.keys():
        print(f"<tr><td>{key}</td><td>{form.getvalue(key)}</td></tr>")
    print("</table>")

    print("<h2>Request Info:</h2>")
    print("<table border='1' cellpadding='5'>")
    print(f"<tr><td><b>Method</b></td><td>POST</td></tr>")
    print(f"<tr><td><b>Hostname</b></td><td>{os.environ.get('HTTP_HOST', 'N/A')}</td></tr>")
    print(f"<tr><td><b>Date/Time</b></td><td>{datetime.datetime.now()}</td></tr>")
    print(f"<tr><td><b>User Agent</b></td><td>{os.environ.get('HTTP_USER_AGENT', 'N/A')}</td></tr>")
    print(f"<tr><td><b>IP Address</b></td><td>{os.environ.get('REMOTE_ADDR', 'N/A')}</td></tr>")
    print("</table>")

print("""
    <p><a href="/">Back to Homepage</a></p>
</body>
</html>""")

