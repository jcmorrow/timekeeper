# import sys
# from os.path import abspath, dirname, join

# TIMEKEEPER_PATH = abspath(join(dirname(__file__), '../timekeeper'))
# sys.path.insert(0, TIMEKEEPER_PATH)

from bs4 import BeautifulSoup
from db import db
from functools import wraps
from import_work_timestamps import from_csv, timestamp
from io import StringIO
from models import WorkTimestamp
from timekeeper import create_app
import unittest

app = create_app()
app.config['SQLALCHEMY_DATABASE_URI'] = ('postgresql://'
                                         'localhost/timekeeper-test')
app.testing = True


def with_app_context(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        with app.app_context():
            return f(*args, **kwds)
    return wrapper


class TestCase(unittest.TestCase):
    @with_app_context
    def setUp(self):
        db.create_all()
        self.client = app.test_client()


def page_content(body):
    return BeautifulSoup(body, 'html.parser').get_text().strip()


class TestImportWorkTimestamps(TestCase):
    def test_with_csv(self):
        import sys
        print(sys.version)
        csv = StringIO("""
/foo.py, 2017-12-03 14:25:38
/bar.py, 2017-12-03 14:26:02
        """.strip())

        work_timestamps = from_csv(csv)

        files = [wt.file for wt in work_timestamps]
        timestamps = [wt.time for wt in work_timestamps]
        self.assertEqual(['/foo.py', '/bar.py'], files)
        self.assertEqual(list(map(timestamp, ['14:25:38', '14:26:02'])),
                         timestamps)


class TestRequestWithNoData(TestCase):
    @with_app_context
    def test_empty_db(self):
        rv = self.client.get('/')
        content = page_content(rv.data)
        self.assertEqual(content, '')
        self.assertEqual(WorkTimestamp.query.all(), [])
