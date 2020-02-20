
#In the main() function, the Pet() class object needs arguments. So, you first need to provide the arguments
#and then input them into the Pet() class object.

class Pet:
    def __init__(self, Name, Animal_type, Age): #Creating the arguments
        self.__name = Name
        self.__animal_type = Animal_type
        self.__age = Age

#Creating the values for the argumnets
    def set_name(self, Name):
        self.__name = Name

    def set_animal_type(self, Animal_type):
        self.__animal_type = Animal_type

    def set_age(self, Age):
        self.__age = Age

    def get_name(self):
        return self.__name

#Declaring the values for the argumnets
    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age


def main():
    pet_Name = input("What's your Pet's Name: ")            #Assiging an variable for the values
    pet_Animal_type = input("What kind of pet you have: ")  #asigging the variable for the values
    pet_Age = float(input("What's the Age of your Pet: "))  #assiging the varible for the values

    pet_details = Pet(pet_Name,pet_Animal_type,pet_Age)     #Setting the variable and calling the class function
    print("The details you have entered are:")
    #Geting the results from the class function and printing all the values from the function
    print("Your Pet Name is:", pet_details.get_name())
    print("The type of Pet you have is:", pet_details.get_animal_type())
    print("And it is", pet_details.get_age(), "Years Old")

main()