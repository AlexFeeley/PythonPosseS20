# empty dictionary
dict = {}

# skip first line
header = f.readline()

for line in f:
    temp = line.split(",")
    if temp[3] == state:
        #date
        x = temp[0]
        #cases
        y = int(temp[4])
    if x in dict:
        dict[x] += y
    else:
        dict[x] = y
