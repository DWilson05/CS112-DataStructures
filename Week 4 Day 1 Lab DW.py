import random
# imports random for shuffle feature

intList = []
# initial list for adding numbers to


def addNumbers():
    while len(intList) < 10:
        number = int(input("Add a integer to the array: "))
        intList.append(number)
# will add 10 of user's integers to initial list


def removeDup():
    for i in sortedList:
        if sortedList.count(i) > 1:
            sortedList.remove(i)
# will check each index in the sorted list to see if it has duplicates
# if it does it will delete


addNumbers()
print(intList)
print(f"The sum of list is {sum(intList)}")
print(f"The min of list is {min(intList)}")
print(f"The max of list is {max(intList)}")
print(f"The length of list is {len(intList)}")

random.shuffle(intList)
print(f"Shuffled list: {intList}")
# will shuffle the initial list and output result

sortedList = sorted(intList)
print(f"Sorted list: {sortedList}")
# creates a new list for the sorted version of the initial list

removeDup()
print(f"Sorted list without Duplicates: {sortedList}")
# removes duplicates from the sorted list and outputs
