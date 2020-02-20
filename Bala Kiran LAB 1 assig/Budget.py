#Declaring all the variables
expenses = "y"
totalexpenses = 0
morebudget = 0
lessbudget = 0

#Requesting for the budget amount which has been allocated for the month

budget = float(input("Please enter the budget which has been allocated for this month(SEK) : "))

#Giving an While loop for adding an expense, if the users enters "Y" he can add an another expense for the month or any
#other key to exit the loop

while expenses == "y":
    expenses = float(input("Please enter an expense: "))          #Adding an expense
    totalexpenses = totalexpenses + expenses                      #Calculating the total Expenses
    expenses = input("If you have more expenses please enter y or any key to quit: ")  #User can enter Y to add and other key to exit

#Calculating the more or less budget to give the value exceed or less used for the month

morebudget = totalexpenses - budget
lessbudget = budget - totalexpenses

#If condition loop where we can print the budget with the condition for exceeded or under or used completed used

if totalexpenses > budget:
    print("You have exceeded your budget for this month by: ", format(morebudget, ",.2f") )
elif budget > totalexpenses:
    print("You have under your budget for this month by: ", format(lessbudget, ",.2f") )
else:
    print("You have exactly used your budget for this month")