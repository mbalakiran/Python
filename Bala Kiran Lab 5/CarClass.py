class Car:
    def __init__(self, year_model, make):#speed # Creating the values
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0 #speed

#Creating the values for the variables
    def set_year_model(self, year_model):
        self.__year_model = year_model

    def set_make(self, make):
        self.__make = make

    def set_speed(self, speed):
        self.__speed = speed
#Setting and declaring the values for the varibles
    def get_year_model(self):
        return self.__year_model

    def get_make(self):
        return self.__make

    def get_speed(self):
        return self.__speed
#defing the accelerate, brake and the speed function
    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5

    def get_speeds(self):
        return self.__speed

def main():

    car_year_model = float(input("Please Enter the Model Year of the Car: "))
    car_name = input("Please Enter the Maker's Name of the Car: ")
    #car_speed = float(input("Please Enter the Current Speed of the car: "))
    #print("Where can also ask the user to enter to enter the speed to look more user specific")
    car_info = Car(car_year_model, car_name)#car_speed

#Printing the accelartion and the break functions with speeds
    car_info.accelerate()
    print("\n""After the First Accelerate, \n The current speed of the car is: ", car_info.get_speeds())

    car_info.accelerate()
    print("After the Second Accelerate, \n The current speed of the car is: ", car_info.get_speeds())

    car_info.accelerate()
    print("After the Third Accelerate, \n The current speed of the car is: ", car_info.get_speeds())

    car_info.accelerate()
    print("After the Forth Accelerate, \n The current speed of the car is: ", car_info.get_speeds())

    car_info.accelerate()
    print("After the Fifth Accelerate, \n The current speed of the car is: ", car_info.get_speeds(), "\n")

    #Brake
    car_info.brake()
    print("After the First Brake, \n The current speed of the car is: ", car_info.get_speeds())

    car_info.brake()
    print("After the Second Brake, \n The current speed of the car is: ", car_info.get_speeds())

    car_info.brake()
    print("After the Third Brake, \n The current speed of the car is: ", car_info.get_speeds())

    car_info.brake()
    print("After the Fourth Brake, \n The current speed of the car is: ", car_info.get_speeds())

    car_info.brake()
    print("After the Fifth Brake, \n The current speed of the car is: ", car_info.get_speeds())


main()
