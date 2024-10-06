from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome to my Python API, by Aurélien Rogé'


if __name__ == '__main__':
    app.run(debug=True)