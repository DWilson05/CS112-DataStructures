def triangleProb(n):
    if n == 0:
        return 0
    else:
        return n + triangleProb(n - 1)


def check_positive_V2():
    while True:
        num = int(input("Enter a positive integer (1 - 500): "))
        if 0 <= num <= 500:
            print("The triangle number is ", triangleProb(num), "\n")
        else:
            print("please only enter positive numbers")


check_positive_V2()

