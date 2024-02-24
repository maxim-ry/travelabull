

api_key = "AIzaSyAeBKDh9v04QH92KSF_BbDdEOrzxR0n-7Y"

import googlemaps

import googlemaps

# Replace 'YOUR_API_KEY' with your actual API key

gmaps = googlemaps.Client(key=api_key)

def find_nearby_places_by_name(place_name, radius=5000, types=None):
    """
    Find recommended places based on the name of the place.

    Parameters:
        - place_name: Name of the place to search for
        - radius: Search radius in meters (default is 5000 meters)
        - types: List of place types to filter the results (e.g., ['restaurant', 'museum'])

    Returns:
        - List of recommended places
    """
    places_result = gmaps.places(query=place_name, radius=radius, type=types)

    recommended_places = []
    for place in places_result['results']:
        place_name = place['name']
        place_address = place.get('formatted_address', 'Address not available')
        place_rating = place.get('rating', 'Rating not available')

        recommended_places.append({
            'Name': place_name,
            'Address': place_address,
            'Rating': place_rating
        })

    return recommended_places

if __name__ == "__main__":
    # Example place name: 'Golden Gate Park'
    place_name = input("Enter the name of the place: ")

    # Example types: ['restaurant', 'museum']
    types = ['restaurant', 'museum']

    recommended_places = find_nearby_places_by_name(place_name, types=types)

    print(f"Recommended Places for '{place_name}':")
    for idx, place in enumerate(recommended_places, 1):
        print(f"{idx}. {place['Name']} - Address: {place['Address']} - Rating: {place['Rating']}")
