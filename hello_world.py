from Flask import Flask

app = Flask(__name__)

def hello_world():
    return 'Hello World'
