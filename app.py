
import os
from pathlib import Path

import mysql.connector
from dotenv import load_dotenv
from flask import Flask

# Load database settings
load_dotenv(Path(__file__).with_name(".env"))

app = Flask(__name__)

@app.route("/week2/")
def counter():
    db = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_DATABASE")
    )

    cursor = db.cursor()

    try:
        # Increase page views by one
        cursor.execute(
            "UPDATE page_views SET views = views + 1 WHERE id = 1"
        )

        # Read the updated value
        cursor.execute(
            "SELECT views FROM page_views WHERE id = 1"
        )
        views = cursor.fetchone()[0]

        db.commit()
    finally:
        cursor.close()
        db.close()

    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Linux Project - Week 2</title>

        <style>
            * {{
                box-sizing: border-box;
            }}

            body {{
                background: #101827;
                color: #f8fafc;
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 45px 20px;
            }}

            .container {{
                max-width: 750px;
                margin: auto;
            }}

            .subtitle {{
                color: #60a5fa;
                font-weight: bold;
                letter-spacing: 2px;
            }}

            h1 {{
                font-size: 36px;
                margin-bottom: 10px;
            }}

            p {{
                color: #cbd5e1;
		font-size: 18px;
                line-height: 1.7;
            }}

            .counter {{
                background: #1c2b44;
                border: 1px solid #334155;
                border-radius: 12px;
                text-align: center;
                padding: 35px;
                margin: 30px 0;
            }}

            .number {{
                color: #60a5fa;
                font-size: 65px;
                font-weight: bold;
                margin: 10px;
            }}

            .tag {{
                display: inline-block;
                background: #283750;
                padding: 9px 14px;
                margin: 4px;
                border-radius: 6px;
                color: #e2e8f0;
            }}

            .info {{
                margin-top: 0px;
                padding-top: 0px;
            }}

            a {{
                color: #60a5fa;
            }}
		.info-box {{
    		background: #1c2b44;
    		border: 1px solid #334155;
    		border-radius: 12px;
    		padding: 25px;
    		margin: 20px 0;
}}
        </style>
    </head>

    <body>
        <div class="container">

            <div class="subtitle">LINUX PROJECT / WEEK 02</div>

            <h1>My Linux Web App :)</h1>

            <p>
                This is my second Linux server project.
                The website uses Python, Flask and MariaDB
                to keep track of the page loads.
            </p>

            <div class="counter">
                <h2>Page Loads</h2>
                <div class="number">{views}</div>
                <p>Try to refresh the page to increase the counter!</p>
            </div>

            <h2>Technologies used</h2>

            <span class="tag">Ubuntu</span>
            <span class="tag">Nginx</span>
            <span class="tag">Python</span>
            <span class="tag">Flask</span>
            <span class="tag">MariaDB</span>
            <span class="tag">Gunicorn</span>

            <div class="info">
   
    <div class="info-box">
        <h2>How does it work?</h2>
        <p>
            Nginx receives the HTTP request and forwards
            it to the Flask application. Flask updates
            the counter stored in the MariaDB database.
        </p>
    </div>

    <div class="info-box">
        <h2>About this project</h2>
        <p>
            The application runs on an Ubuntu server.
            Gunicorn serves the Flask application,
            and systemd starts it automatically.
        </p>
    </div>

    <div class="info-box">
        <h2>Database and persistence</h2>
        <p>
            The counter is stored in a MariaDB database
            in the page_views table.
            I tested it by rebooting the virtual machine.
            The counter kept its value and continued counting.
        </p>
    </div>

    <p>
        <a href="/">Visit my Week 1 site :)</a>
    </p>

    <p>
        <a href="https://github.com/EmppuLyytinen/Linuxweek2">
            My GitHub project :)
        </a>
    </p>

</div>
</div>
    </body>
    </html>
    """

