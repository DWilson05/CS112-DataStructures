number = int(input("Enter a positive Integer: "))
counter = 1
for i in range(0, number + 1):
    if number < 0:
        print("Enter a positive number")
        break
    print(i, end=", ")
    if counter == 5:
        print()
        counter = 0
    counter += 1
