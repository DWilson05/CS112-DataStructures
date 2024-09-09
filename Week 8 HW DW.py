from collections import deque    # imports deque
new_deque = deque()    # create deque


def showQue():    # function to show deque
    print(f"\n    Item Que:")   # formatting
    if new_deque.__len__() == 0:     # if the deque is empty it will tell the user
        print("(The Que is Empty)")
    else:
        for i in new_deque:  # prints each element in deque from left to right
            print(i)


def priority():    # checks priority of the que
    prio = int(input("Enter Priority Level (1-2): "))
    if prio == 1:   # will return one if answer is one
        return 1
    else:
        return 2


choice = 0
while choice != 4:
    print("\n Queue Demo, what do you want to do?")    # formatting and asking for user input
    print(" 1 = Add new job ")
    print(" 2 = Preform next job ")
    print(" 3 = View cued Jobs ")
    print(" 4 = EXIT")

    choice = int(input("\n Enter Choice: "))

    if choice == 1:
        item = int(input("Input Job ID here: "))
        if priority() == 1:
            new_deque.append(item)    # appends item to end of deque
            print(item, "was added to the front of the que")
        else:
            new_deque.appendleft(item)  # appends item to beginning of deque if prio is not one
            print(item, "was added to the que")
    elif choice == 2:
        if len(new_deque) > 0:  # if the deque is not empty it will pop an item off of the end
            job = new_deque.pop()
            print(job, "was preformed")
        else:
            print("The que is empty")   # if que is empty will say it
    elif choice == 3:
        showQue()   # prints out cue

print("\n Goodbye \n")
