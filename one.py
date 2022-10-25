
message1 = "Global Variable"

def myFunction():
    print("\nInside myFunction")
    print(message1)
    message2= "Local Variable"
    print(message2)

myFunction()
print(message1)
print(message2)