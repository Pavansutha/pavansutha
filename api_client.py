# dev_assessment/api_client.py

import requests

def fetch_and_display_users(num_users):
    """
    Fetches users from JSONPlaceholder and displays name, email, and city.
    Handles network issues, non-200 responses, and missing keys.
    
    Args:
        num_users (int): Number of users to fetch.
    
    Returns:
        None
    """
    url = "https://jsonplaceholder.typicode.com/users"
    
    try:
        response = requests.get(url, timeout=10)  # timeout in seconds
        response.raise_for_status()  # Raise HTTPError for non-200 responses
    except requests.exceptions.RequestException as e:
        print(f"Network or HTTP error occurred: {e}")
        return None

    try:
        users = response.json()
        if not isinstance(users, list):
            raise ValueError("Unexpected JSON structure: Expected a list of users.")
        
        for i, user in enumerate(users[:num_users]):
            # Safely get name, email, and city
            name = user.get("name", "N/A")
            email = user.get("email", "N/A")
            city = user.get("address", {}).get("city", "N/A")
            
            print(f"User {i + 1}: Name: {name}, Email: {email}, City: {city}")
    except (ValueError, KeyError, TypeError) as e:
        print(f"Error processing JSON data: {e}")
        return None

if __name__ == "__main__":
    print("Fetching 3 users:")
    fetch_and_display_users(3)

    print("\nFetching 15 users (out-of-bounds test):")
    fetch_and_display_users(15)
