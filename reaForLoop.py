f = open("MyPythonModules/myfile.txt", "r")

for line in f:
    print(line, end="")

f.close()