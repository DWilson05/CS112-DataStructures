number = int(input("Enter a number Here: "))
# takes number you want to multiply by
i = 0
while True:
    result = number * i
    if number < 0:
        print("The application is quitting")
        break
# if the number is negative the program will end
    if result > 500:
        break
# before the result passes 500 the program will end
    print(f"{number} * {i} = {result}")
# print out variables and result
    i += 1
