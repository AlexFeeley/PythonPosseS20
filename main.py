import matplotlib.pyplot as plt
import numpy as np

def Get_Input():
    # Prompt user to enter a state
    state = input("State: ")

    # Case of input doesn't matter, re-prompts user for input until valid state reached
    # Use Valid-State to help
    while ~Valid_State(state):
        print("Not a valid state! \nA valid state name will look like \"Tennessee\"\nPlease try again:")
        state = input("State: ")

    return state

# Boolean function that returns true if state is in U.S., false if not
def Valid_State(myInput):
    # List of every state in the US
    states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado",
     "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois",
     "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland",
     "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana",
     "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York",
     "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania",
     "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah",
     "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]

    if myInput in states:
        return True
    else:
        return False


def Parse_Data():
    # empty dictionary
    data = {}

    file = "us-counties.csv"
    f = open(file, "rt")

    # skip first line
    f.readline()

    state = Get_Input()

    for line in f:
        if state in line:
            temp = line.split(",")

            # date
            y = temp[0]
            y = y[6:]
            # cases
            z = int(temp[4])

            if y in data:
                data[y] += z
            else:
                data[y] = z
    return data

def Visualize_Data():
    # Create list of all dates from dictionary of data
    data = Parse_Data()
    dates = data.keys()
    cases = data.values()

    axis_font = {'fontname': 'Arial', 'size': '14'}

    plt.bar(dates, cases)
    plt.xticks(fontsize = 8, rotation = 90)
    plt.xlabel("Date", **axis_font)
    plt.show()

def graph_dict(dict,state):
    num_infected = list(dict.values())
    total_infected = []
    temp = 0
    for i in range(0, len(num_infected)):
        temp = temp + num_infected[i]
        total_infected[i] = temp

    plt.plot(total_infected)
    plt.xlabel('Number of Days')
    plt.ylabel('Total Infected Cases in '+state)
    plt.show()

def main():
    Visualize_Data()

main()
