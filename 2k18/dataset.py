def readfile(input):
    with open(input, 'r') as reader:
        test = reader.readline()
    return test




def writefile(output):
    with open(output, 'w') as writer:
        writer.write("Tested")