# Write your Application here
# Description: This is the main file for the backend of the application. 
#It contains the main application logic and the API endpoints.
#most used methods to get all the other files

# AMRIT

from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')

def index(): 
    return render_template('autocomplete.html')

if __name__ == "__main__": 
    app.run(debug=True)

#<!DOCTYPE html>
#<html lang="en">
#<head>
#    <meta charset="UTF-8">
#    <meta name="viewport" content="width=device-width, initial-scale=1.0">
#    <title>Document</title>
#</head>
#<body>
#    Hello World 2
#</body>
#</html>

