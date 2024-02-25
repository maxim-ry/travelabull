from flask import Flask, render_template, request
import requests

app = Flask(__name__)

GOOGLE_MAPS_API_KEY = '/Users/Amrit/Desktop/Max_API_key.txt'

def get_city_and_neighborhoods(city, days=3):
    # Use Geocoding API to get the coordinates of the city
    geocoding_url = f'https://maps.googleapis.com/maps/api/geocode/json?address={city}&key={GOOGLE_MAPS_API_KEY}'
    geocoding_response = requests.get(geocoding_url)
    geocoding_data = geocoding_response.json()
    
    if geocoding_data['status'] == 'OK':
        # Extract latitude and longitude coordinates of the city
        location = geocoding_data['results'][0]['geometry']['location']
        city_latitude = location['lat']
        city_longitude = location['lng']
        
        # Define parameters for the Nearby Search API request
        radius = 40234.7  # 25 miles in meters
        type = 'neighborhood'  # Type of place to search for
        
        # Construct the Nearby Search API request URL
        url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={city_latitude},{city_longitude}&radius={radius}&type={type}&key={GOOGLE_MAPS_API_KEY}'
        
        # Send the Nearby Search API request
        response = requests.get(url)
        data = response.json()
        
        if data['status'] == 'OK':
            neighborhoods = []

            num_neighborhoods = days 

            for result in data['results'][:num_neighborhoods]:  # Limit to the top number neighborhoods indicated by num_neighborhoods
                name = result['name']
                location = result['geometry']['location']
                neighborhoods.append({'name': name, 'latitude': location['lat'], 'longitude': location['lng']})
            
            # Return a string containing city name, its coordinates, and three popular neighborhoods with their coordinates
            return f"City: {city}\nCity Coordinates: ({city_latitude}, {city_longitude})\nPopular Neighborhoods:\n{neighborhoods}"
        else:
            print("Error finding popular neighborhoods:", data.get('error_message', ''))
            return "Error finding popular neighborhoods"
    else:
        print("Error geocoding city")
        return "Error geocoding city"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form.get('city')
        result = get_city_and_neighborhoods(city)
        return result
    else:
        return render_template('index.html')

if __name__ == '__main__':
    print(get_city_and_neighborhoods('Boston'))
    app.run(debug=True)
