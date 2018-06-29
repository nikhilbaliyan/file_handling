f=open("R.txt", "w")
for i in range(10):
    line = str(random.randint(1, 100))
    f.write(line)
    print(line)
f.close()
f=open("R.txt", "r")
column=[]
data=f.read()
for line in data:
    column.append(line.split("\t"))
    column.sort()
    print(column)
f.close()