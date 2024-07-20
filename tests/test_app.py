import unittest
import os
os.environ['TESTING'] = 'true'

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)

        # Test for title
        assert "<title>it's sam</title>" in html

        # Test for meta tags
        assert '<meta property="og:title" content="Samuel Lee Website" />' in html
        assert '<meta property="og:description" content="Samuel Lee\'s Website" />' in html

        # Test header links
        assert '<a href="/timeline">say-hi</a>' in html
        assert '<a href="/locations">locations</a>' in html
        assert '<a href="/hobbies">hobbies</a>' in html
        assert '<a href="/#">brain-dump</a>' in html
        assert '<a href="https://www.linkedin.com/in/leesamuel423/">linkedin</a>' in html
        assert '<a href="https://github.com/leesamuel423">github</a>' in html

    def test_timeline(self):
        response = self.client.get("api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 0

        # Posts Data
        posts = [
                {"name": "Audrey", "email": "audrey@example.com", "content": "Test 1"},
                {"name": "Sam", "email": "sam@example.com", "content": "Test 2"},
                {"name": "Kanmani", "email": "kanmani@example.com", "content": "Test 3"},
                {"name": "Jess", "email": "jess@example.com", "content": "Test 4" }
                ]

        # Add Posts
        for p in posts:
            self.client.post("/api/timeline_post", data=p)

        # Check for Posts 
        response = self.client.get("api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 4


    def test_malformed_timeline_post(self):
        response = self.client.post("api/timeline_post", data={"email": "john@example.com", "content": "Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid name" in html

        response = self.client.post("api/timeline_post", data={"name": "John Doe", "email": "john@example.com", "content": ""})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid content" in html

        response = self.client.post("api/timeline_post", data={"name": "John Doe","email": "not-an-email", "content": "Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid email" in html

