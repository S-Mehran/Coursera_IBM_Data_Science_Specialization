from tqdm import tqdm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score

filepath = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-Coursera/medical_insurance_dataset.csv'
df = pd.read_csv(filepath, header=None)

print(df.head(10))

headers = ["age", "gender", "bmi", "no_of_children", "smoker", "region", "charges"]
df.columns = headers
print(df.head())

df = df.replace('?', np.NaN)
print(df.head(10))

print(df.info())

print(df.dtypes)
#print(df.dtypes)
df["age"] = pd.to_numeric(df["age"])
mean_age = df['age'].mean()
df["age"] = df["age"].replace(np.nan, mean_age)
#df['age'].fillna(mean_age, inplace=True)
df["age"] = df["age"].astype("int")
df["smoker"] = pd.to_numeric(df["smoker"])
smoker_repeated = df["smoker"].value_counts().idxmax()
df["smoker"].replace(np.nan, smoker_repeated, inplace=True)
df["smoker"] = df["smoker"].astype("int")
print(df.dtypes)
mean_bmi = df['bmi'].mean()
print(mean_bmi)
mean_charges = df['charges'].mean()
print(mean_charges)
gender_repeated = df["gender"].value_counts().idxmax()
print(gender_repeated)
region_repeated = df["region"].value_counts().idxmax()
print(region_repeated)
child_repeated = df["no_of_children"].value_counts().idxmax()
print(child_repeated)
df["bmi"].replace(np.nan, mean_bmi, inplace=True)
df["charges"].replace(np.nan, mean_charges, inplace=True)
df["gender"].replace(np.nan, gender_repeated, inplace=True)
df["region"].replace(np.nan, region_repeated, inplace=True)
df["no_of_children"].replace(np.nan, child_repeated, inplace=True)

print(df.head(10))

print(df.info())
df["charges"] = df["charges"].round(2)
print(df.head())


sns.regplot(x="bmi", y="charges", data=df, line_kws={"color": "red"})
sns.boxplot(x="smoker", y="charges", data=df)
plt.show()

print(df[['age', 'gender', 'bmi', 'no_of_children', 'smoker', 'region', 'charges']].corr())

lre = LinearRegression()
X = df[['smoker']]
Y = df['charges']
lre.fit(X,Y)

Yhat = lre.predict(X)
rsqu = lre.score(X,Y)
print(rsqu)

x_all = df.drop('charges', axis=1)
lre.fit(x_all, Y)
Yhat2 = lre.predict(x_all)
print(Yhat[0:4])
print(Yhat2[0:4])

rsqu2 = lre.score(x_all, Y)
print(rsqu2)

Input=[('scale',StandardScaler()), ('polynomial', PolynomialFeatures(include_bias=False)), ('model',LinearRegression())]
pipe=Pipeline(Input)
print("Pipe", pipe)

x_all = x_all.astype(float)
pipe.fit(x_all, Y)

ypipe = pipe.predict(x_all)
print(Yhat[0:4])
print(Yhat2[0:4])
print(ypipe[0:4])

rsqu3 = r2_score(Y, ypipe)
print(rsqu3)


x_train, x_test, y_train, y_test = train_test_split(x_all, Y, test_size=0.2,random_state=1)

RidgeModel = Ridge(alpha=0.1)
RidgeModel.fit(x_train, y_train)
Yhat3 = RidgeModel.predict(x_test)
rsqu4 = r2_score(y_test, Yhat3)
print(rsqu4)

pr = PolynomialFeatures(degree=2)
x_train_pr = pr.fit_transform(x_train)
x_test_pr = pr.fit_transform(x_test)
lre.fit(x_train_pr, y_train)

rsqu5 = lre.score(x_test_pr, y_test)
print(rsqu5)

RidgeModel.fit(x_train_pr, y_train)
Yhat4 = RidgeModel.predict(x_test_pr)
rsqu6 = r2_score(y_test, Yhat4)
print(rsqu6)
