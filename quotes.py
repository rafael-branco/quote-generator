import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

def get_quote():
    api_key = os.getenv('API_NINJAS_KEY')
    api_url = 'https://api.api-ninjas.com/v1/quotes'
    
    response = requests.get(api_url, headers={'X-Api-Key': api_key})

    if response.status_code == requests.codes.ok:
        return json.loads(response.text)
    else:
        return {"Error", response.status_code, response.text}
