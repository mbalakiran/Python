def load_numbers():
    #Creating an try expression where the functions test for any error
    try:
        numbers = open("numbers.txt", "r")
        sum = 0
        count = 0
        #with open("numbers.txt", "r") as numbers:
        for line in numbers:
            #count += 1
            sum += int (line.split(" ")[0])
            count += 1

        average = sum / count

    # Except which displays any kind of error
    except IOError as ioerror:                          #IOError if the function has an error in loading the file
        print("An IOError occurred which is:", ioerror)
    except ValueError as valueerror:                    #ValueError if the value is different than the expressed value
        print("An ValueError occurred in the file which is: ", valueerror)

    else:                                               #If the fucntion executes it would be printing this output
        print("The average of the numbers in the file is:", average)

load_numbers()