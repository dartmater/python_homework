import numpy as np
import pandas as pd

#Task1 
#dict of lists

create_dictionary = {'Name': ['Alice', 'Bob', 'Charlie'] ,
'Age': [25, 30, 35],
'City': ['New York', 'Los Angeles', 'Chicago']}

df_create_dictionary = pd.DataFrame(create_dictionary)
print("DataFrame from dictionary of lists:")
print(df_create_dictionary)

task1_data_frame = df_create_dictionary

#Adding a column to the DataFrame
task1_with_salary = df_create_dictionary.copy()
task1_with_salary['Salary'] = [70000, 80000, 90000]

print(task1_with_salary)

# Modify the existing column
task1_older = task1_with_salary.copy()
task1_older['Age'] = task1_with_salary['Age'] + 1
print(task1_older) 

#Save the DataFrame to a CSV file
task1_older.to_csv("employees.csv", index=False)

print("employees.csv")

#Task2
#Load csv into new df
task2_employees = pd.read_csv("employees.csv")
print(task2_employees)

#Read data from JSON

additional_employees = [ 
    {
        "Name": "Eve",
        "Age": 28,
        "City": "Miami",
        "Salary": 60000
    },
    {
        "Name": "Frank",
        "Age": 40,
        "City": "Seattle",
        "Salary": 95000
    }   
]

#  Create the JSON file
with open("additional_employees.json", "w") as f:
    pd.DataFrame(additional_employees).to_json(f, orient="records", indent=4)

json_employees = pd.read_json("additional_employees.json")
print(json_employees)


# Concat employees
more_employees=pd.concat([task2_employees,json_employees], ignore_index=True)

print(more_employees)

#Task3
#1st 3
first_three=more_employees.head(3)
print(first_three)

#last 2

last_two = more_employees.tail(2)
print(last_two)

#get shape means a tuple representing the number of rows and columns in df

employee_shape=more_employees.shape

print(employee_shape)

#info 

more_employees.info()

#Task 4

#Data cleaning
#create df from csv 
dirty_data=pd.read_csv("dirty_data.csv")
print(dirty_data)

#create a copy of df

clean_data = dirty_data.copy()

#remove duplicate rows from df

clean_data=clean_data.drop_duplicates()
print(clean_data)

#convert Age to numeric

clean_data["Age"] = pd.to_numeric(clean_data["Age"], errors='coerce')
clean_data["Age"] = clean_data["Age"].fillna(clean_data["Age"].mean())
print(clean_data)

#convert Salary

clean_data["Salary"] = pd.to_numeric(clean_data["Salary"], errors='coerce')
clean_data["Salary"] = clean_data["Salary"].replace(['unknown', 'n/a'], np.nan)
print(clean_data)

#Age with mean and Salary with median

clean_data["Age"]=clean_data["Age"].fillna(clean_data["Age"].mean())
clean_data["Salary"]=clean_data["Salary"].fillna(clean_data["Salary"].median())

print(clean_data)

#convert Hire Date to datetime

clean_data["Hire Date"] = pd.to_datetime(clean_data["Hire Date"], errors='coerce')

print(clean_data)

#strip xtr whitespaces Name and Department to uppercase

clean_data["Name"]=clean_data["Name"].str.strip().str.upper()
clean_data["Department"]=clean_data["Department"].str.strip().str.upper()

print(clean_data)

