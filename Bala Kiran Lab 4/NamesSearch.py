def GirlNamesReadertoList(importfile):      #Creating an function with an Argument
    girls_name_file = open(importfile, "r") #Assiging the file to an variable
    girls_list = []                         #Creating an Empty List

    girl_name = girls_name_file.readline()  #Creating an Variable to read the line with line wise

    while girl_name != "":                  #Creating an While loop to find the empty line in the file
        girl_name = girl_name.rstrip("\n")  #Assigning an rstrip function to to remove the line spaces
        girls_list.append(girl_name)        #Appending the names with the girl name list
        girl_name = girls_name_file.readline()  #assiging the line function to the girl names

    return girls_list                           #Returing the girls list

def BoysNamesReadertoList(importfile):         #Creating an function with an Argument
    boys_name_file = open(importfile, "r")     #Assiging the file to an variable)
    boys_list = []                            #Creating an Empty List

    boy_name = boys_name_file.readline()        #Creating an Variable to read the line with line wise

    while boy_name != "":                   #Creating an While loop to find the empty line in the file
        boy_name = boy_name.rstrip("\n")    #Assigning an rstrip function to to remove the line spaces
        boys_list.append(boy_name)          #Appending the names with the boy name list
        boy_name = boys_name_file.readline() #assiging the line function to the boy names

    return boys_list                        #Returing the boy list

def SearchName():                           #Function to search the names
    user_name = input("Please Enter an Boy or Girl Name to search: ") #Asking for the name to search
    search_list = []                        #Assigining the empty List

    while user_name != "exit":              #Creating an While Loop to check for the next name or for exit
        search_list.append(user_name)       #Appending the names gving by the user
        user_name = input("Please Enter an Boy or Girl Name to search or exit to Exit: ")#Asking the next name or Exit

    return search_list                      #Returning the Search Value

def SearchinFile(search_list, all_list):    #Searching the Names in the file
    Names = []                              #Assiging an Null List

    for search_index in range(len(search_list)):   #Creating an search Index for loop for the range in the list of Names
        if search_list[search_index] in all_list:   #Creting an Varible to add all the names into one list
            Names.append(search_list[search_index])

    return Names                                    #returning the Names

def PrintResults(search_list, Names):               #Function for printing the Values
    for search_index in range(len(search_list)):
        if search_list[search_index] in Names:      #Creating an if loop to find the name is in the list or not
            print(search_list[search_index], "was among the most popular names")
        else:
            print(search_list[search_index], "Was not among the most popular names")


def main():
    girl_file = "GirlNames.txt"                 #Calling the file
    boys_file = "BoyNames.txt"                  #Calling the file

    girls_list = GirlNamesReadertoList(girl_file)   #creating an girl list and assging the function for girl names to it
    boys_list = BoysNamesReadertoList(boys_file)    #Creating an boy list and assging the function for boy names to it

    all_list = girls_list + boys_list               #Adding the girl and boy to an single list

    search_list = SearchName()                      #Assigning an varabile to the search function
    names_list = SearchinFile(search_list, all_list)    #Finding the name list with respective to the search function
                                                        #and the all list function.

    PrintResults(search_list, names_list)           #Printing the values with respective to the search and name list

main()