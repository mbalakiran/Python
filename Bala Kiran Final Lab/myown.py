from datetime import datetime, date
import pickle
class Bakery_Item:

    def __init__(self, name, note, packing, value, units):
        self.name = name
        self.note = note
        self.packing = packing
        self.value = value
        self.prepared = datetime.now()
        self.produced = date.today()
        self.units = units

class User_Interface:
    def __init__(self):
        self.menu_stock = {}

    def create_an_item(self, bakery_item):
        note = input("Please Enter the Note for the Item: ").lower()
        packing = input("Please Enter the Packing(broken/unbroken): ").lower()
        if packing not in ['broken', 'unbroken']:
            print(F"{packing} is not in the status of broken or unbroken. Please select correct option")
            return False
        try:
            value = float(input("Please enter the Value of the Item: SEK: "))
        except ValueError as err:
            print(err, "is not an number, please enter the number")
            return False
        units = input("Please Enter the Units of Measure of the Item(Kgs/Lts/Piece): ").lower()
        if units not in ['kgs', 'lts', 'piece']:
            print(F"{units} is not in the described units of measure. Please Select the Correct one")
            return False
        self.menu_stock[bakery_item] = Bakery_Item(bakery_item, note, packing, value, units)
        return True

    def read_an_item(self, bakery_item):
        if bakery_item in self.menu_stock:
            print(F"Name of the Item = {self.menu_stock[bakery_item].name}")
            print(F"Note of the Item = {self.menu_stock[bakery_item].note}")
            print(F"Packing Status of the Item = {self.menu_stock[bakery_item].packing}")
            print(F"Value = {self.menu_stock[bakery_item].value}")
            print(F"Units of Measure is = {self.menu_stock[bakery_item].units}\n")
            timenow = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(F"It is been baked on ", timenow)
            print(F"{self.menu_stock[bakery_item].name} is "
                  F"{(date.today() - self.menu_stock[bakery_item].produced).days} Days Old \n ")
        else:
            print(F" They is No Item Name {bakery_item} in the Store. Please Enter an Valid Item Name")

    def update_an_item(self, bakery_item, note, packing, value, units):
        if bakery_item in self.menu_stock:
            if note != " ":
                self.menu_stock[bakery_item].note = note
            if packing != " ":
                if packing not in ['broken', 'unbroken']:
                    print(F"{packing} is not an valid option. Please select correct option to update the Item")
                else:
                    self.menu_stock[bakery_item].packing = packing
            if value != " ":
                try:
                    float(value)
                    self.menu_stock[bakery_item].value = value
                except ValueError as err:
                    print(err, "is not an Valid option to update the value of the item")
            if units != " ":
                if units not in ['kgs', 'lts', 'piece']:
                    print(F"{units} is not in the described units of measure. Please Select the Correct one")
                else:
                    self.menu_stock[bakery_item].units = units
            else:
                print(F"{bakery_item} is not Found in the Store to Update. Don't worry You can Create the Item")

    def delete_an_item(self, bakery_item):
        if bakery_item in self.menu_stock:
            del self.menu_stock[bakery_item]
            print(F"\n{bakery_item} was successfully delete from the store")
        else:
            print(F"{bakery_item} was not found in the Store to Delete")

    def show_items_count_in_bakery(self):
        print(F"\nAs of now we have {len(self.menu_stock)} in the bakery \n")

    def total_sum_of_items(self):
        print(F"\nThe sum of the value in the bakery is {sum(float(self.menu_stock[i].value) for i in self.menu_stock)}")

    def items_with_unbroken_packing(self):
        unbroken_pack = len([self.menu_stock[i]
                             for i in self.menu_stock
                             if self.menu_stock[i].packing == "unbroken"])
        print(F"\n{round(unbroken_pack/len(self.menu_stock)*100, 2)}% of all the items in bakery have unbroken packing")

    def read_items_from_the_file(self, createdfile):
        try:
            file = open(createdfile, "rb")
            self.menu_stock = pickle.load(file)
            file.close()
        except IOError as err:
            print("\n There is no file exits with the name: ", err)

    def write_to_the_file(self, createdfile):
        try:
            file = open(createdfile, "wb")
            pickle.dump(self.menu_stock, file)
            file.close()
        except IOError as err:
            print("\n We are not able to find the filename with ", err)

    def exit_from_bakery(self):
        print("Thank you for your Visit to the Bakery!! See you Soon.")

    def User_Interface_menu(self):
        n = 1
        choice = 99
        create_an_item = 1
        read_an_item = 2
        update_an_item = 3
        delete_an_item = 4
        count_in_bakery = 5
        value_of_bakery = 6
        percentage_of_unbroken = 7
        read_the_items_from_file = 8
        write_the_items_to_file = 9
        exit = 0

        while choice != exit:

            print("1. Add an New Bakery Item")
            print("2. Read about the Bakery Item")
            print("3. Update an Bakery Item")
            print("4. Delete an Bakery Item")
            print("5. Count the Items in the Bakery")
            print("6. Count the Value of the Items in the Bakery")
            print("7. Count the percentages of Unbroken Items in the Bakery")
            print("8. Read the Items from the File")
            print("9. Write the Items to the File ")
            print("0. Exit the Bakery\n")

            try:
                choice = int(input("Please Enter your Option: "))
            except ValueError as err:
                print(err, "is not an valid choice")

            if choice == create_an_item:
                name = input("\nPlease Enter the Name for the Bakery Item: ").lower()
                if name in self.menu_stock:
                    print(F"{name} is already in the Bakery Item list. The {name} will be added as {name}{n}")
                    name = name + F"{n}"
                    n += 1
                if self.create_an_item(name):
                    print(F"{name} was Added to the Bakery Item\n")

            elif choice == read_an_item:
                bakery_item = input("Please Enter the Name of the item to Display the Details: ").lower()
                self.read_an_item(bakery_item)

            elif choice == update_an_item:
                bakery_item = input("\n Please Enter the Name of the Item in Bakery to be updated: ").lower()
                if bakery_item in self.menu_stock:
                    note = input("Please Enter the New Note for the Bakery Item Or Leave it Blank: ").lower()
                    packing = input("Please Enter the Packing for the Bakery Item or Leave It Blank: ").lower()
                    value = input("Please Enter the Value of the Item: SEK ")
                    units = input("Please Enter the Unit of the Item in Kilo/Lit/Pack: ").lower()
                    self.update_an_item(bakery_item, note, packing, value, units)
                    print(F"\n {bakery_item} has been updated successfully \n")
                else:
                    print(F"\n {bakery_item} is not in the items. ")
                    print(F"Please Enter a valid name which is in the stock to be Updated")

            elif choice == delete_an_item:
                bakery_item = input("Please Enter the Item Name to be Deleted from the List: ")
                if bakery_item in self.menu_stock:
                    self.delete_an_item(bakery_item)
                    print(F"\n The item name {bakery_item} has been deleted from the record \n ")
                else:
                    print(F"\n {bakery_item} We are not able to find the Item. \n ")

            elif choice == count_in_bakery:
                self.show_items_count_in_bakery()

            elif choice == value_of_bakery:
                self.total_sum_of_items()

            elif choice == percentage_of_unbroken:
                if len(self.menu_stock) > 0:
                    self.items_with_unbroken_packing()
                else:
                    print("\n The Bakery is Empty \n")

            elif choice == read_the_items_from_file:
                createdfile = input("Please Enter the file name with items to read(Skip Extension): ")
                self.read_items_from_the_file(createdfile + ".pkl")

            elif choice == write_the_items_to_file:
                createdfile = input("Please Enter file name to save(Skip Extension): ")
                self.write_to_the_file(createdfile + ".pkl")

            elif choice == exit:
                self.exit_from_bakery()

            else:
                print("Please Enter an Valid option to enter the Bakery")

mybakery = User_Interface()
mybakery.User_Interface_menu()


