import requests

# URL for the JoJo API (getting a list of characters)
url = "https://jojos-api.vercel.app/"

# Make a request to the API
response = requests.get(url)

# Check the status code of the response
print(f"Status Code: {response.status_code}")

# Print the raw response content
print(f"Response Text: {response.text}")

# Only try to parse the response if it was successful (status code 200)
if response.status_code == 200:
    try:
        data = response.json()  # Parse the JSON data
        print(data)  # Print the data
    except requests.exceptions.JSONDecodeError:
        print("Error: The response is not valid JSON.")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")