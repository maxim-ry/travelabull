from flask import Flask, render_template, request
import requests

app = Flask(__name__)

GOOGLE_MAPS_API_KEY = '/Users/Amrit/Desktop/Max_API_key.txt'

def geocode_city(city):
    # Use Geocoding API to get the coordinates of the city
    geocoding_url = f'https://maps.googleapis.com/maps/api/geocode/json?address={city}&key={GOOGLE_MAPS_API_KEY}'
    geocoding_response = requests.get(geocoding_url)
    geocoding_data = geocoding_response.json()
    
    # Initialize the result dictionary
    result = {'city': city}
    
    # Check if the Geocoding API request was successful
    if geocoding_data['status'] == 'OK':
        # Extract latitude and longitude coordinates from the response
        location = geocoding_data['results'][0]['geometry']['location']
        latitude = location['lat']
        longitude = location['lng']
        
        # Add latitude and longitude to the result dictionary
        result['latitude'] = latitude
        result['longitude'] = longitude
    else:
        # If the Geocoding API request was not successful, print an error message
        print("Error geocoding city")
    
    # Return the result dictionary
    return result

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the city name from the form submission
        city = request.form.get('city')
        
        # Call the geocode_city function to obtain the coordinates
        result = geocode_city(city)
        
        # Return a message indicating success
        return 'Coordinates printed in terminal.'
    else:
        # Render the HTML form for inputting the city name
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


def find_popular_neighborhoods(latitude, longitude):
    # Define parameters for the Nearby Search API request
    radius = 5000  # Search radius in meters
    type = 'neighborhood'  # Type of place to search for
    
    # Construct the Nearby Search API request URL
    url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={latitude},{longitude}&radius={radius}&type={type}&key={GOOGLE_MAPS_API_KEY}'
    
    # Send the Nearby Search API request
    response = requests.get(url)
    data = response.json()
    
    # Check if the Nearby Search API request was successful
    if data['status'] == 'OK':
        # Extract information about the top three results
        neighborhoods = []
        for result in data['results'][:3]:
            name = result['name']
            location = result['geometry']['location']
            neighborhoods.append({'name': name, 'latitude': location['lat'], 'longitude': location['lng']})
        
        return neighborhoods
    else:
        # If the Nearby Search API request was not successful, return an empty list
        print("Error finding popular neighborhoods:", data.get('error_message', ''))
        return []

print(geocode_city('Tampa'))
print(find_popular_neighborhoods(27.9516896, -82.45875269999999))

if __name__ == '__main__':

    print("hello world")
    print(geocode_city('Tampa'))
    print(find_popular_neighborhoods(27.9516896, -82.45875269999999))

    app.run(debug=True)
