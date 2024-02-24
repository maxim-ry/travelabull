from flask import Flask, jsonify, request
import googlemaps

app = Flask(__name__)

def read_api_key():
    file_path = '/Users/Amrit/Desktop/Max_API_key.txt'
    # Read the API key from the file
    with open(file_path, 'r') as file:
        return file.read().strip()

api_key = read_api_key()
gmaps = googlemaps.Client(key=api_key)

@app.route('/autocomplete', methods=['GET']) 
def autocomplete():
    query = request.args.get('query')
    results = gmaps.places_autocomplete(query)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)

