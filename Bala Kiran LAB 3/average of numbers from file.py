def load_numbers():
    numbers = open("numbers.txt", "r")               #opening the file numbers.txt and reading it
    sum = 0                                          #declaing sum and count varables for finding average
    count = 0

    for line in numbers:                            #For checking the numbers variable in the file
        sum += int(line.split(" ")[0])              #calculating the sum of the numbers by spliting the lines
        count += 1                                  # for counting till the last number in the file

    average = sum / count                           #Calculating the average of the numbers by sum of numbers and count

    print("the average of the numbers in the file is:", average)    #Printing the average of the numbers
load_numbers()