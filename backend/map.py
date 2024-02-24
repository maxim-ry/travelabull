
import googlemaps

def get_api_key():
    # Assuming your API key is stored in a file named 'api_key.txt'
    api_key_file = '/Users/sultansamid/Documents/GitHub/allCodings/auth.txt'  # Specify the path to your API key file
    with open(api_key_file, 'r') as file:
        return file.read().strip()



gmaps = googlemaps.Client(key=get_api_key())

def find_nearby_places_by_name(place_name, radius=5000, types=None):
    """
    Find recommended places based on the name of the place.
    Parameters:
        - place_name: Name of the place to search for
        - radius: Search radius in meters (default is 5000 meters)
        - types: List of place types to filter the results (e.g., ['restaurant', 'museum'])

    Returns:
        - List of recommended places
    """
    # Make a request to the Google Places API
    places_result = gmaps.places_nearby(location='your_location', keyword=place_name, radius=radius, type=types)

    # Extract relevant information from the API response
    places = []
    for place in places_result['results']:
        places.append({
            'name': place['name'],
            'location': place['geometry']['location'],
            'place_id': place['place_id']
        })

    return places