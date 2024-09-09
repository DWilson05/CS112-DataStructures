               
from StackModule import Stack

my_stack = Stack() # declare a new stack my_stack of class Stack

while True:  # choice menu
    print("\nWhat do you want to do?")
    print(" 1. Push an item on the stack")
    print(" 2. Pop an item from stack")
    print(" 3. Print out stack")
    print(" 4. Display length of stack")
    print(" 5. Exit")
    choice = int(input(" Choice: "))

    if choice==1:  # adding data
        num = int(input("\n Enter number to push: "))
        my_stack.Push(num)  # call Stack class function Push to add data
        print( num, " pushed on stack")
    elif choice==2:  # removing data
        x = my_stack.Pop()  # call Stack class function Pop to remove data
        print(x, " was popped out")
    elif choice==3:  # display the Stack
        my_stack.traverse_list()  # call Stack class function traverse list to display
    elif choice==4:  # count nodes in the Stack
        x = my_stack.get_count()  # call Stack class function get count
        print("Stack has ", x, " items now")
    elif choice == 5:  # quit by breaking out of the While
        break
    else:  # entry is not 1-5
        print("\nInvalid entry, try again.")
         
      
print("\n Goodbye \n")
