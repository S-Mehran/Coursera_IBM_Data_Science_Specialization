import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

filepath = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-Coursera/laptop_pricing_dataset_mod1.csv"
df = pd.read_csv(filepath)

print(df.info())

print(df.head())
print(df.columns)

df[['Screen_Size_cm']] = np.round(df[['Screen_Size_cm']],2)
print(df.head())

df.replace("?", np.nan, inplace = True)
print(df.head(5))

missing_data = df.isnull()
print(missing_data.head(5))


for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("")    

avg_weight = df["Weight_kg"].astype("float").mean(axis=0)
print("Mean of weight is:", avg_weight)

df["Weight_kg"].replace(np.nan, avg_weight, inplace=True)

#df[['Screen_Size_cm']] = df[['Screen_Size_cm']].astype("float")
frequent_screen = df['Screen_Size_cm'].value_counts().idxmax()
#print(frequent_screen)
print(df.dtypes)
df["Screen_Size_cm"].replace(np.nan, frequent_screen, inplace=True)

df[['Screen_Size_cm']] = df[['Screen_Size_cm']].astype("float")
df[['Weight_kg']] = df[['Weight_kg']].astype("float")

print(df.dtypes)


df["Screen_Size_cm"] = df["Screen_Size_cm"]/2.54
df.rename(columns={"Screen_Size_cm": "Screen_Size_in"}, inplace=True)
print(df.head())

df["Weight_kg"] = df['Weight_kg']*2.205
df.rename(columns={"Weight_kg": "Weight_lb"}, inplace=True)
print(df.head())


df["CPU_frequency"] = df["CPU_frequency"]/df["CPU_frequency"].max()
print(df.head())


bins = np.linspace(min(df["Price"]), max(df["Price"]), 4)
group_names = ["Low", "Medium", "High"]
df["price_binned"] = pd.cut(df["Price"],bins,labels=group_names, include_lowest=True)
print(df.head())


plt.hist(df["Price"], bins = 3)

# set x/y labels and plot title
plt.xlabel("Price")
plt.ylabel("count")
plt.title("Laptop Price bins")
plt.show()

plt.bar(group_names, df["price_binned"].value_counts())

# set x/y labels and plot title
plt.xlabel("Price")
plt.ylabel("count")
plt.title("Laptop Price bins")
plt.show()

dummy_variable = pd.get_dummies(df["Screen"])
dummy_variable.rename(columns={"IPS Panel": "Screen-IPS_Panel", "Full HD": "Screen-Full_HD"})
df = pd.concat([df, dummy_variable], axis = 1)

df.drop("Screen", axis=1, inplace=True)
print(df.head())

df.to_csv('C:\\Users\\M-TT\\Code\\clean_df_Laptops.csv')
