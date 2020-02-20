class Person:
    def __init__(self, Name, Address, Age, Phone): #Creating the varibles for the class
        self.__name = Name
        self.__address = Address
        self.__age = Age
        self.__phone_num = Phone

    #Set methods
    def set_name(self,Name):
        self.__name = Name
    def set_address(self, Address):
        self.__address = Address
    def set_age(self, Age):
        self.__age = Age
    def set_phone_num(self, Phone):
        self.__phone_num = Phone


    #Get methods
    def get_name(self):
        return self.__name
    def get_address(self):
        return self.__address
    def get_age(self):
        return self.__age
    def get_phone_num(self):
        return self.__phone_num

def main():
    print("Please Note: I am asking all the required names like User Name, Friend Name and the Family Member " +\
    "Names from the user to look more user specify for the Names")
    #Askking the Self details from the user
    self_Name = input("Please enter your Name: ")
    self_Address = input("Please enter your own Address: ")
    self_Age = int(input("Please enter your Age: "))
    self_Phone = int(input("Please enter your Phone Number: "))
    #Asking the Friend Details from the user
    friend_Name = input("Please enter your Friend Name: ")
    friend_Address = input("Please enter your Friend Address: ")
    friend_Age = int(input("Please enter your Friend Age: "))
    friend_Phone = int(input("Please enter your Friends Phone number: "))
    #Asking the Family Member Details from the user
    family_Name = input("Please enter your Family Member Name: ")
    family_Address = input("Please enter your Family Member address: ")
    family_Age = int(input("Please enter your Family Member age: "))
    family_Phone = int(input("Please enter your Family Member Phone number: "))

    #Calling all the functions from the class variables
    self_details = Person(self_Name, self_Address, self_Age, self_Phone)
    friend_details = Person(friend_Name, friend_Address, friend_Age, friend_Phone)
    family_details = Person(family_Name, family_Address, family_Age, family_Phone)

    #Printing the self Details
    print("Your Name is: ", self_details.get_name())
    print("Your Address is: ", self_details.get_address())
    print("Your Age is: ", self_details.get_age())
    print("Your Phone number is: ", self_details.get_phone_num())
    #Printing the friend details
    print("Your Friend Name is: ", friend_details.get_name())
    print("Your Friend Address is: ", friend_details.get_address())
    print("Your Friend Age is: ", friend_details.get_age())
    print("Your Friend Phone number is: ", friend_details.get_phone_num())
    #Printing the Family Members Details
    print("Your Family Member Name is: ", family_details.get_name())
    print("Your Family Member Address is: ", family_details.get_address())
    print("Your Family Member Age is: ", family_details.get_age())
    print("Your Family Member Phone number is: ", family_details.get_phone_num())

main()

#def friend():
 #   friend_Name = input("Please enter your Friend Name: ")
 #   friend_Address = input("Please enter your Friend Address: ")
 #   friend_Age = int(input("Please enter your Friend Age: "))
 #   friend_Phone = int(input("Please enter your Friends Phone number: "))


  #  friend_details = Person(friend_Name, friend_Address, friend_Age, friend_Phone)


 #   print("Your Friend Name is: ", friend_details.get_name())
 #   print("Your Friend Address is: ", friend_details.get_address())
 #   print("Your Friend Age is: ", friend_details.get_age())
 #   print("Your Friend Phone number is: ", friend_details.get_phone_num())

#friend()

#def family():
   # family_Name = input("Please enter your Family Member Name: ")
   # family_Address = input("Please enter your Family Member address: ")
   # family_Age = int(input("Please enter your Family Member age: "))
   # family_Phone = int(input("Please enter your Family Member Phone number: "))


  #  family_details = Person(family_Name, family_Address, family_Age, family_Phone)


  #  print("Your Family Member Name is: ", family_details.get_name())
   # print("Your Family Member Address is: ", family_details.get_address())
  #  print("Your Family Member Age is: ", family_details.get_age())
 #   print("Your Family Member Phone number is: ", family_details.get_phone_num())

#family()