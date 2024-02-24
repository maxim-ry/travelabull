
import googlemaps
from flask import jsonify

def get_api_key():
    # Assuming your API key is stored in a file named 'api_key.txt'
    api_key_file = '/Users/sultansamid/Documents/GitHub/allCodings/auth.txt'  # Specify the path to your API key file
    with open(api_key_file, 'r') as file:
        return file.read().strip()

gmaps = googlemaps.Client(key=get_api_key())

# Replace 'YOUR_API_KEY' with your actual API key

def find_nearby_places_by_name(place_name, radius=5000, types=None):

    places_result = gmaps.places(query=place_name, radius=radius, type=types)

    recommended_places = []
    for place in places_result['results']:
        place_name = place['name']
        place_address = place.get('formatted_address', 'Address not available')
        place_rating = place.get('rating', 'Rating not available')

        recommended_places.append({
            'Name': place_name,
            'Address': place_address,
            'Rating': place_rating
        })

    return jsonify(recommended_places)