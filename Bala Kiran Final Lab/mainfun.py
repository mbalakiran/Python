from Class_Bakery import Product
from User_Interface import Menu


def choice_list():

    choice = 0

    while choice != EXIT:

        select_choice()

        choice = int(input("Please Enter your choice: "))

        if choice == CREATE_BAKERY_ITEM:
           print("")

        elif choice == READ_ABOUT_ITEM:
            print("")

        elif choice == UPDATE_AN_ITEM:
            print("")

        elif choice == DELETE_AN_ITEM:
            print("")

        elif choice == EXIT:
            print("Exited")
        else:
            print("Invalid Choice")

        break
    else:
        print(" ")

def select_choice():
    print("Select your Choice: ")
    print("1. Create An Bakery Item ")
    print("2. To Read About an Item ")
    print("3. To Update an Item ")
    print("4. To Delete an Item ")
    print("5. To Exit the Bakery")

def defined_products():
    try:
        #content = open("All_Products.txt", "a")
        itemlist = [ ]
        # space = " "
        #print(itemlist)

        item1 = Product("Bread", "Soft Bread", "Not Broken", 10, "Not Baked")
        item2 = Product("Cake", "Soft Cake", "Broken", 60, "Baked")
        item3 = Product("Cookie", "Chocolate Cookie", "Not Broken", 20, "Baked")
        item4 = Product("Chocolates", "Chocolate Pack", "Not Broken", 40, "Baked")
        name = item1.get_name()
        note = item1.get_note()
        list_inst = [name, note]
        print(list_inst)
        itemlist.extend([item1,item2,item3,item4])
        print (itemlist[0].item1)

    except ValueError as valueerror:
        print(itemlist, valueerror)
    else:
        print(itemlist)

