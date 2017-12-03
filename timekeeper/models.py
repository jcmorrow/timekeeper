from db import db


class WorkTimestamp(db.Model):
    __tablename__ = 'work_timestamps'

    id = db.Column(db.Integer, primary_key=True)
    file = db.Column(db.String(), nullable=False)
    time = db.Column(db.DateTime(), nullable=False)
