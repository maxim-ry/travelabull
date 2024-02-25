from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

GOOGLE_MAPS_API_KEY = '/Users/Amrit/Desktop/Max_API_key.txt'

@app.route('/get_popular_neighborhoods', methods=['GET'])
def get_popular_neighborhoods():
    city = request.args.get('city')  # Get the city name from the query parameters
    
    # Use Geocoding API to get the coordinates of the city
    geocoding_url = f'https://maps.googleapis.com/maps/api/geocode/json?address={city}&key={GOOGLE_MAPS_API_KEY}'
    geocoding_response = requests.get(geocoding_url)
    geocoding_data = geocoding_response.json()
    
    if geocoding_data['status'] == 'OK':
        location = geocoding_data['results'][0]['geometry']['location']
        lat = location['lat']
        lng = location['lng']

        # Perform a nearby search to find popular neighborhoods around the city
        radius = 5000  # Set the radius for the nearby search (in meters)
        types = 'neighborhood'  # Specify the type of place to search for
        nearby_search_url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{lng}&radius={radius}&type={types}&key={GOOGLE_MAPS_API_KEY}'
        nearby_search_response = requests.get(nearby_search_url)
        nearby_search_data = nearby_search_response.json()
        
        if nearby_search_data['status'] == 'OK':
            # Extract relevant information from the results
            popular_neighborhoods = []
            for place in nearby_search_data['results']:
                popular_neighborhoods.append({
                    'name': place['name'],
                    'location': place['geometry']['location']
                })
            
            return jsonify({'status': 'success', 'popular_neighborhoods': popular_neighborhoods})
        else:
            return jsonify({'status': 'error', 'message': 'Error fetching nearby neighborhoods'})
    else:
        return jsonify({'status': 'error', 'message': 'Error geocoding city'})

test_city = 'Tampa'
test_response = requests.get(f'http://127.0.0.1:5000/get_popular_areas?city={test_city}')
print("Response Status Code:", test_response.status_code)
print("Response Content:", test_response.content)

# if __name__ == '__main__':
#     app.run(debug=True)


# test_city = 'Tampa'
# test_response = requests.get(f'http://127.0.0.1:5000/get_popular_areas?city={test_city}')
# print("Response Status Code:", test_response.status_code)
# print("Response Content:", test_response.content)

# if __name__ == '__main__':

#     test_city = 'New York'
#     test_response = requests.get(f'http://127.0.0.1:5000/get_popular_areas?city={test_city}')
#     print("Response Status Code:", test_response.status_code)
#     print("Response Content:", test_response.content)


#     app.run(debug=True)


