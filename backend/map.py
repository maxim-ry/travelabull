
import googlemaps
import os

def get_api_key():
    # Assuming your API key is stored in a file named 'api_key.txt'
    api_key_file = '/Users/sultansamid/Documents/GitHub/allCodings/auth.txt'  # Specify the path to your API key file
    with open(api_key_file, 'r') as file:
        return file.read().strip()


gmaps = googlemaps.Client(key=get_api_key())

