# Inheritance in Python

from oops_basics_04 import FullTimeManagementEmloyee

def main():
    employee = FullTimeManagementEmloyee("Johannes", "Klotz", "100-200-300", 3, 50000)
    employee.get_info_employee()

if __name__ == "__main__":
    main()