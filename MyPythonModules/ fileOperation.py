f = open("MyPythonModules/myfile.txt", "r")
firstLine = f.readline()
secondLine = f.readline()
print(firstLine)
print(secondLine)

f.close()