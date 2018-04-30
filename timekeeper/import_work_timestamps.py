import csv
from datetime import date

from .models import WorkTimestamp


def new_work_timestamp(row):
    return WorkTimestamp(file=row[0],
                         time=timestamp(row[1].split()[1].strip()))


def timestamp(time):
    return ' '.join([date.today().strftime("%Y/%m/%d"), time])


def from_csv(csv_content):
    return list(map(new_work_timestamp, csv.reader(csv_content)))
