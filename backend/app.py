from flask import Flask, request, jsonify, render_template

from flask_cors import CORS  # Install using: pip install flask-cors
import time

import json

import DayFinder
import map as mapper
import description as desc


google_api_key = "API_KEY_HERE"

app = Flask(__name__)
CORS(app)

stored_location_information = None
prev_data = {"key": "initial value"}

@app.route('/api/data', methods=['POST'])
def receive_data():
    global stored_location_information
    
    data = request.json

    # Access the received data
    start_date = data.get('startDate')
    end_date = data.get('endDate')
    specification = data.get('specification')
    location = data.get('location')
    difference_in_days = data.get('differenceInDays')

    # Gets an array of the generation location points for each day.
    general_locations = DayFinder.get_nearby_locations(google_api_key, location, difference_in_days)

    location_information = {}

    location_information = {}

    for day_number, place in enumerate(general_locations, start=1):
        day_key = f"Day {day_number}"
        location_information[day_key] = {'Morning': [], 'Afternoon': [], 'Evening': []}

        # For each time period, extend with location data
        for period in ['Morning', 'Afternoon', 'Evening']:
            places_function = getattr(mapper, f"get_{period.lower()}_places")
            places = places_function(google_api_key, place)

            # Assuming get_location_descriptions expects a list of place dictionaries
            # and returns a list of strings (descriptions for each place)
            descriptions = desc.get_location_descriptions(places)

            # Combine places with their descriptions
            for place, description in zip(places, descriptions):
                place['description'] = description  # Add the description to each place

            location_information[day_key][period].extend(places)

    stored_location_information = location_information

    return jsonify(location_information)

@app.route('/api/data', methods=['GET'])
def get_data():
    global prev_data
    global stored_location_information

    if stored_location_information != prev_data:
        prev_data = stored_location_information
        return jsonify(stored_location_information)
    else:
        return jsonify({"status": "no_change"})



if __name__ == '__main__':
    app.run(debug=True, port=5000)
