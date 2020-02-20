import random

print("I am Calculating the Magic Square by taking the Random Numbers")

r_number = random.sample(range(1, 10), 3 * 3)  #Creating an Random Number with the numbers 1-9 and by 2D list 3*3 Matrix

print(r_number[0:3])                            #Printing the First Row
print(r_number[3:6])                            #Printing the Second Row
print(r_number[6:])                             #Printing the Third Row

def Lo_shu_Magic(r_number):                 #Creating an Main Function with rnumber as argument
    row_0 = r_number[0] + r_number[1] + r_number[2]         #Creating an row and columns and dig up addtions

    row_1 = r_number[3] + r_number[4] + r_number[5]

    row_2 = r_number[6] + r_number[7] + r_number[8]

    col_0 = r_number[0] + r_number[1] + r_number[2]

    col_1 = r_number[3] + r_number[4] + r_number[5]

    col_2 = r_number[6] + r_number[7] + r_number[8]

    diag_up = r_number[2] + r_number[4] + r_number[6]

    diag_down = r_number[0] + r_number[4] + r_number[8]


        #or if row_0 == row_1 == row_2 == col_0 == col_1 == col_2 == diag_up == diag_down:
    if row_0 == row_1 and row_0 == row_2 and row_0 == col_0 and row_0 == col_1 and row_0 == col_2 and row_0 == diag_up \
           and row_0 == diag_down: #Checking the IF condition for the sum is equal to all the rows =columns = dig
        print("This is a Lu Shu Magic Square!")
    else:                           #Else Not magic square
        print("This is not a Lu Shu Magic Square")
    print("The Sum of row 1 is", row_0, "\t\t\tThe sum of row 2 is", row_1, "\t\t\tThe sum of row 3 is", row_2)
    print("The Sum of column 1 is", col_0, "\t\t\tThe Sum of column 2 is", col_1, "\t\t\tThe Sum of column 3 is", col_2)
    print("The sum of Diagonal Up is ", diag_up, "\t\t\tThe sum of Diagonal down is ", diag_down)

    return


Lo_shu_Magic(r_number)
