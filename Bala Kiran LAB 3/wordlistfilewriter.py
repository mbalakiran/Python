def main():
    #Asking for the number of words user wants to enter
    numberofwords = int(input("Enter the number of words to be written to a file: "))

    #Creating an file with the write funtion w
    wordfile = open("Written file.txt", "w")

    #Enetering the number of the words informed by the user
    word = input("Enter the number of words requested: ")

    #Spliting the words through quatations as it understands the space and next word which has been entered by the user
    #will be taken as an new word
    words = word.split(" ")

    #Creating an while loop for checking the number of words is matching with the user count or not
    while numberofwords >= len(words):
        wordfile.write(str(word) + " ")
        break                                               #Ending the functon through break
    else:                                                   #If the number of words entered more than of requested
        print("The number of letters are more")             # Number it would be printing this error message
main()

def printfile():
    wordfile = open("written file.txt", "r")                #Opeing the file and reading the file
    wordcontent = wordfile.read()
    print("The words which have been entered to the file are: \n",wordcontent)
printfile()

