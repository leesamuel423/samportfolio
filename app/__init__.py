import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

# ---------- DATA ----------
user_data = {"name": "Sam", "about" : "Software Engineer. Teacher. Runner. Professional Sleeper.", "profilepic": "./static/img/sam.jpg", "github": "link", "linkedin": "link"}

hobbies_data = [
    {"name": "Gym", "image": "static/img/hobbies/gym.jpg"},
    {"name": "Running", "image": "static/img/hobbies/running.jpg"},
    {"name": "Binging KDramas", "image": "static/img/hobbies/kdrama.jpg"}
]

education_data = [
    {
        "school": "School Name 1",
        "img": "/static/img/school/school1.jpg",
        "degree": "M.S in Computer Science",
        "year": 2025
    },
    {
        "school": "School Name 2",
        "img": "/static/img/school/school2.jpg",
        "degree": "B.S in Computer Science",
        "year": 2021
    }
]

experiences_data = [
    {
        "company_name": "XYZ",
        "position": "Software Engineer",
        "dates": "2023 - 2024",
        "location": "US",
        "description": [
            "bullet point 1",
            "bullet point 2",
        ]
    },
    {
        "company_name": "XYZ2",
        "position": "Software Engineer",
        "dates": "2020 - 2021",
        "location": "US",
        "description": [
            "bullet point 1",
            "bullet point 2",
        ]
    },
]

locations_data = [
    {"country": "Boston, MA, USA", "lat": 42.3601, "long": -71.0589},
    {"country": "Fairfax County, VA, USA", "lat": 38.8462, "long": -77.3064},
    {"country": "Fresno, California, USA", "lat": 36.7378, "long": -119.7871},
    {"country": "Toronto, Ontario, Canada", "lat": 43.651070, "long": -79.347015}
]

# ---------- ROUTES ----------

@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"), user=user_data)

@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', title="Hobbies", hobbies=hobbies_data)

@app.route('/education')
def education():
    return render_template('education.html', title="Education", education=education_data)

@app.route('/experiences')
def experiences():
    return render_template('experiences.html', title="Experiences", experiences=experiences_data)

@app.route('/locations')
def map_view():
    return render_template('map.html', title="Map", locationData=locations_data)

