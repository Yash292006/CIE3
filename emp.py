import sys

if len(sys.argv) == 3:
    script_name = sys.argv[0]
    name = sys.argv[1]
    empid = sys.argv[2]
    salary = sys.argv[3]
    year_of_experience = sys.argv[4]
    print("User provided input values:")
else:
    script_name = sys.argv[0]
    empid = "E001"
    name = "Deepa"
    salary = "50000"
    year_of_experience = "5"
    print("No input given using default values:")

print("Script Name:", script_name)
print("Employee Name:", name)
print("Employee ID:", empid)
print("Salary:", salary)
print("Year of Experience:", year_of_experience)