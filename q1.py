with open('nikhil.txt') as f:
    data = f.readlines()
lastline = data[-1]
n = int(input("enter the number of lines "))
tail = data[-n:]