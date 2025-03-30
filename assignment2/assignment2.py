#Task 2

import csv
import traceback
import os
import custom_module
from datetime import datetime

def read_employees():
    try:
        employees_dict = {}
        rows_list = []
        
        with open('../csv/employees.csv', newline='') as csvfile:
            csv_reader = csv.reader(csvfile)
            
           
            employees_dict["fields"] = next(csv_reader)
            
           
            employees_dict["rows"] = list(csv_reader)
            
        return employees_dict
    
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        return None


employees = read_employees()
print(employees)

#Task3 

def column_index(column_name):
    return employees["fields"].index(column_name)
employee_id_column = column_index("employee_id")

#Task4

def first_name(row_number):
    return employees["rows"][row_number][column_index("first_name")]

#Task5

def employee_find(employee_id):
   def employee_match(row):
      return int(row[employee_id_column]) == employee_id
   matches= list(filter(employee_match, employees["rows"]))
   return matches 

#Task6
def employee_find_2(employee_id):
   matches= list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))
   return matches
#Task7
def sort_by_last_name():
    employees["rows"].sort(key=lambda row: row[column_index("last_name")])
    return employees["rows"]
sort_by_last_name()
print(employees['rows'])

#Task8
def employee_dict(row):
    return {key: value for key, value in zip(employees["fields"], row)if key != "employee_id"}
print(employees['rows'])

#Task9
def all_employees_dict():
    return {row[employee_id_column]: employee_dict(row) for row in employees["rows"]}
print(all_employees_dict())

#Task10

def get_this_value():
    return os.getenv('THISVALUE')
    
print(get_this_value())

#Task11

def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)
    return custom_module.secret
print(custom_module.secret)
print(set_that_secret("abracadabra"))

#Task12
def read_minutes():
   try:
      minutes1= {"fields": [], "rows": []}
      minutes2= {"fields": [], "rows": []}
    
      with open('../csv/minutes1.csv', "r") as csvfile1:
        csv_reader1 = csv.reader(csvfile1)
        minutes1["fields"] = next(csv_reader1)  
        for row in csv_reader1:
           minutes1["rows"].append(tuple(row))
        
      with open('../csv/minutes2.csv', "r") as csvfile2:
        csv_reader2 = csv.reader(csvfile2)
        minutes2["fields"] = next(csv_reader2)  
        for row in csv_reader2:
           minutes2["rows"].append(tuple(row))  
      return minutes1, minutes2
   except Exception as e:
      trace_back = traceback.extract_tb(e.__traceback__)
      stack_trace = list()
      for trace in trace_back:
         stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
      print(f"Exception type: {type(e).__name__}")
      message = str(e)
      if message:
         print(f"Exception message: {message}")
      print(f"Stack trace: {stack_trace}")
      return None, None
minutes1, minutes2 = read_minutes() 
print(minutes1)
print(minutes2)

#Task13

def create_minutes_set():
   set1=set(minutes1["rows"])
   set2=set(minutes2["rows"])
   minutes_set=set1.union(set2)
   return minutes_set
minutes_set = create_minutes_set()
print(minutes_set)

#Task14

def create_minutes_list():
    minutes_list = list(minutes_set)
    minutes_list = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_list))
    return minutes_list
minutes_list = create_minutes_list()
print(minutes_list)


#Task15
def write_sorted_list():
   minutes_list.sort(key=lambda x: x[1])
   converted_list = list(map(lambda x: (x[0], x[1].strftime("%B %d, %Y")), minutes_list))
   with open("./minutes.csv", "w", newline='') as csvfile:
      csv_writer = csv.writer(csvfile)
      csv_writer.writerow(minutes1["fields"])
      csv_writer.writerows(converted_list)

   return converted_list
write_sorted_list()
print(write_sorted_list())   