#Requesting the user to input two numbers and returning them
def numbers():
    firstnumber = float(input("Please enter the first number: "))
    secondnumber = float(input("Please enter the second number: "))

    return firstnumber, secondnumber

#Defining them and giving in if condition
def mymax(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

def main():
    firstnumber, secondnumber = numbers()  #assiging the two numbers to numbers()

    print("\nThe greatest number between", format(firstnumber, ",.2f"), "and", format(secondnumber, ",.2f"), "is", \
          mymax(format(firstnumber, ",.2f") , format(secondnumber, ",.2f")))
    # Printing both the numbers and checking them with the my_max function to print the greatest numbers


main()