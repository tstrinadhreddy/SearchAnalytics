from flask import Flask
from .Business import XmlParser
app = Flask(__name__)

@app.route('/')
def hello_world():
    return XmlParser.loadRSS()
    #return 'Hello, World!'