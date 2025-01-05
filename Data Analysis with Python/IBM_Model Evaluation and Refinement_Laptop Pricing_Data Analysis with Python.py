from tqdm import tqdm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.preprocessing import PolynomialFeatures

filepath = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-Coursera/laptop_pricing_dataset_mod2.csv'
df = pd.read_csv(filepath)

df=df._get_numeric_data()
print(df.head())

df.drop(['Unnamed: 0', 'Unnamed: 0.1'], axis=1, inplace=True)
print(df.head())

x_data = df.drop('Price', axis=1)
y_data = df['Price']

x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.1,random_state=1)

lre = LinearRegression()
lre.fit(x_train[['CPU_frequency']], y_train)
print("The result for Train Test Split are:\n")
print(lre.score(x_train[['CPU_frequency']], y_train))
print(lre.score(x_test[['CPU_frequency']], y_test))

scores = cross_val_score(lre, x_data[['CPU_frequency']], y_data, cv=4)
print("The Results for Cross-Validation are:\n")
mean_Rsq = np.mean(scores)
std_Rsq = np.std(scores)
print("Mean:", mean_Rsq)
print("Standard Deviation:", std_Rsq)


x_train1, x_test1, y_train1, y_test1 = train_test_split(x_data, y_data, test_size=0.5,random_state=0)

Rsqu_test = [] 
order = [1,2,3,4,5]
for n in order:
    pr=PolynomialFeatures(degree=n)
    x_train_pr = pr.fit_transform(x_train[['CPU_frequency']])
    x_test_pr = pr.fit_transform(x_test[['CPU_frequency']])
    lre.fit(x_train_pr, y_train)
    Rsqu_test.append(lre.score(x_test_pr, y_test))
    print(Rsqu_test)

plt.plot(order, Rsqu_test)
plt.xlabel("Order of Polynomial")
plt.ylabel("R^2")
plt.title("R^2 Using test data")
plt.show()

x_train_mult = x_train[['CPU_frequency', 'RAM_GB', 'Storage_GB_SSD', 'CPU_core','OS','GPU', 'Category']]

x_test_mult = x_test[['CPU_frequency', 'RAM_GB', 'Storage_GB_SSD', 'CPU_core','OS','GPU', 'Category']]

pr1 = PolynomialFeatures(degree=2)
x_train_pr1 = pr1.fit_transform(x_train_mult)
x_test_pr1 = pr1.fit_transform(x_test_mult)
#lre.fit(x_train_pr1, y_train1)
Rsqu_test = []
Rsqu_train = []
dummy1 = []

Alpha = np.arange(0.001, 1.0, 0.001)
pbar = tqdm(Alpha)

for alpha in pbar:
    RidgeModel = Ridge(alpha=alpha)
    RidgeModel.fit(x_train_pr1, y_train)
    train_score = RidgeModel.score(x_train_pr1, y_train)
    test_score = RidgeModel.score(x_test_pr1, y_test)

    pbar.set_postfix({"Test Score": test_score, "Train Score": train_score})
    
    Rsqu_test.append(test_score)
    Rsqu_train.append(train_score)

print("The results fpr Ridge Regression are:\n")
print(Rsqu_test)
print(Rsqu_train)
plt.figure(figsize=(6, 6))

plt.plot(Alpha,Rsqu_test, label='validation data  ')
plt.plot(Alpha,Rsqu_train, 'r', label='training Data ')
plt.xlabel('alpha')
plt.ylabel('R^2')
#plt.ylim(0, 1)
plt.legend()
plt.show()

#GRID SEARCH

x_data_mult = x_data[['CPU_frequency', 'RAM_GB', 'Storage_GB_SSD', 'CPU_core','OS','GPU', 'Category']]
parameters = [{'alpha': [0.0001, 0.001, 0.01, 0.1, 1, 10]}]
RR= Ridge()
Grid1 = GridSearchCV(RR, parameters, cv=4)

Grid1.fit(x_data_mult, y_data)
print(Grid1.best_estimator_)
