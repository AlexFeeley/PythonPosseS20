from matplotlib import rcParams
rcParams['font.family']='sans-serif'
rcParams['font.sans-serif']=['Verdana']
import matplotlib.pyplot as plt
import numpy as np

# String function that returns the state for the data that is to be visualized
def Get_Input():
    # Prompt user to enter a state
    state = input("State: ").lower()

    # Case of input doesn't matter, re-prompts user for input until valid state reached
    while not Valid_State(state):
        print("Not a valid state! Please try again:")
        state = input("State: ")

    return state


# Boolean helper function that returns true if state is in U.S., false if not
def Valid_State(myInput):
    # List of every state in the US
    states = ["alabama", "alaska", "arizona", "arkansas", "california", "colorado",
              "connecticut", "delaware", "florida", "georgia", "hawaii", "idaho", "illinois",
              "indiana", "iowa", "kansas", "kentucky", "louisiana", "maine", "maryland",
              "massachusetts", "michigan", "minnesota", "mississippi", "missouri", "montana",
              "nebraska", "nevada", "new hampshire", "new jersey", "new mexico", "new york",
              "north carolina", "north dakota", "ohio", "oklahoma", "oregon", "pennsylvania",
              "rhode island", "south carolina", "south dakota", "tennessee", "texas", "utah",
              "vermont", "virginia", "washington", "west virginia", "wisconsin", "wyoming"]

    if myInput in states:
        return True
    else:
        return False


# Function to parse csv data and put one state's cases and dates into a dictionary
def Parse_Data(state):
    # empty dictionary
    data = {}

    file = "us-counties.csv"
    f = open(file, "rt")

    # skip first line
    f.readline()

    for line in f:
        if state in line.lower():
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


# Graphs data
def Visualize_Data(data, state):
    # Create list of all dates from dictionary of data
    dates = data.keys()
    cases = data.values()
    plt.bar(dates, cases, align = "center", color = "green") # Put data into bar graph
    plt.xticks(fontsize=7, rotation=90) # Format X-Axis Label
    plt.yticks(fontsize=10)
    plt.xlabel("Date") # X-Axis Label
    plt.ylabel("Number of Cases") # Y-Axis Label
    plt.suptitle("Number of Covid-19 Cases in " + state.upper()) # Title
    plt.title("Total Number of Covid-19 Cases in " + state.upper() + ": " + str(sum(data.values())) , fontsize=12) # Subtitle

    plt.show()


def main():
    state = Get_Input() # Get state for covid-19 data to be visualized
    data = Parse_Data(state) # Put that state's data into a dictionary
    Visualize_Data(data, state) # Visualize that data


main()
