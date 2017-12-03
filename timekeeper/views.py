from flask import render_template
from flask.blueprints import Blueprint
from models import WorkTimestamp

work_timestamps = Blueprint('work_timestamps', __name__,
                            template_folder='templates')


@work_timestamps.route('/')
def index():
    work_timestamps = WorkTimestamp.query.all()
    return render_template("work_timestamps_index.html",
                           work_timestamps=work_timestamps)
