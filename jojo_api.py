import requests
import random

# Base URL for the JoJo API
base_url = "https://stand-by-me.herokuapp.com/api/v1/"

# Function to get all characters
def get_all_characters():
    response = requests.get(f"{base_url}characters")
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching characters: {response.status_code}")
        return None

# Function to get all stands
def get_all_stands():
    response = requests.get(f"{base_url}stands")
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching stands: {response.status_code}")
        return None

# Fetch characters and pick one randomly
characters = get_all_characters()
if characters:
    random_character = random.choice(characters)
    print("Random Character:", random_character)

# Fetch stands and pick one randomly (if you implement this later)
# stands = get_all_stands()
# if stands:
#     random_stand = random.choice(stands)
#     print("Random Stand:", random_stand