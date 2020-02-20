#Initialization the Variables
name : "0"
# getting input from the user and assigning it to Name
name = str(input("Please enter your name: "))
#Requesting the user for the values of Height and Weight
height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kg: "))

# the formula for calculating bmi

bmi = weight/(height*height)

#Printing the value of the BMI with the condition result for the condition loop

print(name, "your BMI value is:", bmi, "and your condition is: ", end='')

#conditions loop for finding the BMI results
if ( bmi < 18.5):
   print("Underweight")

elif ( bmi >= 18.5 and bmi <= 24.99):
   print("Normal Weight")

elif ( bmi >= 25 and bmi < 29.99):
   print("Overweight")

elif ( bmi >=30):
   print("Obesity")

