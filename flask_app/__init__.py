# initialize the app
from flask import Flask
import os

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_KEY")
