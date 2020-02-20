class Product:
    # constructor to set default values of product class property
    def __init__(self, name, note, packing, value, item_status, unit):
        self.name = name
        self.note = note
        self.packing = packing
        self.value = value
        self.item_status = item_status
        self.unit = unit

class User_Interface:
    def __init__(self):
        self.store = {}

    def create_an_item(self, bakeryproduct):
        note = input('Enter the short description for the item: ')
        packing = input('Enter the package state (broken/unbroken): ')
        value = input('Enter the price: ')
        item_status = input("Enter the Item Status Baked or not: ")
        unit = input("Enter the Unit of the product measure(Kgs/lts : ")
        self.store[bakeryproduct] = Product(bakeryproduct, note, packing, value, item_status, unit)
        return True

    def read_an_item(self, bakeryproduct):
        if bakeryproduct in self.store:
            print(f'Name: {self.store[bakeryproduct].name}')       #f'string is a new way to format an string
            print(f'Short description: {self.store[bakeryproduct].note}')
            print(f'State of the packaging: {self.store[bakeryproduct].packing}')
            print(f'price: {self.store[bakeryproduct].value}')
            print(f'item_status: {self.store[bakeryproduct].item_status}')
            print(f'unit: {self.store[bakeryproduct].unit}')
        else:
            print(f"Sorry, {bakeryproduct} is not present in the menu")

    def update_an_item(self, bakeryproduct, note, packing, value, item_status, unit):
        if bakeryproduct in self.store:
            if note != '':
                self.store[bakeryproduct].note = note
            if packing != '':
                self.store[bakeryproduct].packing = packing
            if value != '':
                self.store[bakeryproduct].value = value
            if item_status != '':
                self.store[bakeryproduct].item_status = item_status
            if unit != '':
                self.store[bakeryproduct].unit = unit
        else:
            print(f"{bakeryproduct} was not found in the menu")

    def delete_an_item(self, bakeryproduct):
        if bakeryproduct in self.store:
            del self.store[bakeryproduct]
        else:
            print(f"{bakeryproduct} is not present in the menu")

    def exit(self):
        print("Thank you for using your notebook today.")

    def create_an_User_Interface(self):
        choice = 0
        create_an_item = 1
        read_an_item = 2
        update_an_item = 3
        delete_an_item = 4
        exit = 5

        while choice != exit:
            print('\nWelcome to Bakery (User_Interface)')
            print('1) Add new bakery item')
            print('2) Read about a bakery item')
            print('3) Update a bakery item')
            print('4) Delete a bakery item')
            print('5) exit\n')

            choice = int(input('Enter your option: '))

            if choice == create_an_item:
                name = input('Enter the name for a new item: ')
                if name in self.store:
                    print(f"{name} is already in the menu, I'll change the name to {name}_{n}")
                    name = name + f'_{n}'
                    n += 1
                if self.create_an_item(name):
                    print(f'\n{name} was added\n')

            elif choice == read_an_item:
                bakeryproduct = input("\nEnter the item's name: \n")
                self.read_an_item(bakeryproduct)

            elif choice == update_an_item:
                bakeryproduct = input('Enter the name of an updating item: ')
                note = input(
                    "Enter updated short_description, if you don't want to update this field, leave it empty: ")
                packing = input(
                    "Enter updated package_status, if you don't want to update this field, leave it empty: ")
                value = input("Enter updated price, if you don't want to update this field, leave it empty: ")
                item_status = input("Enter the Status of the product(Baked or Not Baked): ")
                unit = input("Enter the unit of the product(Kgs/Lts): ")
                self.update_an_item(bakeryproduct, note, packing, value, item_status, unit)
                print(f'\n{bakeryproduct} was updated\n')

            elif choice == delete_an_item:
                bakeryproduct = input("\nWhich item you'd like to delete? \n")
                self.delete_an_item(bakeryproduct)
                print("Item was deleted")

            elif choice == exit:
                self.exit()

            else:
                print("Please Enter the correct option")

interface = User_Interface()
interface.create_an_User_Interface()