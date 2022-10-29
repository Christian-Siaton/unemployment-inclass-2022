
import requests
import os
import json
from pprint import pprint
from dotenv import load_dotenv
from statistics import mean

load_dotenv()

API_KEY = os.getenv("API_KEY")

request_url = f"https://www.alphavantage.co/query?function=UNEMPLOYMENT&apikey={API_KEY}"

response = requests.get(request_url)

parsed_response = json.loads(response.text)
print(type(parsed_response))
pprint(parsed_response)


# Challenge A
#
# What is the most recent unemployment rate? And the corresponding date? 
# Display the unemployment rate using a percent sign.

latest = parsed_response["data"][0]

print('----------------------')
print("The most recent unemployment rate is:", str(latest['value'])+'%.')
print('The corresponding date is', str(latest['date']) +'.')




# type 'exit()' to exit from the Python console back to Command Line
breakpoint()