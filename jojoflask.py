from flask import Flask, jsonify, render_template, redirect, url_for
import requests
import random


app = Flask(__name__)

# Base URL for the JoJo API
base_url = "https://stand-by-me.herokuapp.com/api/v1/"

def get_all_characters():
    response = requests.get(f"{base_url}characters")
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching characters: {response.status_code}")
        return None
    
def get_all_stands():
    response = requests.get(f"{base_url}stands")
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching stands: {response.status_code}")
        return None


# Function to pick a random entry
def pick_random(entry_list):
    return random.choice(entry_list) if entry_list else None


# Fetch stands and pick one randomly (if you implement this later)
stands = get_all_stands()
if stands:
    random_stand = random.choice(stands)
    print("Random Stand:", random_stand)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/random_character')
def random_character():
    characters = get_all_characters()
    character = pick_random(characters)  # Fixed the typo here
    if character:
        return render_template('display.html', entry=character, entry_type="Character")
    else:
        return jsonify({"error": "No character found"}), 404
    
@app.route('/random_stand')
def random_stand():
    stands = get_all_stands()
    stand = pick_random(stands)  # Pass the list 'stands' to pick_random, not 'stand'
    if stand:
        return render_template('display.html', entry=stand, entry_type="Stand")
    else:
        return jsonify({"error": "No stand found"}), 404


    
if __name__ == '__main__':
    app.run(debug=True)
    
