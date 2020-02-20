#Initialization the variables
videos = 0
points = 0
name = "0"
#Requesting for the name
name = str(input("Please Enter your name: "))
#Requesting for the Videos purchased for the month
videos = int(input('Enter the number of videos that has been purchased for this month: '))
#Entering into the Condition loop
if videos == 0:
    points = 0
elif videos == 1:
    points = 5
elif videos == 2:
    points = 15
elif videos == 3:
    points = 30
elif videos >= 4:
    points = 60
else:
    print("Wrong number")
#Print the vale of the points which have been earned for the month
print(name,"the number of point awarded for this month are: ", points)
