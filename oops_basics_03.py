# OOP in Pyhton

class Employee:

    __gender = "female"

    # Class Constructor
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.__base_annual_salary = 0
        self.__bonus_percentage = 0                    # private Access

    # Methods
    def get_monthly_gross(self):
        return self.__base_annual_salary / 12
    
    def get_standard_annual_bonus_amount(self):
        return self.__base_annual_salary * (self.__bonus_percentage / 100)

    # Getters
    @property
    def base_annual_salary(self):
        return self.__base_annual_salary

    @property
    def bonus_percentage(self):
        return self.__bonus_percentage
        
    # Setters
    @base_annual_salary.setter
    def base_annual_salery(self, base_annual_salary):
        if 45000.00 <= base_annual_salary <= 120000.00:
            self.__base_annual_salary = base_annual_salary
        else:
            print("Annual base salary must be between 45k abd 120k!")

    @bonus_percentage.setter
    def bonus_percentage(self, bonus_percentage):
        if 5.0 <= bonus_percentage <= 21:
            self.__bonus_percentage = bonus_percentage
        else:
            print("Bonus percentages must be between 5% an 21 %") 

    def __get_employee_id(self):
        return "111-222-333"

    def get_info_employee(self):
        print("Employee Info".center(58, "-"))
        print("Name:                 {1}, {0} ".format(self.first_name, self.last_name))
        print("Gender:               {}".format(self.__gender))
        print("Emplyee ID:           {}".format(self.__get_employee_id()))
        print("Base Ann. Salary:     $ {:8.2f}".format(self.base_annual_salary))
        print("Bonus percentage:       {:8.2f} %".format(self.bonus_percentage))
        print("Monthy gross pay:     $ {:8.2f}".format(self.get_monthly_gross()))
        print("Standard Ann. Salary: $ {:8.2f}".format(self.get_standard_annual_bonus_amount()))

def main():
    print("Hello from main()!")
    empl1 = Employee("Kara", "Smith")
    empl1.base_annual_salery = 55000.00
    empl1.bonus_percentage = 5
    empl1.__gender = "male"             # this will be not assigned!
    empl1.get_info_employee()

    empl2 = Employee("Susi", "Schmusi")
    empl2.base_annual_salery = 55000.00
    empl2.bonus_percentage = 5
    empl2.__gender = "male"
    empl2.get_info_employee()
    


    

if __name__ == '__main__':
    main()
