import os 
from dotenv import load_dotenv
import requests

load_dotenv()

websiteURL = os.getenv('websiteURL')

request = requests.get(websiteURL)

print(request.status_code)