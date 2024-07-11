import requests

# Define the API endpoints
signup_url = "http://127.0.0.1:8000/signup"
login_url = "http://127.0.0.1:8000/login"

# Sample signup for Kim Dahyun
signup_data = {
    "name": "Kim Dahyun",
    "date_of_birth": "1998-05-28",
    "gender": "Female",
    "country": "South Korea",
    "email": "kim.dahwinn@example.com",
    "password": "securepassword"
}

signup_response = requests.post(signup_url, json=signup_data)
print(signup_response.json())

# Sample login for Kim Dahyun
login_data = {
    "email": "kim.dahyun@example.com",
    "password": "securepassword"
}

login_response = requests.post(login_url, json=login_data)
print(login_response.json())
