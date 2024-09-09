import array
# imports arrays into python

ar = array.array('i', [])
# declares array


def addNumbers():
    while len(ar) < 15:
        number = int(input("Add a integer to the array: "))
        ar.append(number)
# until the array has 15 integers it will keep asking user to add an int


def selectionSort(a):
    start = 0
    for start in range(0, len(a)):
        # Assume the first number is the smallest
        minloc = start  # set min location
        min = a[start]  # set element at the start as min
        # Get the minimum
        for i in range(start + 1, len(a)):  # loop through the numbers after the min
            if a[i] < min:  # check if the current number is less than min
                min = a[i]  # if so, set it as the new min
                minloc = i  # set new min location
        # Flip min with the first one
        a[minloc] = a[start]
        a[start] = min


def binarySearch(s):  # function for the Binary Search, takes a value to find, returns its index.
    l = 0  # low, bottom index
    h = len(ar) - 1  # high, top index
    while l <= h:  # low should be less or equal to high
        m = (l + h) // 2  # find the middle
        if ar[m] == s:  # if the middle index has the value return it
            return m
        elif ar[m] < s:  # if the middle index value is less than the value, move the low above middle, 2nd half
            l = m + 1
        else:  # if the middle index value is more or equal to value, move the high below the middle, 1st half
            h = m - 1
    # if we reach here, then element was not


def appendInt():
    newNumb = int(input("What number would you like to add?"))
    ar.append(newNumb)
    print(f"The new number {newNumb} was added to the end of the array")
# appends users number to end of array


def insertInt():
    newNumb = int(input("What number would you like to add?: "))
    newPos = int(input("Where would you like it to be placed?: "))
    errorCheck(newPos)
    ar.insert(newPos - 1, newNumb)
    print(f"The new number {newNumb} was inserted in the index {newPos}")
# inserts users number at users requested position and error checks if position is valid


def popInt():
    newNumb = int(input("What integer would you like to pop?"))
    if ar.count(newNumb) > 0:
        x = ar.pop(binarySearch(newNumb))
        print(f"The first appearance of {x} was popped")
    else:
        print(f"The number {newNumb} was not found in the array")
# pops the first appearance of the number that the user requested


def removeInt():
    newNumb = int(input("What number would you like to remove?"))
    while True:
        if ar.count(newNumb) > 0:
            ar.remove(newNumb)
        else:
            print(f"The number {newNumb} is no longer in the array")
            break
# removes any appearance of the users number from array


def countInt():
    newNumb = int(input("check how many times this number appears: "))
    print(f"The number {newNumb} was found {ar.count(newNumb)} times in the array")
# counts how many times the users number appears


def viewArray():
    i = 1
    for m in ar:
        print(f"{i}.) {m}")
        i += 1
# prints out numbered list


def searchInt():
    search = int(input("Enter a number to look for: "))
    if ar.count(search) > 0:
        print(f"{search} was first found at location {binarySearch(search)}")
    else:
        print(f"{search} was not found in the array")
# searches for the location of the users number


def errorCheck(i):
    if i <= 0 or i > len(ar):
        print("Enter a valid number")
        menu()
# error checks mainly for the insert function


def menu():
    while True:
        choice = int(input("""
        1. Find value location
        2. Append
        3. Insert
        4. Pop
        5. Remove
        6. Count occurrence
        7. View array
        8. Quit

        Please enter your choice (1-8): """))
        if choice == 1:
            searchInt()
        elif choice == 2:
            appendInt()
        elif choice == 3:
            insertInt()
        elif choice == 4:
            popInt()
        elif choice == 5:
            removeInt()
        elif choice == 6:
            countInt()
        elif choice == 7:
            viewArray()
        elif choice == 8:
            print("All Done")
            break
        else:
            continue


addNumbers()
selectionSort(ar)
viewArray()
menu()
