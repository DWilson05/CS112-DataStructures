               
from LinkedListmodule import LinkedList


My_List = LinkedList()

choice = 0
while choice != 10:
    print("\n LinkedList Demo, what do you want to do?")
    print(" 1 = Insert at beginning ")
    print(" 2 = Insert at the end ")
    print(" 3 = Insert in the middle")
    print(" 4 = Traverse and print List ")
    print(" 5 = Count number of nodes ")
    print(" 6 = Search for an item ")
    print(" 7 = Delete the first node ")
    print(" 8 = Delete the last node ")
    print(" 9 = Delete a particular node ")
    print(" 10 = Exit")
    choice = int(input("\n Enter Choice: "))

    if choice==1:
        num = int(input("\n Enter number to add to linked list: "))
        My_List.insert_at_start(num)
        print( num , " inserted at the beginning")
    elif choice==2:
        num = int(input("\n Enter number to add to linked list: "))
        My_List.insert_at_end(num)
        print( num , " inserted at the end")
    elif choice==3:
        num = int(input("\n Enter number to add to linked list: "))
        x = int(input(" Put it after which number? "))
        My_List.insert_after_item(x,num)
        print( num , " inserted at the end")
    elif choice==4:
        My_List.traverse_list()
    elif choice==5:
        x = My_List.get_count()
        print("List has ",x, " items now")
    elif choice ==6:
        x = int(input(" Enter number to search for: "))
        My_List.search_item(x)
    elif choice==7:
        My_List.delete_at_start()
        print("Removed first item")
    elif choice==8:
        My_List.delete_at_end()
        print("Removed last item")
    elif choice==9:
         x = int(input(" Enter number to delete: "))
         My_List.delete_element(x)
         print("Removed it (if found)")
        
        
        
      
print("\n Goodbye \n")
