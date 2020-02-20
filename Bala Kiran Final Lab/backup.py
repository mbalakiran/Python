from Class_Bakery import Bakery_Item
from User_Interface import User_Interface

def User_Interface_menu(self):
    n = 1
    choice = 0
    create_an_item = 1
    read_an_item = 2
    update_an_item = 3
    delete_an_item = 4
    count_in_bakery = 5
    value_of_bakery = 6
    percentage_of_unbroken = 7
    exit = 8

    while choice != exit:
        print("1. Add an New Bakery Item")
        print("2. Read about the Bakery Item")
        print("3. Update an Bakery Item")
        print("4. Delete an Bakery Item")
        print("5. Count the Items in the Bakery")
        print("6. Count the Value of the Items in the Bakery")
        print("7. Count the percentages of Unbroken Items in the Bakery")
        print("8. Exit the Bakery")

        try:
            choice = int(input("Please Enter your Option: "))
        except ValueError as err:
            print(err, "is not an valid choice")

        if choice == create_an_item:
            name = input("Please Enter the Name for the Bakery Item: ").lower()
            if name in self.menu_stock:
                print(F"{name} is already in the Bakery Item list. I will be adding the new {name} as {name}_{n}")
                name = name + F"_{n}"
                n += 1
            if self.create_an_item(name):
                print(F"{name} was Added to the Bakery Item\n")

        elif choice == read_an_item:
            bakery_item = input("Please Enter the Name of the item to Display the Details: ")
            self.read_an_item(bakery_item)

        elif choice == update_an_item:
            bakery_item = input("Please Enter the Name of the Item in Bakery to be updated: ").lower()
            note = input("Please Enter the New Note for the Bakery Item Or Leave it Blank").lower()
            value = input("Please Enter the Value of the Item: SEK ")
            unit = input("Please Enter the Unit of the Item in Kilo/Lit/Pack: ").lower()
            self.update_an_item(bakery_item, note, value, unit)
            print(F"\n {bakery_item} has been updated successfully \n")

        elif choice == delete_an_item:
            bakery_item = input("Please Enter the Item Name to be Deleted from the List: ")
            self.delete_an_item(bakery_item)
            print(F"\n The item name {bakery_item} has been deleted from the record \n ")

        elif choice == count_in_bakery:
            self.show_items_count_in_bakery()

        elif choice == value_of_bakery:
            self.total_sum_of_items()

        elif choice == percentage_of_unbroken:
            if len(self.menu_stock) > 0:
                self.items_with_unbroken_packing()
            else:
                print("\n The Bakery is Empty \n")

        elif choice == exit:
            self.exit_from_bakery()

        else:
            print("Please Enter an Valid option to enter the Bakery")

#mybakery = User_Interface()
User_Interface_menu(self)



