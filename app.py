from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, world! how are you and how are u doing :)'

if __name__ == '__main__':
    app.run()