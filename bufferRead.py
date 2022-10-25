inputFile = open("MyPythonModules/myfile.txt", "r")
outputFile = open("MyPythonModules/myfile2.txt", "w")

msg = inputFile.read(4)

while msg != "":
    outputFile.write(msg + "\n")
    msg = inputFile.read(4)

inputFile.close()
outputFile.close()