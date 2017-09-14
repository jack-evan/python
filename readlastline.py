# create function to read the last line of a file
def getlastline():
    with open('/home/jnunez/Desktop/testread.txt','r') as file1:
        return (list(file1)[-1])

# set variable to getlastline function and pass into write function
avar = getlastline()

# function to write the last line of a file
def writelastline():
    with open('/home/jnunez/Desktop/testwrite.txt','w') as file2:
        file2.write(avar)

writelastline()



