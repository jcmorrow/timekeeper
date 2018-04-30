from flask import Flask
from views import work_timestamps
from flask_migrate import Migrate


def create_app():
    from db import db
    app = Flask(__name__)
    app.config.from_pyfile('config/default.py')
    app.config.from_envvar('CONFIG_FILE')
    db.init_app(app)
    app.register_blueprint(work_timestamps, url_prefix='')
    Migrate(app, db)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
