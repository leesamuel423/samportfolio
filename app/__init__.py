import datetime
import os
import re

import frontmatter
import markdown
from dotenv import load_dotenv
from flask import Flask, abort, make_response, render_template, request
from flask_assets import Bundle, Environment
from peewee import *
from playhouse.shortcuts import model_to_dict

load_dotenv()
app = Flask(__name__, static_url_path="/static", static_folder="static")

# Enable automatic reloading of templates
app.config["TEMPLATES_AUTO_RELOAD"] = True

assets = Environment(app)
assets.url = app.static_url_path

scss = Bundle("styles/main.scss", filters="libsass", output="gen/main.css")
assets.register("scss_all", scss)

# ----------> DATABASE <----------
if os.getenv("TESTING") == "true":
    print("Running in test mode")
    mydb = SqliteDatabase("file:memory?mode=memory&cache=shared", uri=True)
else:
    mydb = MySQLDatabase(
        os.getenv("MYSQL_DATABASE"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        host=os.getenv("MYSQL_HOST"),
        port=3306,
    )
print(mydb)

mydb.connect()


# ----------> DATA <----------
user_data = {
    "github": "https://github.com/leesamuel423",
    "linkedin": "https://www.linkedin.com/in/leesamuel423/",
}


education_data = [
    {
        "school": "university of pennsylvania",
        "degree": "masters in computer science",
        "year": "2024 - 2026",
    },
    {
        "school": "mcmaster university",
        "degree": "bachelors of health sciences honours",
        "year": "2017 - 2021",
    },
]

experiences_data = [
    {
        "company_name": "google",
        "position": "software engineer intern",
        "dates": "incoming summer 2025",
    },
    {
        "company_name": "starbourne labs",
        "position": "full stack software engineer",
        "dates": "aug 2024 - present",
    },
    {
        "company_name": "alki",
        "position": "founder | software engineer",
        "dates": "jul 2023 - present",
    },
    {
        "company_name": "cs engineering",
        "position": "full stack software engineer",
        "dates": "jun 2023 - feb 2025",
    },
    {
        "company_name": "meta",
        "position": "production engineering fellow",
        "dates": "jun 2024 - sep 2024",
    },
    {
        "company_name": "oslabs",
        "position": "software engineer",
        "dates": "mar 2023 - jun 2023",
    },
]

# ----------> ROUTES <----------


@app.route("/")
def about():
    return render_template(
        "about.html",
        url=os.getenv("URL"),
        user=user_data,
        education=education_data,
        experiences=experiences_data,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
