inputFile = open("myimage.jpg", "rb")
outputFile = open("myimage2.jpg", "wb")

msg = inputFile.read(1024)

while msg != "":
    outputFile.write(msg)
    msg = inputFile.read(1024)

inputFile.close()
outputFile.close()