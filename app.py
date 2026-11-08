
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
    <html>
    <head>
        <title>My Linux week2 project</title>
    </head>
    <body>
        <h1>My Linux Web App</h1>
        <p>This page uses Python, Flask and MariaDB.</p>
        <h2>Page loads: {views}</h2>
        <p>Running on Ubuntu and Nginx soon! :D</p>
    </body>
    </html>
    """
