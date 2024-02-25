from flask import Flask, render_template, request
import requests

app = Flask(__name__)

GOOGLE_MAPS_API_KEY = 'AIzaSyAeBKDh9v04QH92KSF_BbDdEOrzxR0n-7Y'

# **Days needs to be modified**

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
        rank_by = 'prominence'  # Rank results by prominence
        
        # Construct the Nearby Search API request URL with rank_by parameter
        url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={city_latitude},{city_longitude}&radius={radius}&type={type}&rankby={rank_by}&key={GOOGLE_MAPS_API_KEY}'
        
        # Send the Nearby Search API request
        response = requests.get(url)
        data = response.json()
        
        if data['status'] == 'OK':
            neighborhoods = []

            num_neighborhoods = min(days, len(data['results']))  # Ensure number of neighborhoods is within the available results

            for result in data['results'][:num_neighborhoods]:  # Limit to the top number neighborhoods indicated by days or available results
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
    
    # uncomment below if you want to test what is being output
    # print(get_city_and_neighborhoods('New York'))
    
    app.run(debug=True)
