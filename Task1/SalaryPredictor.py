import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

data=pd.read_csv("SalaryData.csv")

y=data['Salary']
x=data['YearsExperience']
x=x.values.reshape(-1,1)

model=LinearRegression()
model.fit(x,y)

p=int(input("Enter the years of experience for which salary will be predicted: "))
out=model.predict([[p]])

print(out)