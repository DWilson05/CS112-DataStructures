
stack = []  # declare a new list called stack

choice = 0
while True:  # choice menu
    print("\nWhat do you want to do?")
    print(" 1. Push an item on the stack")
    print(" 2. Pop an item from stack")
    print(" 3. Print out stack")
    print(" 4. Display length of stack")
    print(" 5. Exit")
    choice = int(input(" Choice: "))
    if choice == 1:  # adding data
        x = int(input("\n Enter data to push: "))  # get an integer
        stack.append(x)  # use list append function to add at the end
        print( x, "added to Stack")
    elif choice == 2:  # removing data
        if len(stack)>0:  # as long as the stack has data
            y = stack.pop()  # remove the top element
            print("\n", y, " was popped")
        else:  # empty, nothing to remove
            print("\n Stack is empty")
    elif choice == 3:  # display the stack
        print("\nStack", stack)
    elif choice == 4:  # check stack length using len
        print("\nStack size is ", len(stack))
    elif choice == 5:  # quit by breaking out of the While
        print("\nQuitting, goodbye!")
        break
    else:  # entry is not 1-5
        print("\nInvalid entry, try again.")

                 
print("Goodbye")
