def checkIfPrime(numberToCheck):
    for i in range(2, numberToCheck):
        if numberToCheck % i == 0:
            return False
    return True