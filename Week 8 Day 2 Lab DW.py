from collections import deque    # imports deque
new_deque = deque()    # create deque


def showQue():    # function to show deque
    print(f"\n    Item Que:")   # formatting
    if new_deque.__len__() == 0:     # if the deque is empty it will tell the user
        print("(The Que is Empty)")
    else:
        for i in new_deque:  # prints each element in deque from left to right
            print(i)


choice = 0
while choice != 8:
    print("\n Queue Demo, what do you want to do?")    # formatting and asking for user input
    print(" 1 = Add to the right ")
    print(" 2 = Add to the left ")
    print(" 3 = pop item to the right ")
    print(" 4 = pop item to the left ")
    print(" 5 = Reverse")
    print(" 6 = Rotate ")
    print(" 7 = Clear ")
    print("8 = Quit ")

    choice = int(input("\n Enter Choice: "))

    if choice == 1:
        item = input("Input Here: ")
        new_deque.append(item)    # appends item to end of deque
        showQue()    # calls show que function
    elif choice == 2:
        item = input("Input Here: ")
        new_deque.appendleft(item)    # appends item to beginning of deque
        showQue()
    elif choice == 3:
        if len(new_deque) > 0:  # if the deque is not empty it will pop an item off of the end
            new_deque.pop()
        showQue()
    elif choice == 4:
        if len(new_deque) > 0:    # if the deque is not empty it will pop off the start
            new_deque.popleft()
        showQue()
    elif choice == 5:
        new_deque.reverse()   # reverses the deque
        showQue()
    elif choice == 6:
        steps = int(input("Input steps to rotate: "))
        new_deque.rotate(steps)  # rotates deque by user input of steps
        showQue()
    elif choice == 7:
        new_deque.clear() # clears the deque
        showQue()

print("\n Goodbye \n")
