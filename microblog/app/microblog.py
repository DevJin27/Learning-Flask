# from flask import Flask
from app import app # this imports app (variable in app/__init__.py) which is a part of app(the folder/directory)
app.run(debug=True) # this runs the app