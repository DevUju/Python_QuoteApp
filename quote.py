from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_quote(category):
    request_url = f"https://api.api-ninjas.com/v1/quotes?category={category}"
    quote_data = requests.get(request_url, headers={'X-Api-Key': {os.getenv("API_KEY")}}).json()
    return quote_data

if __name__ == "__main__":
    print("\n*** Get A New Quote ***\n")
    category = input("\nPlease enter a city: ").lower()

    if not bool(category.strip()):
        category = "happiness"

    quote_data = get_quote(category)
    print("\n")
    print(quote_data)
