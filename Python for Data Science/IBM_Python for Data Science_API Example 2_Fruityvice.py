import requests
import json
import pandas as pd

data = requests.get("https://fruityvice.com/api/fruit/all")

results = json.loads(data.text)

df2 = pd.DataFrame(results)
#print(df2)
df2 = pd.json_normalize(results)

print(df2)

cherry = df2.loc[df2["name"] == 'Cherry']
cherry = (cherry.iloc[0]['family']) , (cherry.iloc[0]['genus'])
print(cherry)

banana = df2.loc[df2["name"] == 'Banana']
banana = (banana.iloc[0]['nutritions.calories']) 
print(banana)
