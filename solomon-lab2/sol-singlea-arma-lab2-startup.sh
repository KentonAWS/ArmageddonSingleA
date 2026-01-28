#!/bin/bash
# =============================================================================
# Lab 2: EC2 Startup Script (User Data Automation)
# Author: Solomon Sutton
# Purpose: Automatically configure an EC2 instance to host a static website
# Web Server: Apache (httpd)
# =============================================================================

# -----------------------------------------------------------------------------
# STEP 1: System Update
# Ensures all packages are current before installing new software
# -----------------------------------------------------------------------------
yum update -y

# -----------------------------------------------------------------------------
# STEP 2: Install Apache Web Server
# httpd is the Apache package name on Amazon Linux
# -----------------------------------------------------------------------------
yum install -y httpd

# -----------------------------------------------------------------------------
# STEP 3: Start Apache and Enable Auto-Start on Boot
# systemctl start  → starts the service immediately
# systemctl enable → ensures it starts automatically after reboot
# -----------------------------------------------------------------------------
systemctl start httpd
systemctl enable httpd

# -----------------------------------------------------------------------------
# STEP 4: Create the HTML Web Page
# This writes a complete HTML file with inline CSS to the Apache web root
# The page includes: name, background image, embedded image, and 3 sections
# -----------------------------------------------------------------------------
cat <<'EOF' > /var/www/html/index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Solomon Sutton | EC2 Static Site</title>
    <style>
        /* ===== GLOBAL STYLES ===== */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.8;
            color: #f0f0f0;
            background-image: url('https://static.vecteezy.com/system/resources/thumbnails/037/320/188/small/golden-elegance-realistic-3d-black-pedestal-with-palm-leaves-on-black-background-free-photo.jpg');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            background-repeat: no-repeat;
            min-height: 100vh;
        }

        /* ===== OVERLAY FOR READABILITY ===== */
        .overlay {
            background-color: rgba(0, 0, 0, 0.7);
            min-height: 100vh;
            padding: 40px 20px;
        }

        /* ===== CONTAINER ===== */
        .container {
            max-width: 900px;
            margin: 0 auto;
        }

        /* ===== HEADER ===== */
        header {
            text-align: center;
            padding: 40px 0;
            border-bottom: 2px solid rgba(255, 255, 255, 0.2);
            margin-bottom: 40px;
        }

        header h1 {
            font-size: 3rem;
            color: #00d4ff;
            text-shadow: 0 0 20px rgba(0, 212, 255, 0.5);
            margin-bottom: 10px;
        }

        header p {
            font-size: 1.2rem;
            color: #b0b0b0;
            font-style: italic;
        }

        /* ===== CONTENT SECTIONS ===== */
        .section {
            background-color: rgba(255, 255, 255, 0.1);
            border-radius: 12px;
            padding: 30px;
            margin-bottom: 30px;
            backdrop-filter: blur(5px);
            border: 1px solid rgba(255, 255, 255, 0.1);
        }

        .section h2 {
            color: #00d4ff;
            font-size: 1.8rem;
            margin-bottom: 15px;
            border-left: 4px solid #00d4ff;
            padding-left: 15px;
        }

        .section p {
            font-size: 1.1rem;
            color: #e0e0e0;
        }

        /* ===== EMBEDDED IMAGE ===== */
        .image-container {
            text-align: center;
            margin: 30px 0;
        }

        .image-container img {
            max-width: 100%;
            height: auto;
            border-radius: 12px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
            border: 2px solid rgba(0, 212, 255, 0.3);
        }

        .image-container p {
            margin-top: 10px;
            font-size: 0.9rem;
            color: #888;
            font-style: italic;
        }

        /* ===== FOOTER ===== */
        footer {
            text-align: center;
            padding: 30px 0;
            margin-top: 40px;
            border-top: 2px solid rgba(255, 255, 255, 0.2);
        }

        footer p {
            color: #888;
            font-size: 1rem;
        }

        footer .copyright {
            margin-top: 15px;
            font-size: 0.9rem;
            color: #666;
        }
    </style>
</head>
<body>
    <div class="overlay">
        <div class="container">
            
            <!-- HEADER WITH NAME -->
            <header>
                <h1>Solomon Sutton</h1>
                <p>Cloud Engineer by day... and night</p>
            </header>

            <!-- SECTION 1: ABOUT ME -->
            <section class="section">
                <h2>About Me</h2>
                <p>Cloud engineer and explorer</p>
            </section>

            <!-- EMBEDDED IMAGE -->
            <div class="image-container">
                <img src="https://chatgpt.com/backend-api/estuary/public_content/enc/eyJpZCI6Im1fNjk3NWY5OTZiNzcwODE5MWI4ODAzYzUyZGYyOGZjODY6ZmlsZV8wMDAwMDAwMDg4NmM3MWY1OTMxZmNmYjlmNGJkNDllOSIsInRzIjoiMjA0ODAiLCJwIjoicHlpIiwiY2lkIjoiMSIsInNpZyI6IjkxMDhmYTVhZDVmZTRmNzE2YTQzMmU1ZTdmYThkMjM0NDcxMjc5NDU0ZmM4NzM1YTg3ZDYyOTQyNTA1NGQyYjUiLCJ2IjoiMCIsImdpem1vX2lkIjpudWxsLCJjcyI6bnVsbCwiY3AiOm51bGwsIm1hIjpudWxsfQ==" alt="Library Lion">
                <p></p>
            </div>

            <!-- SECTION 2: PROJECT DESCRIPTION -->
            <section class="section">
                <h2>Project Description</h2>
                <p>This lab introduces Linux automation and cloud initialization by writing a startup script that configures an EC2 instance to host a front-facing static website.</p>
            </section>

            <!-- SECTION 3: CONTACT -->
            <section class="section">
                <h2>Contact</h2>
                <p>Questions, collaborations, or inquiries? Send them solodarity@gmail.com.</p>
            </section>

            <!-- FOOTER -->
            <footer>
                <p>&copy; 2026 EleMENTALS &mdash; In Light We Roll.</p>
            </footer>

        </div>
    </div>
</body>
</html>
EOF

# -----------------------------------------------------------------------------
# STEP 5: Set Correct Permissions
# Ensures Apache can read and serve the HTML file
# -----------------------------------------------------------------------------
# chmod 644 /var/www/html/index.html

# -----------------------------------------------------------------------------
# Script Complete - Web server is now running and serving the static page
# Access via: http://<EC2-Public-IP>
# -----------------------------------------------------------------------------
