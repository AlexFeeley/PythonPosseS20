# empty dictionary
dict = {}
file = "us-counties.csv"
f = open(file, "rt")

# skip first line
header = f.readline()

for line in f:
    temp = line.split(",")

    #state
    x = temp[2]
    #date
    y = temp[0]
    #cases
    z = int(temp[4])

    if x in dict:
        if y in dict[x]:
            dict[y] += z
        else:
            dict[x] = {y,z}
    else:
        dict = { x: {y, z}}


print(dict)