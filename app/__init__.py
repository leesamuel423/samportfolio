import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from peewee import *
from playhouse.shortcuts import model_to_dict
import datetime

load_dotenv()
app = Flask(__name__)

# Enable automatic reloading of templates
app.config['TEMPLATES_AUTO_RELOAD'] = True


# ----------> DATABASE <----------
mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
                     user=os.getenv("MYSQL_USER"),
                     password=os.getenv("MYSQL_PASSWORD"),
                     host=os.getenv("MYSQL_HOST"),
                     port=3306
                     )
print(mydb)

class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb

mydb.connect()
mydb.create_tables([TimelinePost])


# ----------> DATA <----------
user_data = {
        "github": "https://github.com/leesamuel423", 
        "linkedin": "https://www.linkedin.com/in/leesamuel423/"
        }

hobbies_data = [
        {
            "name": "Dog Dad", 
            "image": [
                {
                    "src": "/static/assets/hobbies/agee1.png", 
                    "alt": "image of dog"
                    },
                {
                    "src": "/static/assets/hobbies/agee2.png", 
                    "alt": "image of dog"
                    }
                ],
            "desc": "Dog dad to a spoiled 2 year old Goldador named Agee (A-G). RIP to any disposable income."

            },
        {
            "name": "Gym", 
            "image": [
                ],
            "desc": "Lifting heavy things ... B: 245 / S: 325 / D: 405",
            },
        {
            "name": "Running", 
            "image": [
                {
                    "src": "/static/assets/hobbies/run1.png",
                    "alt": "image of two people smiling before race"
                    },
                {
                    "src": "/static/assets/hobbies/run2.png",
                    "alt": "image of two people smiling after race"
                    },
                ],
            "desc": "Training for a marathon in October 2024. Hoping to do an Ironman one day!"
            },
        ]

education_data = [
        {
            "school": "University of Pennsylvania",
            "degree": "M.S in Computer Science",
            "year": "2024 - 2025"
            },
        {
            "school": "McMaster University",
            "degree": "B.S in Health Sciences Honours",
            "year": "2017 - 2021"
            }
        ]

experiences_data = [
        {
            "company_name": "Meta & Major League Hacking",
            "position": "Production Engineering Fellow",
            "dates": "June 2024 - Present",
            "location": "Toronto, ON",
            "description": [
                "Engineered a dynamic web-based application utilizing Python, Flask, Jinja, MySQL, Nginx, Docker, and unittest.",
                ]
            },
        {
            "company_name": "CS Engineering",
            "position": "Software Engineer",
            "dates": "Jun 2023 - Jan 2024",
            "location": "Los Angeles, CA",
            "description": [
                "Developed and maintained React and Redux based public and internal applications.",
                "Identified and resolved flaky Cypress tests by 80% through strategic network request interceptions, aliases, custom timeouts, addressing state management issues, and utilizing larger VM runners.",
                "Leveraged Jest, Cypress, and React Testing Library for comprehensive unit and end-to-end testing of React, Redux, and Express components, ensuring test isolation and enhancing reliability in support of CI/CD.",
                "Led TypeScript migration to ensure type safety and reinforce data consistency, reducing type errors by 21%.",
                "Employed Docker CLI for project containerization, preflight checks before deployment, and consistent project-wide formatting and linting configurations, ensuring standardization of development across teams.",
                "Mentored engineering teams through the Software Development Life Cycle (SDLC) of full-stack open-source applications, facilitating an AGILE/SCRUM environment to enhance workflow and ensure successful product launches."
                ]
            },
        {
            "company_name": "OSLabs",
            "position": "Software Engineer",
            "dates": "Mar 2023 - Jun 2023",
            "location": "New York, NY",
            "description": [
                "Developed Trydent, an automated Cypress end-to-end (E2E) test generator that captures and analyzes user interactions from XPATH, streamlining the testing process and enhancing developer productivity by over 60%.",
                "Designed and implemented the core functionality for DOM selectors and input monitoring, effectively establishing a bridge between the DOM and service workers, and utilized selector and input data in code generation and implementation of assertion mode to validate the DOM state for more reliable and efficient test code.",
                "Utilized Sass with SMACSS principles for effective CSS preprocessing and enhanced code maintainability, using mixins to develop modular, reusable components that contributed to standardized styling and code efficiency.",
                "Spearheaded comprehensive documentation to improve future development and engineering on-boarding."
                ]
            }
        ]

locations_data = [
        {"country": "Boston, MA, USA", "lat": 42.3601, "long": -71.0589},
        {"country": "Fairfax County, VA, USA", "lat": 38.8462, "long": -77.3064},
        {"country": "Fresno, California, USA", "lat": 36.7378, "long": -119.7871},
        {"country": "Toronto, Ontario, Canada", "lat": 43.651070, "long": -79.347015}
        ]

# ----------> ROUTES <----------

@app.route('/')
def about():
    return render_template('about.html', 
                           title="Samuel Lee", 
                           url=os.getenv("URL"), 
                           user=user_data, 
                           education=education_data, 
                           experiences=experiences_data)

@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', title="Hobbies", hobbies=hobbies_data)

@app.route('/locations')
def map_view():
    return render_template('map.html', title="Map", locationData=locations_data)

@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    name = request.form['name']
    email = request.form['email']
    content = request.form['content']
    timeline_post = TimelinePost.create(name=name, email=email, content=content)

    return model_to_dict(timeline_post)

@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    return {
            'timeline_posts': [
                model_to_dict(p)
                for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
                ]
            }


@app.route('/api/timeline_post/<int:id>', methods=['DELETE'])
def delete_time_line_post(id):
    try:
        post = TimelinePost.get_by_id(id)
        post.delete_instance()
        return {
                'deleted': True
                }
    except:
        return {
                'deleted': False
                }


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
