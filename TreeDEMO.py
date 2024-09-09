from TreeModule import BinaryTree


my_tree = BinaryTree()

while True:
    print("\n Binary Search Tree Demo, what do you want to do?")
    print(" 1 = Insert data ")
    print(" 2 = Traverse and print Tree inorder ")
    print(" 3 = Count number of nodes ")
    print(" 4 = Search for an item ")
    print(" 5 = Delete an item ")
    print(" 6 = Exit")
    
    choice = int(input("\n Enter Choice: "))
    if choice == 1:  # Entering new node into a tree
        num = int(input("\n Enter number to add to tree: "))
        my_tree.insert(num)
        print(num, " inserted")
    elif choice == 2:  # Printing all nodes in ascending order
        my_tree.inorder()
    elif choice == 3:  # Count number of nodes
        my_tree.get_count()
    elif choice == 4:  # Search to see if item exists
        x = int(input(" Enter number to search for: "))
        answer = my_tree.find(x)
        if answer:
            print("Found it")
        else:
            print("Not found") 
    elif choice == 5:  # Delete a node
        x = int(input(" Enter number to delete: "))
        answer = my_tree.delete(x)
        if answer is None:
            my_tree.root = None
    elif choice == 6:  # Exit
        print("Exiting.")
        break
    else:
        print("Invalid input, try again.")
