import sys

def main():
    if len(sys.argv) == 5:
        script_name = sys.argv[0]
        empid = sys.argv[1]
        empname = sys.argv[2]
        salary = sys.argv[3]
        year_of_experience = sys.argv[4]
    else:
        script_name = sys.argv[0]
        empid = "101"
        empname = "yash"
        salary = "10000"
        year_of_experience = "5"

    print("Employee Details:")
    print(f"Employee ID: {empid}")
    print(f"Employee Name: {empname}")
    print(f"Salary: {salary}")
    print(f"Year of Experience: {year_of_experience}")

