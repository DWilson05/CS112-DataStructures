import array

a = array.array('i', [])


def addNumbers():
    while len(a) < 5:
        number = int(input("Add a number to the array: "))
        a.append(number)


def displaySum():
    array_Sum = 0
    for m in a:
        array_Sum += m
    return array_Sum


def displayAverage():
    return displaySum() / len(a)


def displaySmallest():
    smallest = a[0]
    for m in a:
        if smallest > m:
            smallest = m
    return smallest


def displayLargest():
    largest = a[0]
    for m in a:
        if largest < m:
            largest = m
    return largest


addNumbers()
print(f"Your array is: {a[0]}, {a[1]}, {a[2]}, {a[3]}, {a[4]}")
print(f"The sum of your array is: {displaySum()}")
print(f"The average of your array is: {displayAverage()}")
print(f"The largest number is: {displayLargest()}")
print(f"The smallest number is: {displaySmallest()}")
print("All Done")
