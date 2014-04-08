from flask import Flask

#this will be our main controller, it will start all process and handle user request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
