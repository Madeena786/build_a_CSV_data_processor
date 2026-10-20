### 

### **Task 20 - Build a CSV Data Processor**



A Python project that reads employee salary data from a CSV file and calculates useful salary statistics such as total salary, average salary, highest salary, lowest salary, and number of employees.

Project Description

This project demonstrates practical CSV processing using Python's built-in csv module.



The program reads employee information from a CSV file, extracts salary values, and calculates different statistics from the salary data.



It also handles missing or invalid salary values using exception handling.



###### **Objectives**

\- Learn how to read CSV files using Python.

\- Understand the use of Python's csv module.

\- Extract data from CSV files.

\- Calculate salary statistics.

\- Handle missing or invalid values.

\- Generate a simple summary report.



###### **Technologies Used**

\- Python

\- CSV module

\- File handling

\- Exception handling



###### **Project Structure**

CSV\_Data\_Processor/

├── employees.csv

├── csv\_processor.py



###### **Input CSV File**

Name,Department,Salary

Ravi,IT,30000

Sita,HR,25000

John,IT,40000

Anu,Sales,35000

Rahul,IT,45000


###### **Python Program**

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



###### **How the Program Works**

1\. The csv module is imported.

2\. The process\_csv() function receives the CSV filename.

3\. An empty list is created to store valid salaries.

4\. The CSV file is opened in read mode.

5\. csv.DictReader() reads each row as a dictionary.

6\. The salary value is converted to a number using float().

7\. Valid salaries are added to the list.

8\. try-except handles missing or invalid salary values.

9\. sum(), len(), max(), and min() calculate the statistics.

10\. The final employee salary report is displayed.



###### **Output**

Employee Salary Report

\-----------------------

Number of employees: 5

Total salary: 175000.0

Average salary: 35000.0

Highest salary: 45000.0

Lowest salary: 25000.0

###### 

###### **Key Concepts Learned**

\- CSV file handling

\- Python csv module

\- csv.DictReader()

\- Lists

\- Functions

\- Loops

\- try-except

\- Type conversion

\- sum()

\- len()

\- max()

\- min()



###### **Conclusion**

The CSV Data Processor successfully reads employee salary data from a CSV file and generates useful salary statistics.

This project helped me understand practical CSV processing, file handling, data extraction, calculations, and exception handling using Python.

