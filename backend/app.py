# Write your Application here
# Description: This is the main file for the backend of the application. 
#It contains the main application logic and the API endpoints.
#most used methods to get all the other files


from flask import Flask, render_template
from map import find_nearby_places_by_name

app = Flask(__name__)

@app.route('/')
def index():
    # Call the function from map.py to get nearby places
    places = find_nearby_places_by_name('restaurant')  # Example: Find nearby restaurants
    return render_template('index.html', places=places)

if __name__ == '__main__':
    app.run(debug=True)