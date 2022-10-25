f = open("MyPythonModules/myfile.txt", "a")
f.write("\nThis is a test")
f.close()

r = open("MyPythonModules/myfile.txt", "r")
for line in r:
    print(line, end="")

r.close()