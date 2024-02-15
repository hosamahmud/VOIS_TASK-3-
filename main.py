import csv
import pandas as pd

dataFrame =pd.read_csv('Employees.csv')
dataFrame.drop_duplicates(subset='Name ',keep='first', inplace= True)
dataFrame['Age'] = dataFrame['Age'].round()
dataFrame['Salary(EGP)'] = dataFrame['Salary(USD)']* 30.9386
dataFrame.drop('Salary(USD)' , axis=1 , inplace=True)


x = dataFrame['Age'].mean()
y = dataFrame['Salary(EGP)'].median()
z = dataFrame['Gender'].value_counts(normalize=True)

print(" Average age: ", x )
print(" Median salaries: ", y)
print(" Ratio beetween males and female employees:\n ", z)

final = 'Employees_final.csv'
dataFrame.to_csv(final)

print("the final DataFrame is : ")
print(dataFrame)



