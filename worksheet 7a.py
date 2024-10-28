#SRISHTI MITTAL 102323081
# #1.1 importing pandas
#write the command to import the pandas library and chk its version.

import pandas as pd
print(pd.__versions__)

#1.2 creating a dataframe
#create a simple DataFrame using the following data:
#name age city
#alice 25 new york
#bob 30 los angeles
#charlie 35 chicago
#print the data frame

data = {'Name' : ['Alice', 'bob', ' charlie'], 
        'Age': [25, 30, 35],
          'city'; ['new york', 'los angeles', 'chicago']}
df = pd.DataFrame(data)
print(df)

#2.1panda series
#creating a panda series from a list

import pandas as pd
l = [100, 200, 300, 400, 500]
s1 = pd.Series(l)
s1

#2.2 Accessing elements in a series
#to access the second and fourth element, and print them

print(f"Second element: {s1[1]}")
print(f"Fourth element: {s1[3]}")

#2.3
#create a second series...
#perform element wise addition b/w the two series

s2 = pd.Series([10, 20, 30, 40, 50])
result = s1 + s2
print(result) 

#3.1 DataFrame column access

import pandas as pd

data = {"Name":['Alice','Bob','Charlie'],"Age":[25,30,35],"City":['New York','Los Angeles','Chicago']}
df = pd.DataFrame(data)

df.iloc[:,0:2]

#3.2 adding a new column

df['Salary'] = [50000, 60000, 70000]
print(df)

#3.3 

print(df["Age"].mean())
print(df["Salary"].sum())

#4.1 Filtering and Indexing

filtered_df = df[df['Age'] > 28]
print (filtered_df)

#4.2 

df_indexed = df.set_index('Name')
print(df_indexed)
df_reset = df_indexed.reset_index()
print(df_reset)

#5.1 working with CSV Data
#Assume you have a CSV file called employees.csv with the following content:
# Name, Department, Salary
# John, Sales, 50000
# Jane, MarkeƟng, 60000
# Emily, HR, 55000
# Write the code to read this CSV file into a Pandas DataFrame and print the contents of the
# DataFrame. 

import csv
data = [
    ["Name", "Department", "Salary"],
    ["John", "Sales", 50000],
    ["Jane", "Marketing", 60000],
    ["Emily", "HR", 55000]
]
with open("employees.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)
# Assuming the file 'employees.csv' is in the same directory
df_employees = pd.read_csv('employees.csv')
print(df_employees)

#5.2 CSV data manipulation

filtered_employees = df_employees[df_employees['Salary'] > 55000]
print(filtered_employees[['Name', 'Department']])

#6.1 grouping by department

average_salary = df_employees.groupby('Department')['Salary'].mean()
print(average_salary)

#6.2

salary_stats = df_employees.groupby('Department')['Salary'].agg(['min', 'max'])
print(salary_stats)

#7.1 Merging DataFrames

import pandas as pd

df1 = pd.DataFrame({'Name':['John', 'Jane', 'Emily'],'Department': ['Sales', 'Marketing', 'HR']})
df2 = pd.DataFrame({'Name': ['John', 'Jane', 'Emily'],'Experience (Years)': [5, 7, 3]})

df1
df2

r = pd.merge(df1, df2, on = "Name")
print(r)

#8.1 Sorting Data 

r.sort_values("Experience (Years)", axis = 0, ascending = False, inplace = True, na_position = 'last')
print(r)


