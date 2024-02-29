# Given latitude and longitude in JSON, 
# find nearby restaurants and hotels in a range of 10 miles 
# separated into two functions, sorted by highest to lowest rating.
    # if possible, try to add an additional filter after the one above...
    # ...to sort by lowest to highest price per person or night respectively
# Additionally, each function should return in JSON 

# Mostly good, need to **fix the sorting**

from flask import Flask, jsonify, request  # Import necessary modules from Flask

import requests


app = Flask(__name__)  # Create a Flask application instance

GOOGLE_MAPS_API_KEY = 'API_KEY_HERE'  # Set your Google Maps API key

def get_nearby_places(lat, lng, radius, place_type):
    # Function to fetch nearby places (restaurants or hotels) using Google Maps Places API
    url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{lng}&radius={radius}&type={place_type}&key={GOOGLE_MAPS_API_KEY}'
    # Construct the API URL with provided latitude, longitude, radius, place type, and API key

    response = requests.get(url)  # Send a GET request to the API URL
    data = response.json()  # Parse the response JSON
    return data['results']  # Return the list of nearby places

def get_place_details(place_id):
    # Function to fetch details of a place using Google Maps Places API
    url = f'https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&key={GOOGLE_MAPS_API_KEY}'
    # Construct the API URL with provided place ID and API key
    response = requests.get(url)  # Send a GET request to the API URL
    data = response.json()  # Parse the response JSON
    return data['result']  # Return the details of the place

@app.route('/get_restaurants_and_hotels', methods=['POST'])
# Define a route '/get_restaurants_and_hotels' that accepts POST requests

def get_restaurants_and_hotels():
    data = request.json  # Extract JSON data from the request body
    lat = data['latitude']  # Extract latitude from the JSON data
    lng = data['longitude']  # Extract longitude from the JSON data
    radius = 16093.4  # Define the radius in meters (10 miles)
    restaurants = get_nearby_places(lat, lng, radius, 'restaurant')  # Get nearby restaurants
    hotels = get_nearby_places(lat, lng, radius, 'lodging')  # Get nearby hotels

    # Get details for each restaurant and hotel
    for place in restaurants:
        place['details'] = get_place_details(place['place_id'])  # Add details to each restaurant
    for place in hotels:
        place['details'] = get_place_details(place['place_id'])  # Add details to each hotel

    # Sort the restaurants and hotels by user ratings
    restaurants_sorted = sorted(restaurants, key=lambda x: (x.get('rating', 0), -x.get('price_level', 0)), reverse=True)
    hotels_sorted = sorted(hotels, key=lambda x: (x.get('rating', 0), -x.get('price_level', 0)), reverse=True)


    return jsonify({
        'restaurants': restaurants_sorted[:5],  # Return the top 5 restaurants
        'hotels': hotels_sorted[:5]  # Return the top 5 hotels
    })

if __name__ == '__main__':

    # Example usage of the functions to demonstrate their functionality
    # Replace the latitude and longitude with your desired coordinates

    # example_latitude = 27.964157
    # example_longitude = -82.452606
    # example_radius = 16093.4  # 10 miles in meters
    # example_restaurants = get_nearby_places(example_latitude, example_longitude, example_radius, 'restaurant')
    # example_hotels = get_nearby_places(example_latitude, example_longitude, example_radius, 'lodging')

    # print("Example Nearby Restaurants:")
    # for restaurant in example_restaurants[:5]:
    #     print(f"{restaurant['name']} - Rating: {restaurant.get('rating', 'No rating')}")

    # print("\nExample Nearby Hotels:")
    # for hotel in example_hotels[:5]:
    #     print(f"{hotel['name']} - Rating: {hotel.get('rating', 'No rating')}")
        
    app.run(debug=True)  # Run the Flask application in debug mode





