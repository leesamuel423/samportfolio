import unittest
from peewee import *

from app import TimelinePost

MODELS = [TimelinePost]

test_db = SqliteDatabase(':memory:')

class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)

        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
        test_db.drop_tables(MODELS)

        test_db.close()

    def test_timeline_post(self):
        # Post 1
        first_post = TimelinePost.create(name='John Doe', email='john@example.com', content="Hello World, I\'m John!")
        assert first_post.id == 1

        # Post 2
        second_post = TimelinePost.create(name='Jane Doe', email='jane@example.com', content="Hello World, I\'m Jane!")
        assert second_post.id == 2

        posts = TimelinePost.select().order_by(TimelinePost.id)
        
        # Check count
        assert posts.count() == 2

        # Check for accuracy
        first_post_from_db = posts[0]
        second_post_from_db = posts[1]

        assert first_post_from_db.name == 'John Doe'
        assert first_post_from_db.email == 'john@example.com'
        assert first_post_from_db.content == "Hello World, I'm John!"

        assert second_post_from_db.name == 'Jane Doe'
        assert second_post_from_db.email == 'jane@example.com'
        assert second_post_from_db.content == "Hello World, I'm Jane!"
