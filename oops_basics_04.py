# Inheritance in Python
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, first_name, last_name, emp_id, years_of_experience):
        self.first_name = first_name
        self.last_name = last_name
        self.emp_id = emp_id
        self.years_of_experience = years_of_experience

    @abstractmethod
    def get_monthly_salary(self):
        pass

    @abstractmethod
    def get_annual_bonus(self):
        pass

    @abstractmethod
    def get_info_employee(self):
        print("Employee Info".center(58, "-"))
        print("Name:                 {1}, {0} ".format(self.first_name, self.last_name))
        print("Emplyee ID:           {}".format(self.emp_id))
        print("Years of Experience:  {}".format(self.years_of_experience))


class FullTimeManagementEmloyee(Employee):

    __bonus_percentage = 5
    
    def __init__(self, first_name, last_name, emp_id, years_of_experience, annual_salary):
        super().__init__(first_name, last_name, emp_id, years_of_experience)
        self.annual_salary = annual_salary

    def get_monthly_salary(self):
        return self.annual_salary / 12

    def get_annual_bonus(self):
        return self.annual_salary * self.__bonus_percentage / 100 

    def get_info_employee(self):
        super().get_info_employee()
        print("Annual Salary:      $ {:8.2f}".format(self.annual_salary))
        print("Monthly Salary:     $ {:8.2f}".format(self.get_monthly_salary()))
        print("Annual Bonus:       $ {:8.2f}".format(self.get_annual_bonus()))

def main():
    print("Greeting from main method!")
    empl = FullTimeManagementEmloyee("Hans", "Wurst", "111-222-333", 5, 70000)
    empl.get_info_employee()


if __name__ == "__main__":
    main()
