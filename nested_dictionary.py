# empty dictionary
dict = {}
file = "us-counties.csv"
f = open(file, "rt")

# skip first line
header = f.readline()

state = input("State: ")

for line in f:
    if state in line:
        temp = line.split(",")

        # state
        x = temp[2]
        # date
        y = temp[0]
        # cases
        z = int(temp[4])

        if y in dict:
            dict[y] += z
        else:
            dict[y] = z

print(dict)
