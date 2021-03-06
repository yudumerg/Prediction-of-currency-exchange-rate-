# Adding the libraries for project
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Reading the data set
data = pd.read_csv('2016dolar.csv')
print(data)
date = data[['Date']]
print(date)
price = data[['Price']]
print(price)


#Dividing the data set as train and test data
from sklearn.model_selection import train_test_split
x_train, x_test,y_train,y_test = train_test_split(date,price,test_size=0.33, random_state=0)

#Machine Learning with Linear Regression
from sklearn.linear_model import LinearRegression
lr = LinearRegression()

#Estimating Operations
lr.fit(x_train,y_train)
prediction = lr.predict(x_test)

#Visualization of data set
x_train = x_train.sort_index()
y_train = y_train.sort_index()
plt.plot(x_train,y_train)
plt.plot(x_test,lr.predict(x_test))
plt.title("Price of Dollar")
plt.xlabel("Date")
plt.ylabel("Price")
