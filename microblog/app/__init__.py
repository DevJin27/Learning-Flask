from flask import Flask
app = Flask(__name__)
from app import routes #unlike other imports -- why is this one on the bottom of the file?