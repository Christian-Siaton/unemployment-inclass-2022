
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

data = parsed_response["data"]
latest = data[0]

print('----------------------')
print("The most recent unemployment rate is:", str(latest['value'])+'%.')
print('The corresponding date is', str(latest['date']) +'.')

# Challenge B
# 
# What is the average unemployment rate for all months during this calendar year?
# ... How many months does this cover?

unemployment_rates = []

for x in data:
    unemployment_rates.append(x['value'])

sum = 0
for x in unemployment_rates:
    sum = float(x) + sum

# Rounding code from https://stackoverflow.com/questions/20457038/how-to-round-to-2-decimals-with-python
average_unemployment_rate = round(sum / len(unemployment_rates), 5)

print ('---------------------')
print(f'The average unemployment rate is {average_unemployment_rate}%.')
print('This covers', len(unemployment_rates), 'months.')


# type 'exit()' to exit from the Python console back to Command Line
breakpoint()