import csv
from datetime import date
from models import WorkTimestamp


def new_work_timestamp(row):
    return WorkTimestamp(file=row[0],
                         time="{} {}".format(date.today().strftime("%Y/%m/%d"),
                                             row[1].strip()))


def from_csv(csv_content):
    new_work_timestamps = []
    rows = csv.reader(csv_content)
    for row in rows:
        new_work_timestamps.append(new_work_timestamp(row))
    return new_work_timestamps
