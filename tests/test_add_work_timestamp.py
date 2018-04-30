import sys
from os.path import abspath, dirname, join

TIMEKEEPER_PATH = abspath(join(dirname(__file__), '../timekeeper'))
sys.path.insert(0, TIMEKEEPER_PATH)

import unittest
from compact_work_timestamps import (compact_work_timestamps,
                                     datetime_from_time_string)
from robber import expect


class TestAddWorkTimestamp(unittest.TestCase):
    def test_when_there_are_two_points(self):
        # it returns a single session
        points = ['00:00:01', '00:00:04']
        expected = list(map(datetime_from_time_string, points))

        compacted = compact_work_timestamps(points)

        expect(compacted).to.eq([expected])

    def test_when_there_are_three_points(self):
        # it returns a single session
        points = ['00:00:01', '00:00:04', '00:00:08']
        expected = list(map(datetime_from_time_string, [points[0], points[2]]))

        compacted = compact_work_timestamps(points)

        expect(compacted).to.eq([expected])

    def when_there_are_multiple_session(self):
        # it returns them all
        points = ['00:00:01', '00:04:00', '00:10:00', '00:14:00']
        list(map(datetime_from_time_string, [points[0], points[2]]))

        compacted = compact_work_timestamps(points)

        expect(len(compacted)).to.eq(2)
