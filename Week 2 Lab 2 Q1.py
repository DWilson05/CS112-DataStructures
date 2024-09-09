print("Miles to Kilometers and Meters.")
number = float(input("How many miles would you like to convert? "))
# asks for original mile number


def milesToMeters():
    return number * 1.609
# stores number of meters


def milesToKil():
    return number * 160934
# stores number of kilometers


def printOutput():
    print(f"{number} miles is {milesToKil()} Kilometers or {milesToMeters()}  Meters.")
# prints out final message while calling both earlier functions

printOutput()
