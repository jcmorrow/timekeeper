from flask import Flask

app = Flask(__name__)
app.config.from_object('config.default')
app.config.from_envvar('CONFIG_FILE')


@app.route('/')
def hello():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
