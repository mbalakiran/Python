
CREATE_BAKERY_ITEM = 1
READ_ABOUT_ITEM = 2
UPDATE_AN_ITEM = 3
DELETE_AN_ITEM = 4
EXIT = 5


def main():
    choice = 0
    all_list = [ ]
    name = []
    note = []
    packing = []
    value = []
    all_list.extend((name, note, packing, value))

   # complete_file = ("All_Products.txt", "a")

    while choice != EXIT:
        select_choice()



        choice = int(input())
        if choice == CREATE_BAKERY_ITEM:
            #number = int(input("How many Items you want to add: "))
            #for x in range(number)
            names = input("Enter Name: ")
            name.append(names)
            notes = input("Enter Notes: ")
            note.append(notes)
            packs = input("Enter Packing: ")
            packing.append(packs)
            values = input("Enter Value: ")
            value.append(values)



        elif choice == READ_ABOUT_ITEM:
            #for x in range()



