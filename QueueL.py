
queue = []

choice = 0
while choice != 5:
    print("\nWhat do you want to do?")
    print(" 1. Add an item to the end of the queue")
    print(" 2. Remove first item in queue")
    print(" 3. Print out queue")
    print(" 4. Display length of queue")
    print(" 5. Exit")
    choice = int(input(" Choice: "))
    if choice == 1:
        x = int(input("\n Enter data to add: "))
        queue.append(x)
        print(x, "added to queue")
    elif choice == 2:
        if len(queue) > 0:
            y = queue.pop(0)
            print("\n", y, " was removed from queue")
        else:
            print("\n queue is empty")
    elif choice == 3:
        print("\nqueue", queue)
    elif choice == 4:
        print("\nqueue size is ", len(queue))

print("Goodbye")
