import yfinance as yf
import pandas as pd
import requests

apple = yf.Ticker("AAPL")
print(apple)
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/apple.json"
output_file = "apple.json"

response = requests.get(url)
if response.status_code == 200:
    with open(output_file, 'wb') as file:
        file.write(response.content)
    print(f"File downloaded successfully and saved as {output_file}")
else:
    print(f"Failed to download file: HTTP status code {response.status_code}")


import json
with open('apple.json') as json_file:
    apple_info = json.load(json_file)
    # Print the type of data variable    
    #print("Type:", type(apple_info))
print(apple_info)

apple_info['country']

apple_share_price_data = apple.history(period="max")

print(apple_share_price_data.head())

apple_share_price_data.reset_index(inplace=True)

apple_share_price_data.plot(x="Date", y="Open")

apple.dividends

apple.dividends.plot()

