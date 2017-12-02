from bs4 import BeautifulSoup
from timekeeper import app, db
from models import WorkTimestamp
from import_work_timestamps import from_csv
from io import StringIO
import time
import unittest


def page_content(body):
    return BeautifulSoup(body, 'html.parser').get_text().strip()


class ImportFromCsvTest(unittest.TestCase):
    def test_with_csv(self):
        csv = StringIO("""
/import_work_timestamps.py, 14:25:38
/tests_import_work_timestamps.py, 14:26:02
        """.strip())
        work_timestamps = from_csv(csv)

        self.assertEqual(work_timestamps[0].file, '/import_work_timestamps.py')
        self.assertEqual(work_timestamps[1].file,
                         '/tests_import_work_timestamps.py')
        self.assertEqual(work_timestamps[0].time,
                         time.strptime('14:25:38', '%H:%M:%S'))
        self.assertEqual(work_timestamps[1].time,
                         time.strptime('14:26:02', '%H:%M:%S'))


class RequestWithNoData(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = (
            'postgresql://localhost/timekeeper-test'
        )
        app.testing = True
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        pass

    def test_empty_db(self):
        rv = self.app.get('/')
        content = page_content(rv.data)
        self.assertEqual(content, '')
        self.assertEqual(WorkTimestamp.query.all(), [])


if __name__ == '__main__':
    unittest.main()
