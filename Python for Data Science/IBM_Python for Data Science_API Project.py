import pandas as pd
import numpy as np


URL="https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"


table = pd.read_html(URL)
df = table[3]
print(df.head())

df.columns = range(df.shape[1])

df2 = df[[0,2]]

df_new = df2.iloc[1:11]

df_new.columns = ["Country", "GDP (Million USD)"]
#df_new[0] = "Country"
#df_new[2] = "GDP (Million USD)"

print(df_new)

 
df_new["GDP (Million USD)"] = df_new["GDP (Million USD)"].astype(str).str.replace(',','')
df_new["GDP (Million USD)"] = pd.to_numeric(df_new["GDP (Million USD)"])
df_new["GDP (Billion USD)"] = df_new["GDP (Million USD)"]/1000
df_new["GDP (Billion USD)"] = df_new["GDP (Billion USD)"].round(2)
df_new = df_new.drop(columns=["GDP (Million USD)"])
print(df_new)
df_new.to_csv("Largest Economies.csv")

#df_new["GDP (Millions USD)"] = df_new["GDP (Millions USD)"]/1000

#Array = np.array(df_new)
#print(Array)

#print(type(Array))
#print(Array.ndim)
#print(Array.shape)



#bs = Array[0:10, 1]
#print(bs)
#bs = bs.astype(int)
#print(bs)
#for b in Array[0:10, 1]:
 #   b = b/1000
  #  print(b)





#for b in bs:
 #   b = int(b)
    

#print(bs)

