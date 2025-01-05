import requests
import pandas as pd
import json


URL = "https://official-joke-api.appspot.com/jokes/ten"

r = requests.get(URL)

results = json.loads(r.text)

df = pd.DataFrame(results)

df = df.drop("type", axis='columns')
df = df.drop("id", axis='columns')

print(df)
