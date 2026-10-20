### **TASK 20: Build a CSV Data Processor**



###### **1. Introduction**



CSV stands for Comma-Separated Values. It is a simple file format commonly used to store data in a tabular format. This project uses Python to read employee salary information from a CSV file and calculate useful salary statistics.



###### **2. Objective**



* Understand CSV file processing using Python.
* Learn how to use Python's built-in csv module.
* Read employee data from a CSV file.
* Extract salary values from the CSV file.
* Calculate total, average, highest, lowest salary, and employee count.
* Handle missing or invalid salary values.
* Generate a summary report.



###### **3.Technologies Used**



\- Python

\- CSV Module

\- File Handling

\- Exception Handling



###### **4. Project Description**



The project consists of two main files: employees.csv and csv\_processor.py. The CSV file contains employee names, departments, and salaries. The Python program reads the file, extracts valid salary values, and calculates salary statistics. It also uses exception handling so that missing or invalid salary values do not stop the program.



###### **5. Input CSV Data**



Name,Department,Salary

Ravi,IT,30000

Sita,HR,25000

John,IT,40000

Anu,Sales,35000

Rahul,IT,45000



###### **6. Source Code**



import csv



def process\_csv(filename):

&#x20;   salaries = \[]

&#x20;   with open(filename, "r") as file:

&#x20;       reader = csv.DictReader(file)

&#x20;       for row in reader:

&#x20;           try:

&#x20;               salary = float(row\["Salary"])

&#x20;               salaries.append(salary)

&#x20;           except (ValueError, KeyError):

&#x20;               print("Invalid or missing salary:", row)



&#x20;   if len(salaries) == 0:

&#x20;       print("No valid salary data found.")

&#x20;       return



&#x20;   total = sum(salaries)

&#x20;   average = total / len(salaries)

&#x20;   highest = max(salaries)

&#x20;   lowest = min(salaries)

&#x20;   count = len(salaries)



&#x20;   print("\\nEmployee Salary Report")

&#x20;   print("-----------------------")

&#x20;   print("Number of employees:", count)

&#x20;   print("Total salary:", total)

&#x20;   print("Average salary:", average)

&#x20;   print("Highest salary:", highest)

&#x20;   print("Lowest salary:", lowest)



process\_csv("employees.csv")

###### 

###### **7. Working of the Program**



**1. Import CSV module:** The csv module is imported to read and process CSV files.



**2. Create function:** The process\_csv() function is created to process the given CSV filename.



**3. Create salary list:** An empty list is created to store valid salary values.



**4. Open the file:** The CSV file is opened in read mode using open().



**5. Read CSV data:** csv.DictReader() reads each row as a dictionary.



**6. Extract salary:** row\["Salary"] is converted from text to a floating-point number.



**7. Store salary:** Valid salary values are added to the salaries list.



**8. Handle errors:** ValueError and KeyError are handled using try-except.



**9. Calculate statistics:** sum(), len(), max(), and min() are used to calculate the results.



**10. Display report:** The calculated values are displayed as an Employee Salary Report.



###### **8. Output**



Employee Salary Report

\-----------------------

Number of employees: 5

Total salary: 175000.0

Average salary: 35000.0

Highest salary: 45000.0

Lowest salary: 25000.0



###### **9. Features of the Project**



* Reads employee data from a CSV file.
* Uses Python's built-in CSV module.
* Extracts salary values from each record.
* Calculates total and average salary.
* Finds the highest and lowest salary.
* Counts valid employee salary records.
* Handles missing or invalid salary values.
* Displays a clear summary report.



###### **10. Concepts Used**



Functions, lists, file handling, CSV processing, csv.DictReader(), for loop, try-except, type conversion, sum(), len(), max(), and min().

###### 

###### **11. Learning Outcomes**



This project helped me learn how to read CSV files using Python, use csv.DictReader(), extract values from rows, store data in lists, perform calculations, handle invalid data using exception handling, and generate a summary report from structured input data.

###### 

###### **12. Conclusion**



The CSV Data Processor successfully reads employee salary data from a CSV file and calculates important salary statistics. The project demonstrates practical use of Python's CSV module, file handling, lists, functions, loops, calculations, and exception handling. It provides a simple example of how Python can be used to process structured data and generate meaningful information.

