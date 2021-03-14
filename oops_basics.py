# OOP in Pyhton

class Car:
    # Class Attributes/Variables
    no_of_tires = 4


    # Class Constructor/Initializer (Method with a special name)
    def __init__(self, make, model, year, color, moon_roof = False):
        # Object Attributes/Variables        
        # #super().__init__()
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.moon_roof = moon_roof
        self.engine_running = False

    # Methods    
    def start_the_engine(self):
        self.engine_running = True

    def stop_the_engine(self):
        self.engine_running = False

    # Destructor
    def __del__(self):
        pass

    def get_info(self):
        print("Printing car details:".center(58, "-"))
        print("Make:      {}".format(self.make))
        print("Model:     {}".format(self.model))
        print("Year:      {}".format(self.year))
        print("Color:     {}".format(self.color))
        print("Moon Roof: {}".format(self.moon_roof))
        print("Number of tires {}".format(self.no_of_tires))



    pass

def main():
    print("Hello from the main() method")
    car1 = Car("Trabant","P601", 1972, "Schilfgrün")
    car2 = Car("Ford","Fiesta 2", 1989, "Rot")
    car3 = Car("Tesla","Model 3", 2020, "Rot", True)
    
    car1.get_info()
    car2.get_info()
    car3.get_info()

    del car3
    del car1

    car3.get_info()   






if __name__ == '__main__':
    main()