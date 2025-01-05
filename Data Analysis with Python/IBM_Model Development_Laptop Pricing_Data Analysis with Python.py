import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error, r2_score
import warnings
warnings.filterwarnings("ignore", category=UserWarning) 

filepath = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-Coursera/laptop_pricing_dataset_mod2.csv"
df = pd.read_csv(filepath)

print(df.head())

lm = LinearRegression()
print(lm)

X = df[['CPU_frequency']]
Y = df['Price']
lm.fit(X, Y)

Yhat = lm.predict(X)
print(Yhat[0:5])

ax1 = sns.distplot(df['Price'], hist=False, color="r", label="Actual Value")

# Create a distribution plot for predicted values
sns.distplot(Yhat, hist=False, color="b", label="Fitted Values" , ax=ax1)

plt.title('Actual vs Fitted Values for Price')
plt.xlabel('Price')
plt.ylabel('Proportion of laptops')
plt.legend(['Actual Value', 'Predicted Value'])
plt.show()

print("The R_squared value for LRM is:\n", lm.score(X,Y))

mse = mean_squared_error(df['Price'], Yhat)
print("Mean_Squared_Error of Price and Predicted Price is\n", mse)


                #MULTIPLE LINEAR REGRESSION
lm1= LinearRegression()
Z = df[['CPU_frequency', 'RAM_GB', 'Storage_GB_SSD', 'CPU_core', 'OS', 'GPU', 'Category']]
lm1.fit(Z, Y)
print("MLR\n", lm1.intercept_)
print(lm1.coef_)

Y_hat = lm1.predict(Z)
print(Y_hat[0:10])

ax2 = sns.distplot(Y, hist=False, color="r", label="Actual Value")

# Create a distribution plot for predicted values
sns.distplot(Y_hat, hist=False, color="b", label="Fitted Values" , ax=ax2)

plt.title('Actual vs Fitted Values for Price(MLR)')
plt.xlabel('Price')
plt.ylabel('Proportion of laptops')
plt.legend(['Actual Value', 'Predicted Value'])
plt.show()


print("The R_squared value for MLR is:\n", lm1.score(Z,Y))

#predict_multifit
mse = mean_squared_error(Y, Y_hat)
print("Mean_Squared_Error of Price and Predicted Price is\n", mse)

#POLYNOMIAL REGRESSION

X = X.to_numpy().flatten()
x = df['CPU_frequency']
y = df['Price']
#orders = [1,3,5]
#for order in orders:
#   p = np.poly1d(f)
 #   print(p)
#p
#PlotPolly(p, x, y, 'highway-mpg')
#np.polyfit(x, y, 3)

f1 = np.polyfit(X, Y, 1)
p1 = np.poly1d(f1)

f3 = np.polyfit(X, Y, 3)
p3 = np.poly1d(f3)

f5 = np.polyfit(X, Y, 5)
p5 = np.poly1d(f5)

def PlotPolly(model, independent_variable, dependent_variabble, Name):
    x_new = np.linspace(independent_variable.min(),independent_variable.max(),100)
    y_new = model(x_new)

    plt.plot(independent_variable, dependent_variabble, '.', x_new, y_new, '-')
    plt.title(f'Polynomial Fit for Price ~ {Name}')
    ax = plt.gca()
    ax.set_facecolor((0.898, 0.898, 0.898))
    fig = plt.gcf()
    plt.xlabel(Name)
    plt.ylabel('Price of laptops')
    plt.show()

PlotPolly(p1, X, Y, 'CPU_frequency')
PlotPolly(p3, X, Y, 'CPU_frequency')
PlotPolly(p5, X, Y, 'CPU_frequency')


p_values = [p1, p3, p5]

for value in p_values:
    r_squared = r2_score(Y, value(X))
    print('The R-square value is: ', r_squared)

    print(mean_squared_error(Y, value(X)))


#PIPELINE

#PIPELINE
Input=[('scale',StandardScaler()), ('polynomial', PolynomialFeatures(include_bias=False)), ('model',LinearRegression())]
pipe=Pipeline(Input)
print("Pipe", pipe)

Z = Z.astype(float)
pipe.fit(Z,Y)

ypipe=pipe.predict(Z)
print("YPipe\n", ypipe[0:4])



print('MSE for multi-variable polynomial pipeline is\n: ', mean_squared_error(Y, ypipe))
print('R^2 for multi-variable polynomial pipeline is\n: ', r2_score(Y, ypipe))

