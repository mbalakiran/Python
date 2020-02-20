# Area of Rectangles
#Initialization the valiables
length1 = 0.0
width1 = 0.0
length2 = 0.0
width2 = 0.0

#Requesting for values of the Length and Width for both the rectangles from the user

length1 = float ( input("Enter the length of the rectangle 1 = "))
width1 = float ( input("Enter the width of the rectangle 1 = "))
length2 = float( input("Enter the length of the rectangle 2 = "))
width2 = float( input("Enter the width of the rectangle 2 = "))

#Calculatig the Area for the two rectangle values

rectanglearea1 = length1 * width1
rectanglearea2 = length2 * width2

#Condition loop for print the value for the rectangle

if (rectanglearea1 > rectanglearea2):
    print("\n The area of rectangle 1 is", rectanglearea1, "which is greater than the area of rectangle 2 is",\
    rectanglearea2)

elif (rectanglearea1 < rectanglearea2) :
    print("\n The area of the rectangle 2 is", rectanglearea2, " which greater than the area of the rectangle 1 is",\
          rectanglearea1)

elif (rectanglearea1 == rectanglearea2):
    print(" \n The area of the rectangle 1 is", rectanglearea1, "which is equal to the area of the rectangle 2 is",\
          rectanglearea2)
else:
    print("\n Please enter the correct values")