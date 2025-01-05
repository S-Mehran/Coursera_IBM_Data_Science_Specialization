import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler,PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error, r2_score

filepath='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/FinalModule_Coursera/data/kc_house_data_NaN.csv'
df = pd.read_csv(filepath)
print(df.head())

print(df.dtypes)
print(df.describe())

df.drop(['id', 'Unnamed: 0'], axis=1, inplace=True)
print(df.head())
print(df.describe())

print("number of NaN values for the column bedrooms :", df['bedrooms'].isnull().sum())
print("number of NaN values for the column bathrooms :", df['bathrooms'].isnull().sum())

mean=df['bedrooms'].mean()
df['bedrooms'].replace(np.nan,mean, inplace=True)

mean=df['bathrooms'].mean()
df['bathrooms'].replace(np.nan,mean, inplace=True)

print("number of NaN values for the column bedrooms :", df['bedrooms'].isnull().sum())
print("number of NaN values for the column bathrooms :", df['bathrooms'].isnull().sum())


floor_counts = df['floors'].value_counts()
floor_counts.to_frame()
print(df.head())

sns.boxplot(x="waterfront", y="price", data=df)
plt.show()

sns.regplot(x="sqft_above", y="price", data=df)
plt.show()

df=df._get_numeric_data()
print(df.corr()['price'].sort_values())


X1 = df[['long']]
Y = df['price']
lm = LinearRegression()
lm.fit(X1,Y)
yhat1 = lm.predict(X1)
print(lm.score(X1, Y))
X2 = df[['sqft_living']]
lm.fit(X2, Y)
yhat2 = lm.predict(X2)
print(lm.score(X2, Y))

features = df[["floors", "waterfront","lat" ,"bedrooms" ,"sqft_basement" ,"view" ,"bathrooms","sqft_living15","sqft_above","grade","sqft_living"]]     
lm.fit(features, Y)
yhat3 = lm.predict(features)
print(lm.score(features, Y))

Input=[('scale',StandardScaler()),('polynomial', PolynomialFeatures(include_bias=False)),('model',LinearRegression())]

pipe=Pipeline(Input)
print("Pipe", pipe)

Z = features.astype(float)
pipe.fit(Z,Y)

ypipe=pipe.predict(Z)
print(r2_score(Y, ypipe))
print(yhat1[0:4])
print(yhat2[0:4])
print(yhat3[0:4])
print(ypipe[0:4])


features =["floors", "waterfront","lat" ,"bedrooms" ,"sqft_basement" ,"view" ,"bathrooms","sqft_living15","sqft_above","grade","sqft_living"]    
X = df[features]
Y = df['price']

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.15, random_state=1)


print("number of test samples:", x_test.shape[0])
print("number of training samples:",x_train.shape[0])


RidgeModel = Ridge(alpha=0.1)
RidgeModel.fit(x_train, y_train)
yhat4 = RidgeModel.predict(x_test)
rsqu4 = r2_score(y_test, yhat4)
print(rsqu4)


pr = PolynomialFeatures(degree=2)
x_train_pr = pr.fit_transform(x_train)
x_test_pr = pr.fit_transform(x_test)

RidgeModel.fit(x_train_pr, y_train)
yhat5 = RidgeModel.predict(x_test_pr)
rsqu6 = r2_score(y_test, yhat5)
print(rsqu6)
