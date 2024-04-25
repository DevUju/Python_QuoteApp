from dotenv import load_dotenv
import requests
import os

load_dotenv()

def get_quote(category):
    request_url = f"https://api.api-ninjas.com/v1/quotes?category={category}"
    get_key = os.getenv("API_KEY")
    quote_data = requests.get(request_url, headers={'X-Api-Key': get_key}).json()
    return quote_data

if __name__ == "__main__":
    print("\n*** Get A New Quote ***\n")
    category = input("\nPlease enter a keyword: ").lower()

    quote_data = get_quote(category)
    print("\n")
    print(quote_data)
    
