from flask import Flask, request, jsonify, render_template

from flask_cors import CORS  # Install using: pip install flask-cors
import time

import json

import DayFinder
import map as mapper
import description as desc


google_api_key = "AIzaSyAeBKDh9v04QH92KSF_BbDdEOrzxR0n-7Y"

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

    for day_number, place in enumerate(general_locations, start=1):
        # Use the day number as the key
        day_key = f"Day {day_number}"

        # Initialize a dictionary for the day
        location_information[day_key] = {
            'Morning': [],
            'Afternoon': [],
            'Evening': []
        }

        # Append morning, afternoon, and evening places to the respective lists
        location_information[day_key]['Morning'].extend(mapper.get_morning_places(google_api_key, place))
        location_information[day_key]['Afternoon'].extend(mapper.get_afternoon_places(google_api_key, place))
        location_information[day_key]['Evening'].extend(mapper.get_evening_places(google_api_key, place))

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
