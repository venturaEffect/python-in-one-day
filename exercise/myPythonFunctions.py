from calendar import c
from random import randint
from os import remove, rename

def getUserPoint(userName):
    f = open("./exercise/userScores.txt", "r")
    try:
        for line in f:
            content = line.split(", ")
            if(content[0] == userName):
                f.close()
                return content[1]
            else:
                f.close()
                return "-1"    
    except IOError:
        print("Error: File not found.")
        f = open("./exercise/userScores.txt", "w")
        f.close()
        return "-1"


def updateUserPoints(newUser, userName, score):
    if(newUser):
        f = open("exercise/userScores.txt", "a")
        user = userName + ", " + str(score)
        f.write(user)
        f.close()
    else:
        g = open("exercise/userScores.tmp", "w")
        f = open("exercise/userScores.txt", "r")
        for line in f:
            content = line.split(", ")
            if(content[0] == userName):
                score = content[1] + score
                g.write("%s, %s", userName, score)
        f.close()
        g.close()
        remove("exercise/userScores.txt")
        rename("exercise/userScores.tmp", "exercise/userScores.txt")



def generateQuestion():

    operandList = [0, 1, 2, 3, 4]
    operatorList = ["", "", "", "", ""]
    operatorDict = {1: "+", 2: "-", 3: "*", 4: "**", 5: "/"}

    for i in range(0, 5):
        operandList[i] = randint(1, 9)

    operatorClone = []
    for i in range(0, 4):
        operatorList[i] = operatorDict[randint(1, 5)]
        operatorClone.append(operatorList[i])
        for j in range(0, i):
            if(operatorClone[j] == "**"):
                operatorList[i] = operatorDict[randint(1, 3)]

    while -1: 
        
        questionString = ""

        result = 50001

        while result > 50000 or result < -50000:

            for i in range(0, 5):
                if(i == 0):
                    questionString += str(operandList[i]) + operatorList[i] + "("
                elif(i == 3):
                    questionString += str(operandList[i]) + ")" + operatorList[i]
                elif(i == 4):
                    questionString += str(operandList[i])
                else:
                    questionString += str(operandList[i]) + operatorList[i]

            result = round(eval(questionString))

        questionString = questionString.replace("**", "^")
        question = input("What is the result of %s? " % questionString)

        try:
            if(int(question) == result):
                print("Correct!")
                return 1
            else:
                print("The correct answer is %s" % result)
                return 0
        except ValueError:
            print("Please enter a number.")
            return 0

