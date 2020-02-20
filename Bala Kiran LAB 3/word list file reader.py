def wordsinfile():
    #opening the file
    readwords = open("written file.txt", "r")

    word_count = 0
    # opeing the wile as an readwords variable
    with readwords as file:
        for word in file:                               #for all the words in the file
            word_count += len(word.split())             #Wordcount is been counted by the len of the words function

    print("The Number of the words in file are: ", word_count)  #Printing the number of the words

wordsinfile()

def longestword():
    #Opening the file
    readwords = open("written file.txt", "r")

    #Assin an for loop
    for word in readwords:
        words = word.split()            #using split funtion for spliting the words
        lenword = ""                    #Asking the string value as 0 for the intial start
        for long in words:              #For loop to see the longet word
            if len(long) >= len(lenword):           #finding the longest word by the condition and finding len
                lenword = long                      #if the longest is greated reassign to lenword
        print("The longest word in the file is: ", lenword)     #Printing the lenword
longestword()

def averagelengthofwords():
    #Opening the file
    readwords = open("written file.txt", "r")


    with readwords as wordlen:
        lenword = [len(word)                            #Finding the len of an word
            for line in wordlen                         #for the lines in the wordlenth file
                for word in line.rstrip().split(" ")]   #Spliting the words by the space to have count of words
        lenword_avg = sum(lenword) / len(lenword)       #Calculting the average value by the sum of the len
        print("The average length of words is: ", format(lenword_avg, ".2f"))
        #Printing the average len of the values.
averagelengthofwords()