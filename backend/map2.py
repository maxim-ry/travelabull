import random
import googlemaps


def get_api_key():
    # Assuming your API key is stored in a file named 'api_key.txt'
    api_key_file = '/Users/sultansamid/Documents/GitHub/allCodings/auth.txt'  # Specify the path to your API key file
    with open(api_key_file, 'r') as file:
        return file.read().strip()

gmaps = googlemaps.Client(key=get_api_key())

# Define popular place types you want to search for
place_types = ['tourist_attraction']
morning_place_types = ['tourist_attraction','bakery', 'bicycle_store', 'cafe', 'city_hall', 'light_rail_station', 'park', 'subway_station', 'tourist_attraction', 'zoo']
afternoon_place_types = ['tourist_attraction', 'amusement_park', 'aquarium', 'art_gallery', 'church', 'shopping_mall', 'clothing_store', 'courthouse', 'embassy', 'jewelry_store', 'library', 'mosque', 'museum', 'stadium', 'synagogue', 'zoo']
evening_place_types = ['tourist_attraction','bar', 'night_club', 'bowling_alley', 'casino', 'restaurant', 'stadium']

def get_morning_places(city_name, radius = 8046.72):

    # Geocoding the city name to get its coordinates
    geocode_result = gmaps.geocode(city_name)
    if not geocode_result:
        print("City not found.")
        return []
    
    city_location = geocode_result[0]['geometry']['location']
    #hols all the places
    places_list = []
    
    # Search for popular places of each type
    for place_type in morning_place_types:
        places = gmaps.places_nearby(location=city_location, radius=radius, type=place_type)
        for place in places['results']:
            place_details = {
                'name': place['name'],
                'type': place_type,
                'address': place.get('vicinity', 'N/A'),
                'rating': place.get('rating', 'N/A')
            }
            places_list.append(place_details)
    
    # Convert the rating to a float (or 0 if it's "N/A")
    for place in places_list:
        try:
            # Try converting the rating to a float
            place['rating'] = float(place['rating'])
        except ValueError:
            # If conversion fails, set it to a default (e.g., 0) or leave it as "N/A"
            place['rating'] = 0 
            # Replace 0 with your desired default value if needed

    # Shuffle the list of places
    random.shuffle(places_list)


    # Sort the places_list based on rating in descending order
    places_list.sort(key=lambda x: x['rating'], reverse=True)
     
    
    # Select only the first 10 places (or fewer if there are fewer than 10 available)
    selected_places = places_list[:20]

    # Return a random sample of 0 to 4 places
    #random.sample(selected_places, random.randint(1, 4)) 
    return selected_places

# Example usage:
city_name = 'New York'
radius = 5000  # in meters
popular_places = get_morning_places(city_name, radius)
for place in popular_places:
    print("Name:", place['name'])
    print("Address:", place['address'])
    print("Rating:", place['rating'])
    print("Type:", place['type'])
    print()