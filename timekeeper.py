from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('config.default')
app.config.from_envvar('CONFIG_FILE')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import WorkTimestamp


@app.route('/')
def hello():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
