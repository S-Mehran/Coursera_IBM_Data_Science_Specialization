import yfinance as yf
import pandas as pd
import requests
import json

amd = yf.Ticker("AMD")
print(amd)
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/amd.json"
output_file = "amd.json"
response = requests.get(url)
if response.status_code == 200:
    with open(output_file, 'wb') as file:
        file.write(response.content)
    print(f"File downloaded successfully and saved as {output_file}")
else:
    print(f"Failed to download file: HTTP status code {response.status_code}")


with open('C:\\Users\\M-TT\\amd.json') as json_file:
    amd_info = json.load(json_file)

    # Print the type of data variable    
    #print("Type:", type(apple_info))
print(amd_info)
print(amd_info["country"])
print(amd_info["sector"])
print(amd_info["phone"])


amd_data = amd.history(period="max")
five_rows = amd_data.head()
print(five_rows)

if not amd_data.empty:
    first_day_volume = amd_data.iloc[0]['Volume']
    first_day_date = amd_data.index[0]
    print(f"Volume traded on the first day ({first_day_date}): {first_day_volume}")
else:
    print("No data fetched for AMD.")
## first_row = amd_data.iloc[0]['Volume']
