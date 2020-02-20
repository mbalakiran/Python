#Initizlization the values
sumofnumbers = 0
number = 0

#Requesting for an Number
number = float( input("Please enter an positive number or a negative number to end: "))

#Requesting for an positive number or an negative number to exit the loop with an While loop condition for the number
#which has been entered

while number > -1:
    sumofnumbers = sumofnumbers + number
    number = float( input("Please enter an positive number or a negative number to end: "))

#Printing all the sum of the positive numbers which have been entered
print("\n The sum of all the numbers which have been entered is = ", sumofnumbers)