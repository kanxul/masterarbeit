# OOP in Pyhton

class My_Calc:
    
    # Class Attributes/Variables
    
    # Class Constructor/Initializer (Method with a special name)
    def __init__(self, num1, num2):
        # Object Attributes/Variables        
        self.num1 = num1
        self.num2 = num2

    # Methods    
    def total(self):
        return self.num1 + self.num2

    def diff(self):
        return self.num1 - self.num2

    def get_result(self):
        print("Total = {}".format(self.total()))
        print("Diff =  {}".format(self.diff()))



def main():
    print("Hello from the main() method")
    calc1 = My_Calc(20,20)
    calc2 = My_Calc(-5,20)
    
    calc1.get_result()
    calc2.get_result()
    



if __name__ == '__main__':
    main()


