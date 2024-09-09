import array
# imports arrays into python

ar = array.array('i', [])
# declares array


def addNumbers():
    while len(ar) < 10:
        number = int(input("Add a integer to the array: "))
        ar.append(number)
# until the array has 10 integers it will keep asking user to add an int


def selectionSort(a):
    start = 0
    for start in range(0, len(a)):
        # Assume the first number is the smallest
        minloc = start  # set min location
        min = a[start]  # set element at the start as min
        # Get the minimum
        for i in range(start+1, len(a)):  # loop through the numbers after the min
            if a[i] < min :  # check if the current number is less than min
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


addNumbers()
selectionSort(ar)
print(f"Your array is: {ar[0]}, {ar[1]}, {ar[2]}, {ar[3]}, {ar[4]}, {ar[5]}, {ar[6]}, {ar[7]}, {ar[8]}, {ar[9]}")
search = int(input("Enter a number to look for: "))
print(f"{search} found at location {binarySearch(search)}")
print("All Done")