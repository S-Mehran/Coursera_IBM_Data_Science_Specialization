import pandas as pd
import requests
from bs4 import BeautifulSoup

import warnings
# Ignore all warnings
warnings.filterwarnings("ignore", category=FutureWarning)


url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/amazon_data_webpage.html"

data  = requests.get(url).text
print(data)


soup = BeautifulSoup(data, 'html5lib')

amazon_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])

for row in soup.find("tbody").find_all("tr"):
    col = row.find_all("td")
    print(col)
    date = col[0].text
    Open = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    adj_close = col[5].text
    volume = col[6].text
    

    new_row = pd.DataFrame({"Date": [date], "Open": [Open], "High": [high], "Low": [low], "Close": [close], "Adj Close": [adj_close], "Volume": [volume]})

# Use pd.concat to append the new row
    amazon_data = pd.concat([amazon_data, new_row], ignore_index=True)

print(amazon_data.head())
