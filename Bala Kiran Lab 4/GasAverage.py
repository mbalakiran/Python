import matplotlib.pyplot as plt

#open the file
with open('1994_Weekly_Gas_Averages.txt') as weekly_average:

    #Assginig the value for the Weekly Gas
    weekly_gas = weekly_average.readlines()

    # Opening the File
    weekly_gas = [line.rstrip('\n') for line in open('1994_Weekly_Gas_Averages.txt')]

    #Assiging the X Axis
    x = weekly_gas

    list_gas = []
    i = 0
    for i in range(0, 52, 1):
        i += 1
        i = list_gas.append(i)
    y = list_gas #assiging the Y axis to the list

    #Assiging the for the display
    print('x = ', x)
    print('y = ', y)

    #Giving an Title
    plt.title('1994 Weekly Gas Average')

    #Giving lables for the Axis
    plt.xlabel('Weekly Gas Average Values')
    plt.ylabel('Week Number for the year')

    #Chaging the names for adis
    plt.yticks([10, 20, 30, 40, 50], ['Weak10','Weak20','Weak30','Weak40','Weak50'])

    #Assigning the width
    width = 0.8

    #Ploting the graph
    plt.bar(x,y, width, color="y")

    #Poping the graph
    plt.show()