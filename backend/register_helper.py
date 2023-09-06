import pandas as pd
from geopy.geocoders import Nominatim
from openpyxl import load_workbook

# Function to append data to an Excel file


def append_data(form_data):
    # Get the form data
    name = form_data.get('name')
    age = form_data.get('age')
    email = form_data.get('email')
    number = form_data.get('number')
    location = form_data.get('location')

    # Initialize the geolocator with a user agent
    geolocator = Nominatim(user_agent='my_geocoder')

    # Geocode the location to get latitude and longitude
    location_data = geolocator.geocode(location)
    latitude = longitude = "Not Found"
    if location_data:
        latitude = location_data.latitude
        longitude = location_data.longitude

    # Load the workbook
    wb = load_workbook('./data/helpers_data.xlsx')
    sheet = wb.active

    # Create a row with the form data
    row = (name, age, email, number, location, latitude, longitude)

    # Append the row to the sheet
    sheet.append(row)

    # Save the workbook
    wb.save('./data/helpers_data.xlsx')

    # Close the workbook
    wb.close()
