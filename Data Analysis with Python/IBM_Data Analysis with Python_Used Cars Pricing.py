import pandas as pd
import numpy as np

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"
df = pd.read_csv(url, header = None)
print(df.head())

print(df.tail(10))


# create headers list
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
print("headers\n", headers)

df.columns = headers
print(df.columns)

print(df.head())


#Replace ? values with NaN and Drop missing values

df1=df.replace('?',np.NaN)
df=df1.dropna(subset=["price"], axis=0)
print(df.head(20))

print(df.columns)

df.to_csv("C:\\Users\\M-TT\\Code\\automobile.csv", index=False)

print("Data Types\n", df.dtypes)
print("Statistical Summary\n", df.describe())
print("Statistical Summary of All\n", df.describe(include="all"))

print(df[['symboling', 'normalized-losses', 'make']])
print(df[['symboling', 'normalized-losses', 'make']].describe())


print("Information\n", df.info())
