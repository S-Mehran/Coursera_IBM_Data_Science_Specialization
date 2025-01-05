import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

filepath='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/automobileEDA.csv'
df = pd.read_csv(filepath)

print(df.head())
print(df.dtypes)

df['peak-rpm'].dtypes

print(df[['bore','stroke','compression-ratio','horsepower']].corr())

# Engine size as potential predictor variable of price
sns.regplot(x="engine-size", y="price", data=df)
plt.ylim(0,)
plt.show()

print(df[["engine-size", "price"]].corr())

sns.regplot(x="highway-mpg", y="price", data=df)
plt.show()

print(df[['highway-mpg', 'price']].corr())

sns.regplot(x="peak-rpm", y="price", data=df)
plt.show()
print(df[['peak-rpm','price']].corr())


print(df[["stroke","price"]].corr())

sns.regplot(x="stroke", y="price", data=df)
plt.show()

sns.boxplot(x="body-style", y="price", data=df)
plt.show()
sns.boxplot(x="engine-location", y="price", data=df)
plt.show()
sns.boxplot(x="drive-wheels", y="price", data=df)
plt.show()

print(df.describe())
print(df.describe(include=['object']))

print(df['drive-wheels'].value_counts())
print(df['drive-wheels'].value_counts().to_frame())

drive_wheels_counts = df['drive-wheels'].value_counts().to_frame()
drive_wheels_counts.rename(columns={'drive-wheels': 'value_counts'}, inplace=True)
print(drive_wheels_counts)

drive_wheels_counts.index.name = 'drive-wheels'
print(drive_wheels_counts)


# engine-location as variable
engine_loc_counts = df['engine-location'].value_counts().to_frame()
engine_loc_counts.rename(columns={'engine-location': 'value_counts'}, inplace=True)
engine_loc_counts.index.name = 'engine-location'
print(engine_loc_counts.head(10))


print(df['drive-wheels'].unique())

df_group_one = df[['drive-wheels','price']]

 #grouping results
df_group_one = df_group_one.groupby(['drive-wheels'],as_index=False).mean()
print(df_group_one)

# grouping results
df_gptest = df[['drive-wheels','body-style','price']]
grouped_test1 = df_gptest.groupby(['drive-wheels','body-style'],as_index=False).mean()
print(grouped_test1)

grouped_pivot = grouped_test1.pivot(index='drive-wheels',columns='body-style')
print(grouped_pivot)

grouped_pivot = grouped_pivot.fillna(0) #fill missing values with 0
print(grouped_pivot)

df_group_two = df[['body-style', 'price']]
df_group_two = df_group_two.groupby(['body-style'],as_index=False).mean()
print(df_group_two)

#use the grouped results
plt.pcolor(grouped_pivot, cmap='RdBu')
plt.colorbar()
plt.show()


fig, ax = plt.subplots()
im = ax.pcolor(grouped_pivot, cmap='RdBu')

#label names
row_labels = grouped_pivot.columns.levels[1]
col_labels = grouped_pivot.index

#move ticks and labels to the center
ax.set_xticks(np.arange(grouped_pivot.shape[1]) + 0.5, minor=False)
ax.set_yticks(np.arange(grouped_pivot.shape[0]) + 0.5, minor=False)

#insert labels
ax.set_xticklabels(row_labels, minor=False)
ax.set_yticklabels(col_labels, minor=False)

#rotate label if too long
plt.xticks(rotation=90)

fig.colorbar(im)
plt.show()


pearson_coef, p_value = stats.pearsonr(df['wheel-base'], df['price'])
print("wheel-price\nThe Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value) 

pearson_coef, p_value = stats.pearsonr(df['horsepower'], df['price'])
print("hp-price\nThe Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value) 

pearson_coef, p_value = stats.pearsonr(df['length'], df['price'])
print("length-price\nThe Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value)  

pearson_coef, p_value = stats.pearsonr(df['width'], df['price'])
print("width-price\nThe Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value ) 

pearson_coef, p_value = stats.pearsonr(df['curb-weight'], df['price'])
print( "weight-price\nThe Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value)  


pearson_coef, p_value = stats.pearsonr(df['engine-size'], df['price'])
print("engine-price\nThe Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value) 

pearson_coef, p_value = stats.pearsonr(df['bore'], df['price'])
print("bore-price\nThe Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =  ", p_value ) 

pearson_coef, p_value = stats.pearsonr(df['city-mpg'], df['price'])
print("citympg-price\nThe Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value)  


pearson_coef, p_value = stats.pearsonr(df['highway-mpg'], df['price'])
print( "HighwayMPG-Price Correlation\nThe Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value ) 