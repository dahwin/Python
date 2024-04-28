# import requests

# # Define the URL of your FastAPI application
# url = 'https://18df-104-199-170-14.ngrok-free.app/prompt'

# # Define the data you want to post (a tuple in this case)
# prompt = ' twice dahyun in a beautiful gerden'
# data = {'dahwin': f'{prompt}'}  # Include the 'name' field in the JSON data

# # Send a POST request
# response = requests.post(url, json=data)


# # Print the raw response content for debugging
# print("Raw Response Content:", response.content)

import os

def get_last_created_file(directory="."):
    # Get a list of all files in the directory
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    # Check if there are any files in the directory
    if not files:
        return None

    # Get the full path for each file
    file_paths = [os.path.join(directory, f) for f in files]

    # Get the file with the latest creation time
    last_created_file = max(file_paths, key=os.path.getctime)

    # Get the absolute path
    last_created_file_absolute = os.path.abspath(last_created_file)

    return last_created_file_absolute

# Example usage:
current_directory = "."  # You can change this to the desired directory
generated_image_file = get_last_created_file(current_directory)
print(generated_image_file)

