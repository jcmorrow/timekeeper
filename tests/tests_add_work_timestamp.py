from expects import expect, equal
from compact_work_timestamps import (compact_work_timestamps,
                                     datetime_from_time_string)


with description('when there are two points'):
    with it('returns a single session'):
        points = ['00:00:01', '00:00:04']
        expected = list(map(datetime_from_time_string, points))

        compacted = compact_work_timestamps(points)

        expect(compacted).to(equal([expected]))


with description('when there are three points'):
    with it('returns a single session'):
        points = ['00:00:01', '00:00:04', '00:00:08']
        expected = list(map(datetime_from_time_string, [points[0], points[2]]))

        compacted = compact_work_timestamps(points)

        expect(compacted).to(equal([expected]))

with description('when there are multiple session'):
    with it('returns them all'):
        points = ['00:00:01', '00:04:00', '00:10:00', '00:14:00']
        expected = list(map(datetime_from_time_string, [points[0], points[2]]))

        compacted = compact_work_timestamps(points)

        expect(len(compacted)).to(equal(2))
