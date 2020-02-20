#Declaring the calories burned for the minute
calories_burned_per_minute = 4.2

#Condition for loop with in the range defines the values between that range

for minutes in range(10, 31):
    calories_burnt = minutes * calories_burned_per_minute
    if minutes % 5 == 0 : #Takes only that values in the range whose % of 5 is 0
        print("You have burnt ", calories_burnt, "in", minutes, "minutes")
