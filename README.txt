Features
    1. Fetch Restaurants:
        Retrieves a list of nearby restaurants based on a location and radius.
        Includes details like:
            Name
            Rating
            Address
            Types (e.g., cuisine types)
            Phone number (if available)
    
    2. Save to CSV:
        Exports the restaurant data to a CSV file.
        Sorts the data by rating in descending order for easy interpretation.

Prerequisites
    Python 3.x
    Required Python libraries:
        googlemaps
        pandas
    Install the dependencies using pip:
        pip install googlemaps pandas
    A valid Google Maps API Key with the following enabled:
        Places API
        Geocoding API (optional for extended features)

File Structure
    Main Script: Contains the functions to fetch and save restaurant data.
    Output: Generates a CSV file named restaurants.csv by default.

Functions
    1. fetch_restaurants(api_key, location, radius, keyword="restaurant")
        Purpose: Fetch nearby restaurants using Google Maps API.
        Parameters:
            api_key: Your Google Maps API Key.
            location: A string containing the latitude and longitude (e.g., "30.316496,78.032188").
            radius: Search radius in meters.
            keyword: A string for filtering results. Default is "restaurant".
        Returns: A list of dictionaries containing restaurant details.
        Details:
            Sends a places_nearby request to the API.
            Uses the place_id from the results to fetch additional details like the phone number.
    
    2. save_to_csv(data, filename="restaurants.csv")
        Purpose: Save the fetched restaurant data into a CSV file.
        Parameters:
            data: List of dictionaries containing restaurant details.
            filename: Name of the output CSV file. Default is "restaurants.csv".
        Process:
            Converts the list of dictionaries to a pandas DataFrame.
            Sorts the data by the rating column in descending order.
            Exports the DataFrame to a CSV file.

How to Use
    1. Replace API Key
        Edit the API_KEY variable with your valid Google Maps API Key:
            API_KEY = "YOUR-API-KEY-HERE"
    
    2. Define Location and Radius
        Set your desired location (latitude, longitude) and search radius in meters:
            LOCATION = "30.316496,78.032188"  # Replace with your location
            RADIUS = 500  # Replace with your desired search radius
    
    3. Run the Script
        Execute the script:
            python script_name.py
    
    4. Output
        The script generates a CSV file (restaurants.csv) in the same directory containing restaurant details.

Example Output
    Name            Rating  Types               Address         Phone Number
    Restaurant A    4.5     restaurant, cafe    123 Main St     +1 123-456-7890
    Restaurant B    4.2     restaurant, diner   456 Side St     Not available

Error Handling
    The script includes basic error handling to catch API errors or issues with the response. 
    If an error occurs, it prints a descriptive error message.

Improvements & Customizations
    - Add more filtering options like price level or specific cuisines.
    - Extend the script to fetch additional details like opening hours or reviews.
    - Improve error handling for more granular debugging.
    - Support multiple file formats (e.g., JSON, Excel).

License
    This script is provided "as is" without warranty of any kind. 
    Ensure compliance with the Google Maps API Terms of Service when using this code.
