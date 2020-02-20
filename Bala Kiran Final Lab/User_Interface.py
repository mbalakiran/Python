from Class_Bakery import Bakery_Item

class User_Interface:
    def __init__(self):
        self.menu_stock = {}

  #  def read_from_file(self, file_name):
   #     file = open(file_name, "rb")
    #    file.close()

    def create_an_item(self, bakery_item):
        note = input("Please Enter the Note for the Item: ")
        packing = input("Please Enter the Packing(broken/unbroken): ").lower()
        if packing not in ['broken' , 'unbroken']:
            print(F"{packing} is not in the broken or unbroken. Please select correct option")
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
            print(F"Name = {self.menu_stock[bakery_item].name}")
            print(F"Note = {self.menu_stock[bakery_item].note}")
            print(F"Packing Status = {self.menu_stock[bakery_item].packing}")
            print(F"Value = {self.menu_stock[bakery_item].value}")
            print(F"Units = {self.menu_stock[bakery_item].units}\n")
            timenow = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(F"It is been baked on ", timenow)
            print(F"{self.menu_stock[bakery_item].name} is "
                  F"{(date.today() - self.menu_stock[bakery_item].produced).days} Days Old \n ")
        else:
            print(F" They is No Item Name {bakery_item} in the Store")

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
                print(F"{bakery_item} is not Found in the Store")

    def delete_an_item(self, bakery_item):
        if bakery_item in self.menu_stock:
            del self.menu_stock[bakery_item]
        else:
            print(F"{bakery_item} was not found in the Store to Delete")

    def show_items_count_in_bakery(self):
        print(F"As of now we have {len(self.menu_stock)} in the bakery \n")

    def total_sum_of_items(self):
        print(F"The sum of the value in the bakery is {sum(float(self.menu_stock[i].value) for i in self.menu_stock)}")

    def items_with_unbroken_packing(self):
        unbroken_pack = len([self.menu_stock[i]
                             for i in self.menu_stock
                             if self.menu_stock[i].packing == "unbroken"])
        print(F"{round(unbroken_pack/len(self.menu_stock)*100, 2)}% of all the items in bakery have unbroken packing")

    def exit_from_bakery(self):
        print("Thank you for your Visit to the Bakery!! See you Soon.")