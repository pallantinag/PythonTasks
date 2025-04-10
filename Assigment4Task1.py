try:
    file=open('sample.txt', 'r')
    filelines = list(file.readlines())
    print("Reading file content: "+file.name)
    print("Line 1: "+ filelines[0])
    print("Line 2: "+ filelines[1])
    file.close()
except FileNotFoundError:
    print("Error: The file \'sample.txt\' was not found.")

