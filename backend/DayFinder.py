import json

import requests

def get_nearby_locations(api_key, main_location, num_locations=5):
    base_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"

    # Set up parameters for the API request
    params = {
        'key': api_key,
        'query': f"point of interest {main_location}",  # Use 'point of interest' as a general query
    }

    # Make the API request
    response = requests.get(base_url, params=params)
    results = response.json().get('results', [])



    # Extract relevant information about each place
    nearby_locations = []
    for place in results[:num_locations]:
        location_info = {
            'name': place['name'],
            'address': place.get('formatted_address', ''),
            'latitude': place['geometry']['location']['lat'],
            'longitude': place['geometry']['location']['lng'],
        }
        nearby_locations.append(location_info)

    return [location.get('address', '') for location in json.loads(json.dumps(nearby_locations, indent=2))]

# # Example usage:
#   # Replace with your actual API key
# main_location_name = "New York, NY"  # Replace with the main location you're interested in
# num_locations_to_return = 3

# locations = json.dumps(get_nearby_locations(google_api_key, main_location_name, num_locations_to_return), indent=2)


# addresses_only = [location.get('address', '') for location in json.loads(locations)]


# Print the new list of addresses
# print(addresses_only)