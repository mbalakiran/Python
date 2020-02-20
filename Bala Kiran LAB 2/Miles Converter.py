#Requesting the user to enter the distance in miles
def distanceinmiles():
    enteredmiles = float(input("Please enter the distance in miles: "))
    return enteredmiles
#Converting the miles into kilometers
def kilometerstoconvert(enteredmiles):
    kilometer = enteredmiles / 0.6214
    return kilometer

def main():
    miles = distanceinmiles()                              #Assiging distanceintomiles function to miles
    convertedkilometers = kilometerstoconvert(miles)       #Convereting the kilometers and assiging it

    print(miles, "is convereted into", format(convertedkilometers, ".2f"), "Kilometers")
    #Printing the converted kilometers

main()
