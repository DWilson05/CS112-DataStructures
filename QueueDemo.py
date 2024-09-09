
from QueueModule import Queue

my_queue = Queue()

choice = 0
while choice != 5:
    print("\n Queue Demo, what do you want to do?")
    print(" 1 = Add to the end ")
    print(" 2 = Remove the first node ")
    print(" 3 = Print Queue")
    print(" 4 = Count number of elements inQueue ")
    print(" 5 = Exit ")
    choice = int(input("\n Enter Choice: "))

    if choice == 1:
        num = int(input("\n Enter number to add: "))
        my_queue.add(num)
        print(num, " added to queue")
    elif choice == 2:
        x = my_queue.remove()
        print(x,  " was removed ")
    elif choice == 3:
        my_queue.traverse_list()
    elif choice == 4:
        x = my_queue.get_count()
        print("Queue has ", x, " items now")


print("\n Goodbye \n")
