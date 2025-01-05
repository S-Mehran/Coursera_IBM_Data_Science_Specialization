import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots

import warnings
# Ignore all warnings
warnings.filterwarnings("ignore", category=FutureWarning)

def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    stock_data_specific = stock_data[stock_data.Date <= '2021--06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific.Date, infer_datetime_format=True), y=stock_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date, infer_datetime_format=True), y=revenue_data_specific.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title=stock,
    xaxis_rangeslider_visible=True)
    fig.show()

tesla = yf.Ticker("TSLA")
print(tesla)

tesla_data = tesla.history(period="max")
tesla_data.reset_index(inplace=True)
print(tesla_data.head())

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"

data  = requests.get(url).text
##print(data)


soup = BeautifulSoup(data, 'html.parser')

tesla_revenue_table = soup.find_all("tbody")[1]


dates = []
revenues = []

for row in tesla_revenue_table.find_all('tr')[1:]:  # Skip the header row
    cols = row.find_all('td')
    date = cols[0].text.strip()
    revenue = cols[1].text.strip()
    dates.append(date)
    revenues.append(revenue)

tesla_revenue = pd.DataFrame({
    "Date": dates,
    "Revenue": revenues
})
##tesla_revenue["Revenue"] = tesla_revenue['Revenue'].str.replace(',|\$',"")
tesla_revenue['Revenue'] = tesla_revenue['Revenue'].str.replace(',', '')
tesla_revenue['Revenue'] = tesla_revenue['Revenue'].str.replace('$', '')
tesla_revenue.dropna(inplace=True)

tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]

tesla_revenue['Revenue'] = pd.to_numeric(tesla_revenue['Revenue'], errors='coerce')

# Ensure the 'Date' column in tesla_revenue is of datetime type
tesla_revenue['Date'] = pd.to_datetime(tesla_revenue['Date'])

# Sort the revenue data by Date
tesla_revenue = tesla_revenue.sort_values(by='Date')

print(tesla_revenue.tail())


gme = yf.Ticker("GME")


gme_data = gme.history(period="max")
gme_data.reset_index(inplace=True)
print(gme_data.head())


url2 = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"

data2  = requests.get(url2).text
##print(data)


soup2 = BeautifulSoup(data2, 'html.parser')

gme_revenue_table = soup2.find_all("tbody")[1]


dates = []
revenues = []

for row in gme_revenue_table.find_all('tr')[1:]:  # Skip the header row
    cols = row.find_all('td')
    date = cols[0].text.strip()
    revenue = cols[1].text.strip()
    dates.append(date)
    revenues.append(revenue)

gme_revenue = pd.DataFrame({
    "Date": dates,
    "Revenue": revenues
})
#gme_revenue["Revenue"] = gme_revenue['Revenue'].str.replace(',|\$',"")
gme_revenue['Revenue'] = gme_revenue['Revenue'].str.replace(',', '')
gme_revenue['Revenue'] = gme_revenue['Revenue'].str.replace('$', '')

gme_revenue.dropna(inplace=True)

gme_revenue = gme_revenue[gme_revenue['Revenue'] != ""]



gme_revenue['Revenue'] = pd.to_numeric(gme_revenue['Revenue'], errors='coerce')

# Ensure the 'Date' column in tesla_revenue is of datetime type
gme_revenue['Date'] = pd.to_datetime(gme_revenue['Date'])

# Sort the revenue data by Date
gme_revenue = gme_revenue.sort_values(by='Date')

print(gme_revenue.tail())


make_graph(tesla_data, tesla_revenue, 'Tesla')
make_graph(gme_data, gme_revenue, 'GameStop')
