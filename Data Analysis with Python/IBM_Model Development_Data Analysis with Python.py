import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import seaborn as sns
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

#Link for Lab = https://labs.cognitiveclass.ai/v2/tools/jupyterlite?ulid=ulid-487923d257ad97994e4c705f44d0ee7ddd8cd905

filepath = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/automobileEDA.csv"
df = pd.read_csv(filepath)

lm = LinearRegression()
print(lm)

X = df[['highway-mpg']]
Y = df['price']

lm.fit(X,Y)

Yhat=lm.predict(X)
print(Yhat[0:5])

print(lm.coef_)

lm1 = LinearRegression()

X1 = df[['engine-size']]

lm1.fit(X1, Y)
Yhat1 = lm1.predict(X1)
print(Yhat1[0:5])
print(lm1.coef_)
print(lm1.intercept_)

# using X and Y, OUR LINEAR REGRESSION MODEL BECOMES  
#Yhat=-7963.34 + 166.86*X
#Price=-7963.34 + 166.86*df['engine-size']


Z = df[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']]
lm.fit(Z, df['price'])
print("MLR\n", lm.intercept_)
print(lm.coef_)

lm2 = LinearRegression()
Z1 = df[['highway-mpg', 'normalized-losses']]
lm2.fit(Z1, Y)
print(lm2.coef_)

width = 12
height = 10
plt.figure(figsize=(width, height))
sns.regplot(x="highway-mpg", y="price", data=df)
plt.ylim(0,)
#plt.show()

plt.figure(figsize=(width, height))
sns.regplot(x="peak-rpm", y="price", data=df)
plt.ylim(0,)
#plt.show()

print(df[['highway-mpg', 'peak-rpm', 'price']].corr())

#print(df[['peak-rpm', 'price']].corr())


#DISTRIBUTION PLOT FOR MULTIPLE LINEAR REGRESSION

Y_hat = lm.predict(Z)

plt.figure(figsize=(width, height))


ax1 = sns.distplot(df['price'], hist=False, color="r", label="Actual Value")
sns.distplot(Y_hat, hist=False, color="b", label="Fitted Values" , ax=ax1)


plt.title('Actual vs Fitted Values for Price')
plt.xlabel('Price (in dollars)')
plt.ylabel('Proportion of Cars')

plt.show()
plt.close()


def PlotPolly(model, independent_variable, dependent_variabble, Name):
    x_new = np.linspace(15, 55, 100)
    y_new = model(x_new)

    plt.plot(independent_variable, dependent_variabble, '.', x_new, y_new, '-')
    plt.title('Polynomial Fit with Matplotlib for Price ~ Length')
    ax = plt.gca()
    ax.set_facecolor((0.898, 0.898, 0.898))
    fig = plt.gcf()
    plt.xlabel(Name)
    plt.ylabel('Price of Cars')

    plt.show()
    plt.close()

x = df['highway-mpg']
y = df['price']

# Here we use a polynomial of the 3rd order (cubic) 
f = np.polyfit(x, y, 3)
p = np.poly1d(f)
print(p)
PlotPolly(p, x, y, 'highway-mpg')
np.polyfit(x, y, 3)


# Here we use a polynomial of the 11th order  
f1 = np.polyfit(x, y, 11)
p1 = np.poly1d(f1)
print(p1)
PlotPolly(p1, x, y, 'highway-mpg')
np.polyfit(x, y, 11)

#POLYNOMIAL TRANSFORM
#We create a <b>PolynomialFeatures</b> object of degree 2: 
pr=PolynomialFeatures(degree=2)
print(pr)
Z_pr=pr.fit_transform(Z)
print(Z.shape)
print(Z_pr.shape)
#In the original data, there are 201 samples and 4 features.
#After the transformation, there are 201 samples and 15 features.


#PIPELINE
Input=[('scale',StandardScaler()), ('polynomial', PolynomialFeatures(include_bias=False)), ('model',LinearRegression())]
pipe=Pipeline(Input)
print("Pipe", pipe)

Z = Z.astype(float)
pipe.fit(Z,y)

ypipe=pipe.predict(Z)
print(ypipe[0:4])



Input=[('scale',StandardScaler()),('model',LinearRegression())]

pipe=Pipeline(Input)

pipe.fit(Z,y)

ypipe=pipe.predict(Z)
print(ypipe[0:10])


#Rsquared and MeansquaredError

#R_SQUARED
#highway_mpg_fit
lm.fit(X, Y)
# Find the R^2
print('The R-square is: ', lm.score(X, Y))

#Mean_SQUARED_ERROR
Yhat=lm.predict(X)
print('The output of the first four predicted value is: ', Yhat[0:4])


mse = mean_squared_error(df['price'], Yhat)
print('The mean square error of price and predicted value is: ', mse)
#NOW FOR MULTIPLE LINEAR REGRESSION MODEL
# fit the model 
lm.fit(Z, df['price'])
# Find the R^2
print('The R-square is: ', lm.score(Z, df['price']))

Y_predict_multifit = lm.predict(Z)
print('The mean square error of price and predicted value using multifit is: ', mean_squared_error(df['price'], Y_predict_multifit))


#NOW FOR POLYNOMIAL FIT

r_squared = r2_score(y, p(x))
print('The R-square value is: ', r_squared)

print(mean_squared_error(df['price'], p(x)))

#PREDICTION AND DECISION MAKING
new_input=np.arange(1, 100, 1).reshape(-1, 1)

lm.fit(X, Y)
print(lm)

yhat=lm.predict(new_input)
print(yhat[0:5])

plt.plot(new_input, yhat)
plt.show()

