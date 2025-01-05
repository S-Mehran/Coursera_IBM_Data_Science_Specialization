import pandas as pd
import numpy as np
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-Coursera/laptop_pricing_dataset_base.csv"

df = pd.read_csv(url, header = None)

print(df.head())

headers = ["Manufacturer", "Category", "Screen", "GPU", "OS", "CPU_core", "Screen_Size_inch", "CPU_frequency", "RAM_GB", "Storage_GB_SSD", "Weight_kg", "Price"]

df.columns = headers
print(df.head())

df = df.replace('?', np.NaN)

print("Data Type\n", df.dtypes)
print("Statistical Summay:\n", df.describe())
print("Statistical Summary of All\n", df.describe(include='all'))
print("Summary Information\n", df.info())
