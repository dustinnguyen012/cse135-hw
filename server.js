const express = require('express');
const app = express();
const crypto = require('crypto');

// Session storage (in memory)
const sessions = {};

// Middleware
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

// Simple cookie parser middleware
app.use((req, res, next) => {
    const cookieHeader = req.headers.cookie;
    req.cookies = {};
    if (cookieHeader) {
        cookieHeader.split(';').forEach(cookie => {
            const parts = cookie.split('=');
            const key = parts[0].trim();
            const value = parts.slice(1).join('=').trim();
            req.cookies[key] = value;
        });
    }
    next();
});

// Helper: get real IP from forwarded header or fallback
function getIP(req) {
    return req.headers['x-forwarded-for'] || req.connection.remoteAddress;
}

// Helper: get or create session
function getSession(req) {
    let sessionId = req.cookies['NODESESSID'];
    if (!sessionId || !sessions[sessionId]) {
        sessionId = crypto.randomBytes(16).toString('hex');
        sessions[sessionId] = {};
    }
    return { sessionId, session: sessions[sessionId] };
}

// ==========================================
// HELLO HTML
// ==========================================
app.get('/hw2/hello-html-node', (req, res) => {
    res.send(`<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello HTML - NodeJS</title>
</head>
<body>
    <h1>Hello World!</h1>
    <p><strong>Team Member:</strong> Dustin Nguyen</p>
    <p><strong>Language:</strong> NodeJS</p>
    <p><strong>Date/Time:</strong> ${new Date().toString()}</p>
    <p><strong>Your IP:</strong> ${getIP(req)}</p>
    <p><a href="/">Back to Homepage</a></p>
</body>
</html>`);
});

// ==========================================
// HELLO JSON
// ==========================================
app.get('/hw2/hello-json-node', (req, res) => {
    res.json({
        hello: "Hello World!",
        team_member: "Dustin Nguyen",
        language: "NodeJS",
        date_time: new Date().toString(),
        ip_address: getIP(req)
    });
});

// ==========================================
// ENVIRONMENT VARIABLES
// ==========================================
app.get('/hw2/environment-node', (req, res) => {
    let rows = '';
    Object.keys(req.headers).forEach(key => {
        rows += `<tr><td>${key}</td><td>${req.headers[key]}</td></tr>`;
    });
    const envVars = ['NODE_ENV', 'PORT', 'PATH', 'HOME', 'USER', 'HOSTNAME'];
    envVars.forEach(key => {
        if (process.env[key]) {
            rows += `<tr><td>${key}</td><td>${process.env[key]}</td></tr>`;
        }
    });
    res.send(`<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Environment Variables - NodeJS</title>
</head>
<body>
    <h1>Environment Variables</h1>
    <p><strong>Language:</strong> NodeJS</p>
    <table border="1" cellpadding="5">
        <tr><th>Variable</th><th>Value</th></tr>
        ${rows}
    </table>
    <p><a href="/">Back to Homepage</a></p>
</body>
</html>`);
});

// ==========================================
// ECHO (handles GET, POST, PUT, DELETE)
// ==========================================
app.all('/hw2/echo-node', (req, res) => {
    const body = req.body || {};
    const query = req.query || {};
    const data = Object.keys(body).length > 0 ? body : query;

    res.json({
        echo: "Echo - NodeJS",
        method: req.method,
        hostname: req.hostname,
        date_time: new Date().toString(),
        user_agent: req.headers['user-agent'],
        ip_address: getIP(req),
        received_data: data
    });
});

// ==========================================
// STATE - SAVE PAGE
// ==========================================
app.get('/hw2/state-node-save', (req, res) => {
    const { sessionId } = getSession(req);
    res.cookie('NODESESSID', sessionId);
    res.send(`<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><title>State - NodeJS - Save</title></head>
<body>
    <h1>State Management - NodeJS</h1>
    <h2>Save Your Data</h2>
    <form action="/hw2/state-node-save" method="POST">
        <label>Name: <input type="text" name="name"></label><br><br>
        <label>Message: <input type="text" name="message"></label><br><br>
        <input type="submit" value="Save Data">
    </form>
    <br>
    <form action="/hw2/state-node-clear" method="POST">
        <input type="submit" value="Clear Data">
    </form>
    <br>
    <p><a href="/hw2/state-node-view">View Saved Data</a></p>
    <p><a href="/">Back to Homepage</a></p>
</body>
</html>`);
});

app.post('/hw2/state-node-save', (req, res) => {
    const { sessionId, session } = getSession(req);
    session.name = req.body.name || '';
    session.message = req.body.message || '';
    session.saved_at = new Date().toString();
    sessions[sessionId] = session;
    res.cookie('NODESESSID', sessionId);
    res.redirect('/hw2/state-node-view');
});

// ==========================================
// STATE - VIEW PAGE
// ==========================================
app.get('/hw2/state-node-view', (req, res) => {
    const { sessionId, session } = getSession(req);
    res.cookie('NODESESSID', sessionId);
    let content = '';
    if (session.name || session.message) {
        content = `<table border="1" cellpadding="5">
            <tr><th>Field</th><th>Value</th></tr>
            <tr><td>Name</td><td>${session.name || ''}</td></tr>
            <tr><td>Message</td><td>${session.message || ''}</td></tr>
            <tr><td>Saved At</td><td>${session.saved_at || ''}</td></tr>
        </table>`;
    } else {
        content = '<p>No data saved yet.</p>';
    }
    res.send(`<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><title>State - NodeJS - View</title></head>
<body>
    <h1>State Management - NodeJS</h1>
    <h2>View Saved Data</h2>
    ${content}
    <br>
    <p><a href="/hw2/state-node-save">Go Back and Save/Clear Data</a></p>
    <p><a href="/">Back to Homepage</a></p>
</body>
</html>`);
});

// ==========================================
// STATE - CLEAR
// ==========================================
app.post('/hw2/state-node-clear', (req, res) => {
    const sessionId = req.cookies ? req.cookies['NODESESSID'] : null;
    if (sessionId && sessions[sessionId]) {
        delete sessions[sessionId];
    }
    res.clearCookie('NODESESSID');
    res.redirect('/hw2/state-node-save');
});

// ==========================================
// SESSIONS - PAGE 1
// ==========================================
app.get('/hw2/sessions-node-1', (req, res) => {
    const { sessionId, session } = getSession(req);
    if (req.query.username) {
        session.username = req.query.username;
        sessions[sessionId] = session;
    }
    res.cookie('NODESESSID', sessionId);
    let nameDisplay = session.username
        ? `<p><b>Name:</b> ${session.username}</p>`
        : '<p><b>Name:</b> You do not have a name set</p>';
    res.send(`<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NodeJS Sessions - Page 1</title>
</head>
<body>
    <h1>NodeJS Sessions - Page 1</h1>
    <form action="/hw2/sessions-node-1" method="GET">
        <label>Enter Your Name: <input type="text" name="username" value=""></label><br><br>
        <input type="submit" value="Save Name to Session">
    </form>
    <br><hr><br>
    ${nameDisplay}
    <br>
    <p><a href="/hw2/sessions-node-2">Go to Session Page 2</a></p>
    <p><a href="/hw2/sessions-node-destroy">Destroy Session</a></p>
    <p><a href="/">Back to Homepage</a></p>
</body>
</html>`);
});

// ==========================================
// SESSIONS - PAGE 2
// ==========================================
app.get('/hw2/sessions-node-2', (req, res) => {
    const { sessionId, session } = getSession(req);
    res.cookie('NODESESSID', sessionId);
    let content = session.username
        ? `<p><b>Name:</b> ${session.username}</p><p>Your session is persisting across pages!</p>`
        : '<p><b>Name:</b> No session data found.</p><p>Go back to Page 1 and enter a name first!</p>';
    res.send(`<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NodeJS Sessions - Page 2</title>
</head>
<body>
    <h1>NodeJS Sessions - Page 2</h1>
    <hr>
    ${content}
    <br>
    <p><a href="/hw2/sessions-node-1">Go back to Session Page 1</a></p>
    <p><a href="/hw2/sessions-node-destroy">Destroy Session</a></p>
    <p><a href="/">Back to Homepage</a></p>
</body>
</html>`);
});

// ==========================================
// SESSIONS - DESTROY
// ==========================================
app.get('/hw2/sessions-node-destroy', (req, res) => {
    const sessionId = req.cookies['NODESESSID'];
    if (sessionId && sessions[sessionId]) {
        delete sessions[sessionId];
    }
    res.clearCookie('NODESESSID');
    res.redirect('/hw2/sessions-node-1');
});

// ==========================================
// START SERVER
// ==========================================
const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Node server running on port ${PORT}`);
});
