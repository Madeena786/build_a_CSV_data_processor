import csv
def process_csv(filename):
    salaries = []
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                salary = float(row["Salary"])
                salaries.append(salary)
            except (ValueError, KeyError):
                print("Invalid or missing salary:", row)
    if len(salaries) == 0:
        print("No valid salary data found.")
        return
    total = sum(salaries)
    average = total / len(salaries)
    highest = max(salaries)
    lowest = min(salaries)
    count = len(salaries)
    print("\nEmployee Salary Report")
    print("-----------------------")
    print("Number of employees:", count)
    print("Total salary:", total)
    print("Average salary:", average)
    print("Highest salary:", highest)
    print("Lowest salary:", lowest)
process_csv("employees.csv")
