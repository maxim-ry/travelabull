# Write your Application here
# Description: This is the main file for the backend of the application. 
#It contains the main application logic and the API endpoints.
#most used methods to get all the other files

from flask import Flask, render_template, request
from map import find_nearby_places_by_name

app = Flask(__name__)

@app.route('/')
# def index():
#     return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    place_name = request.form['place_name']
    radius = int(request.form.get('radius', 5000))  # Get optional radius value
    types = request.form.getlist('types')  # Get optional list of place types

    # Call the function with user input and handle potential errors
    try:
        recommended_places = find_nearby_places_by_name(place_name, radius, types)
    except Exception as e:  # Catch potential errors from Google Maps API
        error_message = f"Error: {str(e)}"
        return render_template('index.html', error_message=error_message)

    return render_template('index.html', places=recommended_places)

if __name__ == '__main__':
    app.run(debug=True)
