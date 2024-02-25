from flask import Flask, jsonify
import googlemaps

app = Flask(__name__)

def read_api_key():
    file_path = '/Users/Amrit/Desktop/Max_API_key.txt'
    # Read the API key from the file
    with open(file_path, 'r') as file:
        return file.read().strip()

api_key = read_api_key()
gmaps = googlemaps.Client(key=api_key)

@app.route('/')
def index():
    # Define locations
    locations = [
        {'lat': 40.7128, 'lng': -74.0060},  # New York City
        {'lat': 34.0522, 'lng': -118.2437}, # Los Angeles
        {'lat': 51.5074, 'lng': -0.1278}    # London
        # Add more locations as needed
    ]
    return jsonify(locations)

if __name__ == '__main__':
    app.run(debug=True)
