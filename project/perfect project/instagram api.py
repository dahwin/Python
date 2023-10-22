import requests

# Replace ACCESS_TOKEN with your valid access token
# and USERNAME with the username of the user whose location you want to retrieve
username = ''
access_token = ''
URL = "https://graph.instagram.com/me?fields=business_discovery.username(USERNAME).business_address&access_token=ACCESS_TOKEN"

response = requests.get(URL)

if response.status_code == 200:
    # Success!
    data = response.json()
    business_address = data['business_discovery']['business_address']
    print(f"Street address: {business_address['street_address']}")
    print(f"Zip code: {business_address['zip_code']}")
    print(f"City: {business_address['city_name']}")
    print(f"Region: {business_address['region_name']}")
    print(f"Country: {business_address['country_code']}")
else:
    # An error occurred
    print(f"Error: {response.status_code}")
