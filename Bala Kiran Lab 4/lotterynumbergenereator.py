import random

def Random_Numbers():
    ##Declaring the Random Numbers from the range 0-9 with 7 digit
    random_number = [random.sample(range(0,9), 7)]

    return random_number                        #Returning the Random Number

def lotter_number(lottery_list):                #Creating funtion with argument to print the lottery number

    number = len(lottery_list)                  #Creating an Variable "Number" and assiging the argument with length

    for num_list in range(number):              #Creating an for loop for the range Number
        print("Your Lottery Number is: ", lottery_list[num_list])           #Prnting the Argument


def main():

    random_number = Random_Numbers()            #Assiging random number variable to the Random_number function
    lotter_number(random_number)                #Calling the Lotter_number function with respective to Random Variable

main()

