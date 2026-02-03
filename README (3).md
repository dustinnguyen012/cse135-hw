# CSE 135 - HW2: Server Side Basics and Analytics 3+ Ways

## Team Information
- **Team Member:** Dustin Nguyen
- **Course:** CSE 135 - Winter 2026
- **University:** UCSD

---

## Server Information
- **Domain:** https://dustinng.site
- **IP Address:** 138.68.13.11
- **Server OS:** Ubuntu 24.04 LTS
- **Web Server:** Apache 2.4.58
- **Languages:** Perl 5.38, PHP 8.3, Python 3.12.3, NodeJS 18.19.1

---

## Grader Access

### SSH Access
- **Username:** grader
- **Password:** cse135grader
- **Login Command:** `ssh grader@138.68.13.11`

### Website Access (Basic Auth)
- **Username:** user
- **Password:** cse135user

---

## Homework 2 - All Program Links

### Perl (Provided Demo)
| Program | Link |
|---------|------|
| Hello, Perl! (HTML) | https://dustinng.site/cgi-bin/perl-hello-html-world.pl |
| Hello, Perl! (JSON) | https://dustinng.site/cgi-bin/perl-hello-json-world.pl |
| Environment Variables | https://dustinng.site/cgi-bin/perl-env.pl |
| GET Echo | https://dustinng.site/cgi-bin/perl-get-echo.pl |
| POST Echo | https://dustinng.site/cgi-bin/perl-post-echo.pl |
| General Echo | https://dustinng.site/cgi-bin/perl-general-echo.pl |
| Sessioning | https://dustinng.site/cgi-bin/perl-sessions-1.pl |

### Echo Form
| Program | Link |
|---------|------|
| Echo Form - All Languages | https://dustinng.site/hw2/echo-form.html |

### PHP
| Program | Link |
|---------|------|
| Hello, PHP! (HTML) | https://dustinng.site/hw2/hello-html-php.php |
| Hello, PHP! (JSON) | https://dustinng.site/hw2/hello-json-php.php |
| Environment Variables | https://dustinng.site/hw2/environment-php.php |
| Echo | https://dustinng.site/hw2/echo-php.php |
| State Management | https://dustinng.site/hw2/state-php-save.php |

### Python
| Program | Link |
|---------|------|
| Hello, Python! (HTML) | https://dustinng.site/cgi-bin/hello-html-python.py |
| Hello, Python! (JSON) | https://dustinng.site/cgi-bin/hello-json-python.py |
| Environment Variables | https://dustinng.site/cgi-bin/environment-python.py |
| Echo | https://dustinng.site/cgi-bin/echo-python.py |
| State Management | https://dustinng.site/cgi-bin/state-python-save.py |

### NodeJS
| Program | Link |
|---------|------|
| Hello, Node! (HTML) | https://dustinng.site/hw2/hello-html-node |
| Hello, Node! (JSON) | https://dustinng.site/hw2/hello-json-node |
| Environment Variables | https://dustinng.site/hw2/environment-node |
| Echo | https://dustinng.site/hw2/echo-node |
| State Management | https://dustinng.site/hw2/state-node-save |

---

## Analytics - 3 Approaches

### Approach 1: Google Analytics
Google Analytics (GA4) was set up using the gtag.js library with Measurement ID G-4RBGZMDQ5L. The tracking script was added to the head of index.html. GA4 provides detailed insights into traffic sources, user demographics, page views, and session duration, making it the industry standard for web analytics.

### Approach 2: LogRocket
LogRocket was set up as a session replay and monitoring tool. The LogRocket SDK was installed via npm and served locally from /logrocket.min.js to avoid CDN issues. LogRocket captures full session replays including mouse movements, clicks, and form interactions, and also provides network request monitoring and console error tracking. The project ID is pwe2tk/cse135-project.

### Approach 3: Microsoft Clarity (Free Choice)

**What was evaluated:** Hotjar, Matomo, Plausible, and Microsoft Clarity were all considered. Hotjar's free plan limits session recordings to 35 per day. Matomo required a complex self-hosted setup. Plausible lacked session replay functionality.

**Why Clarity was chosen:** It is completely free with no usage limits, requires only a single script tag to set up, and is maintained by Microsoft. It also automatically masks sensitive user data like passwords by default, making it a privacy-conscious choice.

**Analysis:** Clarity provides session recordings and heatmaps. Session recordings replay user activity including scrolling, clicking, and page navigation. Heatmaps show which parts of the page get the most interaction. Together these complement Google Analytics' quantitative data with qualitative behavioral insights.

---

## Technical Implementation Notes

### CGI Setup
- Apache mod_cgi was enabled and the ScriptAlias was configured to point to /var/www/html/cgi-bin/
- Perl and Python scripts are served directly via CGI with executable permissions
- The shebang lines (#!/usr/bin/perl and #!/usr/bin/python3) are used to specify the interpreter

### PHP Setup
- PHP scripts are served directly by Apache via libapache2-mod-php
- PHP files are located in /var/www/html/hw2/
- PHP sessions are used for state management, with session files stored in the default /tmp directory

### Python Setup
- Python CGI scripts are located in /var/www/html/cgi-bin/
- Custom session management was implemented using cookies and JSON files stored in /tmp/python-sessions/
- Note: Python 3.12 shows a deprecation warning for the cgi module, which is slated for removal in Python 3.13

### NodeJS Setup
- A single Express.js server (server.js) handles all Node routes on port 3000
- Apache mod_proxy forwards /hw2/*-node requests to the Node server at 127.0.0.1:3000
- Session data is stored in memory using a JavaScript object
- The Node server runs as a systemd service (nodeapp.service) for automatic startup on reboot
- The X-Forwarded-For header is used to pass the real client IP through the Apache proxy

### Echo Form
- A single echo-form.html page targets all three language endpoints (PHP, Python, NodeJS)
- Supports GET, POST, PUT, and DELETE methods via JavaScript fetch
- Supports both x-www-form-urlencoded and application/json encoding
- Falls back to basic GET/POST forms inside noscript tags when JavaScript is disabled

### Analytics Integration
- Google Analytics uses gtag.js loaded from googletagmanager.com
- LogRocket is served locally from /logrocket.min.js after being installed via npm
- Microsoft Clarity uses its standard script tag loaded from clarity.ms

---

## GitHub Repository
- **Repository:** https://github.com/dustinnguyen012/cse135-hw
- **Deployment:** Manual git pull workflow
  1. Edit files and push to GitHub
  2. SSH into server: `ssh root@138.68.13.11`
  3. Navigate: `cd /var/www/html`
  4. Pull changes: `git pull origin main`
