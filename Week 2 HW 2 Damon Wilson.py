import math
# allows me to use math equations like square root


def triangleProb(n):
    if n == 0:
        return 0
    else:
        return n + triangleProb(n - 1)
# Calculates answer for triangle prob


def check_positive(n):
    if 0 <= n <= 500:
        return True
    else:
        print("Enter a valid number")
        return False
# checks if the number is positive and less than 500


def sqrRootProb(n):
    return math.sqrt(n)
# calculates square root


def powerProb(n):
    h = int(input("By what power: "))
    return math.pow(n, h)
# calculates power of number by chosen amount


def factorialProb(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorialProb(n - 1)
# calculates factorial of number


def yourFunction(n):
    return math.remainder(n, 5)
# calculates number by mod 5


while True:
    choice = int(input("""
    What would you like to do?
    1.) Factorial
    2.) Triangle Number
    3.) Square Root
    4.) Power of
    5.) Your function
    6.) Quit
    
    Enter Here: """))
    # determines choice
    if choice == 1:
        number = int(input("\nEnter a number from (0 - 500): "))
        # takes number from user that will be put into formulas
        if not check_positive(number):
            continue
        # if the answer is not positive or >500 it will not calculate factorial
        print(f"The factorial is {factorialProb(number)}")
    elif choice == 2:
        number = int(input("\nEnter a number from (0 - 500): "))
        if not check_positive(number):
            continue
        print(f"The triangle is {triangleProb(number)}")
    elif choice == 3:
        number = int(input("\nEnter a number from (0 - 500): "))
        if not check_positive(number):
            continue
        print(f"The square root is {sqrRootProb(number)}")
    elif choice == 4:
        number = int(input("\nEnter a number from (0 - 500): "))
        if not check_positive(number):
            continue
        print(f"The answer is {powerProb(number)}")
    elif choice == 5:
        number = int(input("\nEnter a number from (0 - 500): "))
        if not check_positive(number):
            continue
        print(f"My function of your number Mod 5 is {yourFunction(number)}")
    elif choice == 6:
        break
    # will stop the loop if they enter 6
    else:
        print("\nEnter one of the numbers listed above")
    # user selected a number that was not 1-6
