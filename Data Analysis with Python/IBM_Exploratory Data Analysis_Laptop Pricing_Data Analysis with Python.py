import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats


filepath="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-Coursera/laptop_pricing_dataset_mod2.csv"
df = pd.read_csv(filepath)

print(df.head())

sns.regplot(x = "CPU_frequency", y="Price", data=df)

plt.show()

sns.regplot(x = "Screen_Size_inch", y="Price", data=df)
plt.show()

sns.regplot(x = "Weight_pounds", y="Price", data=df)
plt.show()

print(df[['CPU_frequency', 'Price']].corr())
print(df[['Screen_Size_inch', 'Price']].corr())
print(df[['Weight_pounds', 'Price']].corr())


sns.boxplot(x="Category", y="Price", data=df)
plt.show()

sns.boxplot(x="GPU", y="Price", data=df)
plt.show()

sns.boxplot(x="CPU_core", y="Price", data=df)
plt.show()

sns.boxplot(x="RAM_GB", y="Price", data=df)
plt.show()

sns.boxplot(x="Storage_GB_SSD", y="Price", data=df)
plt.show()

print(df.describe())
print(df.describe(include=['object']))


df_group_one = df[['GPU', 'CPU_core', 'Price']]
df_group_one = df_group_one.groupby(['GPU', 'CPU_core'], as_index=False).mean()
print(df_group_one)

grouped_pivot = df_group_one.pivot(index='GPU', columns='CPU_core')
print(grouped_pivot)

grouped_pivot = grouped_pivot.fillna(0)
print(grouped_pivot)

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

lst = ['Category', 'GPU', 'OS', 'CPU_core', 'Screen_Size_inch', 'Weight_pounds', 'CPU_frequency', 'Storage_GB_SSD']
for param in lst:
    pearson_coef, p_value = stats.pearsonr(df[param], df['Price'])
    print("The Pearson Correlation Coefficient for", param, "is:", pearson_coef, "with a P value of", p_value)