import random
import googlemaps

# Define popular place types you want to search for
place_types = ['tourist_attraction']
morning_place_types = ['bakery', 'cafe', 'park', 'tourist_attraction', 'zoo']
afternoon_place_types = ['tourist_attraction', 'amusement_park', 'aquarium', 'art_gallery', 'museum', 'stadium', 'zoo', 'hindu_temple']
evening_place_types = ['tourist_attraction','bar', 'night_club', 'bowling_alley', 'casino', 'restaurant', 'stadium']

def get_morning_places(key, city_name, description = '', radius = 4800):
    gmaps = googlemaps.Client(key)

    # Geocoding the city name to get its coordinates
    geocode_result = gmaps.geocode(city_name)
    if not geocode_result:
        print("City not found.")
        return []
    
    city_location = geocode_result[0]['geometry']['location']
    #hols all the places
    morning_places_list = []
    
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
            morning_places_list.append(place_details)
    
    # Convert the rating to a float (or 0 if it's "N/A")
    for place in morning_places_list:
        try:
            # Try converting the rating to a float
            place['rating'] = float(place['rating'])
        except ValueError:
            # If conversion fails, set it to a default (e.g., 0) or leave it as "N/A"
            place['rating'] = 0 
            # Replace 0 with your desired default value if needed

    # Shuffle the list of places
    random.shuffle(morning_places_list)


    # Sort the places_list based on rating in descending order
    morning_places_list.sort(key=lambda x: x['rating'], reverse=True)
     
    
    # Select only the first 20 places (or fewer if there are fewer than 20 available)
    selected_places = morning_places_list[:20]

    # Return a random sample more then 2 or equal less then 3 places
    return random.sample(selected_places, random.randint(2, 3)) 


def get_afternoon_places(key, city_name, description = '', radius = 4800):

    gmaps = googlemaps.Client(key)

    # Geocoding the city name to get its coordinates
    geocode_result = gmaps.geocode(city_name)
    if not geocode_result:
        print("City not found.")
        return []
    
    city_location = geocode_result[0]['geometry']['location']
    #hols all the places
    afternoon_place_list = []
    
    # Search for popular places of each type
    for place_type in afternoon_place_types:
        places = gmaps.places_nearby(location=city_location, radius=radius, type=place_type)
        for place in places['results']:
            place_details = {
                'name': place['name'],
                'type': place_type,
                'address': place.get('vicinity', 'N/A'),
                'rating': place.get('rating', 'N/A')
            }
            afternoon_place_list.append(place_details)
    
    # Convert the rating to a float (or 0 if it's "N/A")
    for place in afternoon_place_list:
        try:
            # Try converting the rating to a float
            place['rating'] = float(place['rating'])
        except ValueError:
            # If conversion fails, set it to a default (e.g., 0) or leave it as "N/A"
            place['rating'] = 0 
            # Replace 0 with your desired default value if needed

    # Shuffle the list of places
    random.shuffle(afternoon_place_list)


    # Sort the places_list based on rating in descending order
    afternoon_place_list.sort(key=lambda x: x['rating'], reverse=True)
     
    
    # Select only the first 10 places (or fewer if there are fewer than 10 available)
    selected_places = afternoon_place_list[:20]

    # Return a random sample more then 2 or equal less then 5 places
    #random.sample(selected_places, random.randint(1, 4)) 

    return random.sample(selected_places, random.randint(2, 3)) 


def get_evening_places(key, city_name, description = '', radius = 4800):

    gmaps = googlemaps.Client(key)

    # Geocoding the city name to get its coordinates
    geocode_result = gmaps.geocode(city_name)
    if not geocode_result:
        print("City not found.")
        return []
    
    city_location = geocode_result[0]['geometry']['location']
    #hols all the places
    evening_place_list = []
    
    # Search for popular places of each type
    for place_type in evening_place_types:
        places = gmaps.places_nearby(location=city_location, radius=radius, type=place_type)
        for place in places['results']:
            place_details = {
                'name': place['name'],
                'type': place_type,
                'address': place.get('vicinity', 'N/A'),
                'rating': place.get('rating', 'N/A')
            }
            evening_place_list.append(place_details)
    
    # Convert the rating to a float (or 0 if it's "N/A")
    for place in evening_place_list:
        try:
            # Try converting the rating to a float
            place['rating'] = float(place['rating'])
        except ValueError:
            # If conversion fails, set it to a default (e.g., 0) or leave it as "N/A"
            place['rating'] = 0 
            # Replace 0 with your desired default value if needed

    # Shuffle the list of places
    random.shuffle(evening_place_list)


    # Sort the places_list based on rating in descending order
    evening_place_list.sort(key=lambda x: x['rating'], reverse=True)
     
    
    # Select only the first 10 places (or fewer if there are fewer than 10 available)
    selected_places = evening_place_list[:20]

    # Return a random sample more then 2 or equal less then 5 places
    #random.sample(selected_places, random.randint(1, 4)) 

    return random.sample(selected_places, random.randint(2, 3)) 


# city_name = 'Boston Massachusetts'
# popular_places = get_afternoon_places(city_name)
# for place in popular_places:
#     print("Name:", place['name'])
#     print("Address:", place['address'])
#     print("Rating:", place['rating'])
#     print("Type:", place['type'])
#     print()
# city_name = 'South Tampa'
# popular_places = get_evening_places(city_name)
# for place in popular_places:
#     print("Name:", place['name'])
#     print("Address:", place['address'])
#     print("Rating:", place['rating'])
#     print("Type:", place['type'])
#     print()



 #Example usage:

# city_name = '30 Rockefeller Plaza, New York, NY 10112, United States'
# popular_places = get_morning_places(city_name)
# for place in popular_places:
#     print("Name:", place['name'])
#     print("Address:", place['address'])
#     print("Rating:", place['rating'])
#     print("Type:", place['type'])
#     print()

# city_name = '30 Rockefeller Plaza, New York, NY 10112, United States'
# popular_places = get_evening_places(city_name)
# for place in popular_places:
#     print("Name:", place['name'])
#     print("Address:", place['address'])
#     print("Rating:", place['rating'])
#     print("Type:", place['type'])
#     print()

# city_name = '30 Rockefeller Plaza, New York, NY 10112, United States'
# popular_places = get_afternoon_places(city_name)
# for place in popular_places:
#     print("Name:", place['name'])
#     print("Address:", place['address'])
#     print("Rating:", place['rating'])
#     print("Type:", place['type'])
#     print()
import random
import googlemaps

# Define popular place types you want to search for
place_types = ['tourist_attraction']
morning_place_types = ['bakery', 'cafe', 'city_hall', 'light_rail_station', 'park', 'subway_station', 'tourist_attraction', 'zoo']
afternoon_place_types = ['tourist_attraction', 'amusement_park', 'aquarium', 'art_gallery', 'shopping_mall', 'clothing_store', 'courthouse', 'embassy', 'museum', 'stadium', 'zoo']
evening_place_types = ['tourist_attraction','bar', 'night_club', 'bowling_alley', 'casino', 'restaurant', 'stadium']

def get_morning_places(key, city_name, description = '', radius = 4800):
    gmaps = googlemaps.Client(key)

    # Geocoding the city name to get its coordinates
    geocode_result = gmaps.geocode(city_name)
    if not geocode_result:
        print("City not found.")
        return []
    
    city_location = geocode_result[0]['geometry']['location']
    #hols all the places
    morning_places_list = []
    
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
            morning_places_list.append(place_details)
    
    # Convert the rating to a float (or 0 if it's "N/A")
    for place in morning_places_list:
        try:
            # Try converting the rating to a float
            place['rating'] = float(place['rating'])
        except ValueError:
            # If conversion fails, set it to a default (e.g., 0) or leave it as "N/A"
            place['rating'] = 0 
            # Replace 0 with your desired default value if needed

    # Shuffle the list of places
    random.shuffle(morning_places_list)


    # Sort the places_list based on rating in descending order
    morning_places_list.sort(key=lambda x: x['rating'], reverse=True)
     
    
    # Select only the first 20 places (or fewer if there are fewer than 20 available)
    selected_places = morning_places_list[:20]

    # Return a random sample more then 2 or equal less then 3 places
    return random.sample(selected_places, random.randint(2, 3)) 


def get_afternoon_places(key, city_name, description = '', radius = 4800):

    gmaps = googlemaps.Client(key)

    # Geocoding the city name to get its coordinates
    geocode_result = gmaps.geocode(city_name)
    if not geocode_result:
        print("City not found.")
        return []
    
    city_location = geocode_result[0]['geometry']['location']
    #hols all the places
    afternoon_place_list = []
    
    # Search for popular places of each type
    for place_type in afternoon_place_types:
        places = gmaps.places_nearby(location=city_location, radius=radius, type=place_type)
        for place in places['results']:
            place_details = {
                'name': place['name'],
                'type': place_type,
                'address': place.get('vicinity', 'N/A'),
                'rating': place.get('rating', 'N/A')
            }
            afternoon_place_list.append(place_details)
    
    # Convert the rating to a float (or 0 if it's "N/A")
    for place in afternoon_place_list:
        try:
            # Try converting the rating to a float
            place['rating'] = float(place['rating'])
        except ValueError:
            # If conversion fails, set it to a default (e.g., 0) or leave it as "N/A"
            place['rating'] = 0 
            # Replace 0 with your desired default value if needed

    # Shuffle the list of places
    random.shuffle(afternoon_place_list)


    # Sort the places_list based on rating in descending order
    afternoon_place_list.sort(key=lambda x: x['rating'], reverse=True)
     
    
    # Select only the first 10 places (or fewer if there are fewer than 10 available)
    selected_places = afternoon_place_list[:20]

    # Return a random sample more then 2 or equal less then 5 places
    #random.sample(selected_places, random.randint(1, 4)) 

    return random.sample(selected_places, random.randint(2, 3)) 


def get_evening_places(key, city_name, description = '', radius = 4800):

    gmaps = googlemaps.Client(key)

    # Geocoding the city name to get its coordinates
    geocode_result = gmaps.geocode(city_name)
    if not geocode_result:
        print("City not found.")
        return []
    
    city_location = geocode_result[0]['geometry']['location']
    #hols all the places
    evening_place_list = []
    
    # Search for popular places of each type
    for place_type in evening_place_types:
        places = gmaps.places_nearby(location=city_location, radius=radius, type=place_type)
        for place in places['results']:
            place_details = {
                'name': place['name'],
                'type': place_type,
                'address': place.get('vicinity', 'N/A'),
                'rating': place.get('rating', 'N/A')
            }
            evening_place_list.append(place_details)
    
    # Convert the rating to a float (or 0 if it's "N/A")
    for place in evening_place_list:
        try:
            # Try converting the rating to a float
            place['rating'] = float(place['rating'])
        except ValueError:
            # If conversion fails, set it to a default (e.g., 0) or leave it as "N/A"
            place['rating'] = 0 
            # Replace 0 with your desired default value if needed

    # Shuffle the list of places
    random.shuffle(evening_place_list)


    # Sort the places_list based on rating in descending order
    evening_place_list.sort(key=lambda x: x['rating'], reverse=True)
     
    
    # Select only the first 10 places (or fewer if there are fewer than 10 available)
    selected_places = evening_place_list[:20]

    # Return a random sample more then 2 or equal less then 5 places
    #random.sample(selected_places, random.randint(1, 4)) 

    return random.sample(selected_places, random.randint(2, 3)) 


# city_name = 'Boston Massachusetts'
# popular_places = get_afternoon_places(city_name)
# for place in popular_places:
#     print("Name:", place['name'])
#     print("Address:", place['address'])
#     print("Rating:", place['rating'])
#     print("Type:", place['type'])
#     print()
# city_name = 'South Tampa'
# popular_places = get_evening_places(city_name)
# for place in popular_places:
#     print("Name:", place['name'])
#     print("Address:", place['address'])
#     print("Rating:", place['rating'])
#     print("Type:", place['type'])
#     print()



 #Example usage:

# city_name = '30 Rockefeller Plaza, New York, NY 10112, United States'
# popular_places = get_morning_places(city_name)
# for place in popular_places:
#     print("Name:", place['name'])
#     print("Address:", place['address'])
#     print("Rating:", place['rating'])
#     print("Type:", place['type'])
#     print()

# city_name = '30 Rockefeller Plaza, New York, NY 10112, United States'
# popular_places = get_evening_places(city_name)
# for place in popular_places:
#     print("Name:", place['name'])
#     print("Address:", place['address'])
#     print("Rating:", place['rating'])
#     print("Type:", place['type'])
#     print()

# city_name = '30 Rockefeller Plaza, New York, NY 10112, United States'
# popular_places = get_afternoon_places(city_name)
# for place in popular_places:
#     print("Name:", place['name'])
#     print("Address:", place['address'])
#     print("Rating:", place['rating'])
#     print("Type:", place['type'])
#     print()