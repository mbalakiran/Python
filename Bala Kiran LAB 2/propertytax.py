#Requesting for input for the value of property
def valueofproperty():
    property = float(input("Please enter the value of the property: $ "))
    return property
#Functiion for calculating the assessment value
def assessment(property):
    assessmentofproperty = property * 0.60
    return assessmentofproperty
#Function to calculate the property tax
def calpropertytax(assessmetvalue):
    propertytax = (assessmetvalue / 100) * 0.72
    return propertytax
#Defing the print function where we can print all the values
def printall(actualvalue, assessmentvalue, propertytax):
    print("The actual value of the property entered is: $ ", format(actualvalue, ",.2f"), \
          "\nThe assessment value of the property is: $ ", format(assessmentvalue, ",.2f"),  \
          "\nThe property tax to be paid is: ", format(propertytax, ",.2f"))

def main():
    actualvalue = valueofproperty()                          #assigning valueofproperty function to actualvalue
    assessmentvalue = assessment(actualvalue)                #geting assigning value and actualvalue to assessment value
    propertytax = calpropertytax(assessmentvalue)            #Calculating the property tax value through function
    printall(actualvalue, assessmentvalue, propertytax)      #Printing actual value, assessment value and property tax

main()

