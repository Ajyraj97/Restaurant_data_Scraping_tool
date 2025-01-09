import googlemaps
import pandas as pd

def fetch_restaurants(api_key, location, radius, keyword="restaurant"):
    """
    Fetch restaurant data from Google Maps API, including phone numbers.

    :param api_key: Your Google Maps API key.
    :param location: The center of the search (latitude, longitude).
    :param radius: Search radius in meters.
    :param keyword: Keyword for filtering results (default: "restaurant").
    :return: List of restaurants with details.
    """
    gmaps = googlemaps.Client(key=api_key)

    # Make a Places API Nearby Search request
    response = gmaps.places_nearby(
        location=location,
        radius=radius,
        keyword=keyword
    )

    restaurants = []
    for place in response.get('results', []):
        place_id = place.get("place_id")  # Extract Place ID for detailed information

        # Get place details to fetch phone number
        details = gmaps.place(place_id=place_id)
        result = details.get('result', {})

        restaurant = {
            "name": place.get("name"),
            "rating": place.get("rating", 0),  # Default to 0 if no rating
            "types": ', '.join(place.get("types", [])),  # Join types as a string
            "address": place.get("vicinity"),
            "phone_number": result.get("formatted_phone_number", "Not available")
        }
        restaurants.append(restaurant)

    return restaurants

def save_to_csv(data, filename="restaurants.csv"):
    """
    Save restaurant data to a CSV file sorted by highest rating.

    :param data: List of dictionaries containing restaurant details.
    :param filename: Name of the output CSV file.
    """
    # Convert to DataFrame and sort by rating
    df = pd.DataFrame(data)
    df = df.sort_values(by="rating", ascending=False)

    # Save to CSV
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

# Main Function
if __name__ == "__main__":
    API_KEY = "API-Key_add"  # Replace with your Google Maps API Key
    LOCATION = "30.273090,78.000397"  # Example: New York City (latitude,longitude)
    RADIUS = 15  # Radius in meters (15 meters)

    try:
        # Fetch and save restaurant data
        restaurants = fetch_restaurants(API_KEY, LOCATION, RADIUS)

        if restaurants:
            save_to_csv(restaurants)
        else:
            print("No restaurants found.")

    except Exception as e:
        print("An error occurred:", e)
