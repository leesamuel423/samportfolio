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
        "year": "2024 - 2025",
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


def get_blog_posts():
    """Read all blog posts from the blogs directory."""
    posts = []
    blog_dir = os.path.join(os.path.dirname(__file__), "blogs")

    try:
        # Look for directories in the blogs folder
        for dirname in os.listdir(blog_dir):
            dir_path = os.path.join(blog_dir, dirname)
            if os.path.isdir(dir_path):
                # Look for index.md in each directory
                index_path = os.path.join(dir_path, "index.md")
                if os.path.exists(index_path):
                    try:
                        with open(index_path, "r", encoding="utf-8") as file:
                            # Parse front matter and content
                            post = frontmatter.load(file)

                            # Convert the content from markdown to HTML
                            html_content = markdown.markdown(
                                post.content,
                                extensions=[
                                    "fenced_code",
                                    "tables",
                                    "codehilite",
                                ],
                            )

                            # Use directory name as slug
                            posts.append(
                                {
                                    "slug": dirname,
                                    "title": post.metadata.get(
                                        "title", "Untitled"
                                    ),
                                    "date": post.metadata.get("date"),
                                    "description": post.metadata.get(
                                        "description", ""
                                    ),
                                    "content": html_content,
                                    "assets_path": f"/static/blogs/{dirname}/assets",
                                }
                            )
                    except Exception as e:
                        print(f"Error processing {dirname}: {str(e)}")
                        continue
    except Exception as e:
        print(f"Error reading blog directory: {str(e)}")
        return []

    # Sort posts by date, newest first
    return sorted(posts, key=lambda x: x["date"], reverse=True)


@app.route("/")
def about():
    return render_template(
        "about.html",
        url=os.getenv("URL"),
        user=user_data,
        education=education_data,
        experiences=experiences_data,
        blog_posts=get_blog_posts(),
    )


@app.route("/blog/<slug>")
def blog_post(slug):
    blog_dir = os.path.join(os.path.dirname(__file__), "blogs")
    post_path = os.path.join(blog_dir, slug, "index.md")

    if not os.path.exists(post_path):
        abort(404)

    with open(post_path, "r", encoding="utf-8") as file:
        post = frontmatter.load(file)
        html_content = markdown.markdown(
            post.content, extensions=["fenced_code", "tables", "codehilite"]
        )

    return render_template(
        "blog_post.html",
        post={
            "title": post.metadata.get("title"),
            "date": post.metadata.get("date"),
            "content": html_content,
            "assets_path": f"/static/blogs/{slug}/assets",
        },
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
