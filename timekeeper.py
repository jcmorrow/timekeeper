from flask import Flask, render_template
from db import db
from views import work_timestamps
from flask_migrate import Migrate
from models import WorkTimestamp


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.default')
    app.config.from_envvar('CONFIG_FILE')
    db.init_app(app)
    app.register_blueprint(work_timestamps, url_prefix='')
    Migrate(app, db)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
