#!/usr/bin/python3
import datetime
import os

print("Content-Type: text/html\r\n\r\n")

print("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello HTML - Python</title>
</head>
<body>
    <h1>Hello World!</h1>
    <p><strong>Team Member:</strong> Dustin Nguyen</p>
    <p><strong>Language:</strong> Python</p>
    <p><strong>Date/Time:</strong> """ + str(datetime.datetime.now()) + """</p>
    <p><strong>Your IP:</strong> """ + os.environ.get('REMOTE_ADDR', 'N/A') + """</p>
    <p><a href="/">Back to Homepage</a></p>
</body>
</html>""")
