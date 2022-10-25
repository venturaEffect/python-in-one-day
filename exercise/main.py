
try:

    from myPythonFunctions import getUserPoint, generateQuestion, updateUserPoints

    userName = input("Please enter your name: ")
    score = getUserPoint(userName)
    userScore = int(score)

    if (score == "-1"):
        newUser = True
        userScore = 0
    else:
        newUser = False

    userChoice = "y"
    while userChoice == "y":
        generateQuestion()
        userScore += generateQuestion()
        userChoice = input("Do you want to continue? (y/n) ")

    updateUserPoints(newUser, userName, userScore)

except ValueError as e:
    print(e)