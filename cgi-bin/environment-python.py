#!/usr/bin/python3
import os

print("Content-Type: text/html\r\n\r\n")

print("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Environment Variables - Python</title>
</head>
<body>
    <h1>Environment Variables</h1>
    <p><strong>Language:</strong> Python</p>
    <table border="1" cellpadding="5">
        <tr><th>Variable</th><th>Value</th></tr>""")

for key, value in sorted(os.environ.items()):
    print(f"        <tr><td>{key}</td><td>{value}</td></tr>")

print("""    </table>
    <p><a href="/">Back to Homepage</a></p>
</body>
</html>""")
