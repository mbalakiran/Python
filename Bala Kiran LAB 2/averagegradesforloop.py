#Calculate average by assiging the total divided by 5
def calc_average(total):
    return total / 5

#Grading scale given accondingly
def determine_score(grade):
    if (grade > 0 and grade < 60):
        return "F"
    elif grade < 70:
        return "D"
    elif grade < 80:
        return "C"
    elif grade < 90:
        return "B"
    elif grade <= 100:
        return "A"
    else:
        return "Please enter the correct grades!"

#Entering the 5 test scores with the for loop condition
scores = []
for s in range(1, 6): #Giving the range for the numbers
    score = float ( input("Enter the score {0}: \n" .format(s))) #asking for the input
    print("The grade for the score is: ", determine_score(score)) #printing the individual score and grade
    scores.append(score) #appending the score

def main():
    total = sum(scores)              #assging the sum of scores to total
    avg = calc_average(total)        #Calculating the average by calling calc averge function
    s_grade = determine_score(avg)   # Determining the grade by asiging the avg to grade function

    print("Average score is: ", format(avg, ".2f"), "And the grade for the average score is:", s_grade)
    #Printing the average for the scores

main()