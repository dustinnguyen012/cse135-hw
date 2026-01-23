# CSE 135 HW1 - Web Server Configuration

## Team Members
- Dustin Nguyen

## Server Information
- **Domain**: dustinng.site
- **IP Address**: 138.68.13.11
- **Server**: Ubuntu 24.04 LTS with Apache 2.4.58

## Grader Account Access

### SSH Access
- **Username**: grader
- **Password**: cse135grader
- **Login Command**: `ssh grader@138.68.13.11`

### Website Access
- **Username**: user
- **Password**: cse135user

## Site URLs

### Main Sites
- **Primary Site**: https://dustinng.site
- **Personal Page**: https://dustinng.site/members/dustin.html
- **Collector**: https://collector.dustinng.site
- **Reporting**: https://reporting.dustinng.site

### Homework 1 Files
- **PHP Test**: https://dustinng.site/hw1/hello.php
- **GoAccess Report**: https://dustinng.site/hw1/report.html

## GitHub Repository
- **Repository**: https://github.com/dustinnguyen012/cse135-hw
- **Deployment Process**:
  1. Code changes are pushed to GitHub repository
  2. SSH into server: `ssh root@138.68.13.11`
  3. Navigate to web directory: `cd /var/www/html`
  4. Pull latest changes: `git pull origin main`
  5. Changes are immediately live on https://dustinng.site


### Compression (mod_deflate)
- Enabled for HTML, CSS, JavaScript, and XML files
- Reduces transfer size by approximately 60-70%
- Verified using Chrome DevTools: `Content-Encoding: gzip` appears in response headers

### Server Header Modification
**Attempted Methods:**
1. Modified `ServerTokens Prod` and `ServerSignature Off` in `/etc/apache2/conf-available/security.conf`
2. Used `Header always unset/set Server` directives in apache2.conf
3. Added Header directives to VirtualHost configuration
4. Installed mod_security2 and attempted SecServerSignature directive

