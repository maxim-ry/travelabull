# Write your Application here
# Description: This is the main file for the backend of the application. 
#It contains the main application logic and the API endpoints.
#most used methods to get all the other files

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"