class Node:
    def __init__(self, data):
        self.item = data
        self.ref = None


class LinkedList:
    # ---------------Create an empty linked list -------------

    def __init__(self):
        self.start_node = None

    # --------------- Traverse the linked list  ----------------------

    def traverse_list(self):
        print("Linked List: ", end=" ")
        if self.start_node is None:
            print("List is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item, end=" ")
                n = n.ref
        print(" ")

        #  ------------- Insert at start  ----------------------

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.ref = self.start_node
        self.start_node = new_node

        #  ------------- Insert at end  ----------------------

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return
        n = self.start_node
        while n.ref is not None:
            n = n.ref
        n.ref = new_node

        #  ------------ Insert in middle  ----------------------

    def insert_after_item(self, x, data):
        n = self.start_node
        print(n.ref)
        while n is not None:
            if n.item == x:
                break
            n = n.ref
        if n is None:
            print("Item not in list")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

        #  ------------ Count nodes ---------------------------

    def get_count(self):
        if self.start_node is None:
            return 0
        n = self.start_node
        count = 0
        while n is not None:
            count = count + 1
            n = n.ref
        return count

        #  ------------- Search List for an item  ------------

    def search_item(self, x):
        if self.start_node is None:
            print(" List has no items")
            return
        n = self.start_node
        while n is not None:
            if n.item == x:
                print("Item found")
                return True
            n = n.ref
        print("Item not found")
        return False

        # -------------- Delete first item  ------------------

    def delete_at_start(self):
        if self.start_node is None:
            print("Linked list is empty!")
            return
        self.start_node = self.start_node.ref

        # -------------- Delete last item  --------------------

    def delete_at_end(self):
        if self.start_node is None:
            print("Linked list is empty!")
            return
        n = self.start_node
        while n.ref.ref is not None:
            n = n.ref
        n.ref = None

        # --------------- Delete a certain item ---------------

    def delete_element(self, x):
        if self.start_node is None:
            print("Linked list is empty!")
            return
        if self.start_node.item == x:
            self.start_node = self.start_node.ref
            return
        n = self.start_node
        while n.ref is not None:
            if n.ref.item == x:
                break
            n = n.ref
        if n.ref is None:
            print("item not found")
        else:
            n.ref = n.ref.ref

        # --------------- Sum ---------------

    def find_sum(self):
        if self.start_node is None:   # if the list is empty will return 0
            return 0
        n = self.start_node     # starts at beginning node
        sum = 0
        while n is not None:   # traverses through each node until end
            sum += n.item   # adds up each value stored in each node
            n = n.ref     # changes to following node
        return sum  # total of the values in the nodes

        # --------------- Average ---------------

    def find_avg(self):
        if self.start_node is None:
            return 0
        count = self.get_count()   # calls count function to get count of nodes
        sum = self.find_sum()    # calls sum function to get sum of values
        return sum / count   # returns sum/count to get average

        # --------------- Min ---------------

    def find_min(self):
        if self.start_node is None:
            return 0
        n = self.start_node
        smallest = n.item   # sets the smallest as the first node amount
        while n is not None:
            if smallest > n.item:   # checks though each node if the item is smaller than the maximum
                smallest = n.item
            n = n.ref
        return smallest

        # --------------- Max ---------------

    def find_max(self):
        if self.start_node is None:   # if list is empty it will return 0
            return 0
        n = self.start_node
        maximum = n.item    # sets the maximum as the first node amount
        while n is not None:
            if maximum < n.item:   # checks though each node if the item is greater than the maximum
                maximum = n.item
            n = n.ref
        return maximum

        # --------------- Count ---------------

    def find_count(self, b):
        if self.start_node is None:   # if list is empty it will return 0
            return 0
        n = self.start_node    # will start at starting node
        count = 0
        while n is not None:   # traverse through each node until end
            if n.item == b:   # if the node equals the desired numer the count will rise
                count += 1
            n = n.ref  # will go to next node
        return count  # returns number of times that the node equaled the number


# ----------------------- MAIN -----------------------------


my_list = LinkedList()

choice = 0
while choice != 15:
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
    print(" 10 = Sum of the data ")
    print(" 11 = Average of the data ")
    print(" 12 = Minimum value in list ")
    print(" 13 = Maximum value in list ")
    print(" 14 = Count occurrences of a given value ")
    print(" 15 = Exit")
    choice = int(input("\n Enter Choice: "))

    if choice == 1:
        num = int(input("\n Enter number to add to linked list: "))
        my_list.insert_at_start(num)
        print(num, " inserted at the beginning")
    elif choice == 2:
        num = int(input("\n Enter number to add to linked list: "))
        my_list.insert_at_end(num)
        print(num, " inserted at the end")
    elif choice == 3:
        num = int(input("\n Enter number to add to linked list: "))
        x = int(input(" Put it after which number? "))
        my_list.insert_after_item(x, num)
        print(num, " inserted at the end")
    elif choice == 4:
        my_list.traverse_list()
    elif choice == 5:
        x = my_list.get_count()
        print("List has ", x, " items now")
    elif choice == 6:
        x = int(input(" Enter number to search for: "))
        my_list.search_item(x)
    elif choice == 7:
        my_list.delete_at_start()
        print("Removed first item")
    elif choice == 8:
        my_list.delete_at_end()
        print("Removed last item")
    elif choice == 9:
        x = int(input(" Enter number to delete: "))
        my_list.delete_element(x)
        print("Removed it (if found)")
    elif choice == 10:
        print("The Sum is: ", my_list.find_sum())
    elif choice == 11:
        print("The Average of the list is: ", my_list.find_avg())
    elif choice == 12:
        print("The Minimum of the list is: ", my_list.find_min())
    elif choice == 13:
        print("The Maximum of the list is: ", my_list.find_max())
    elif choice == 14:
        s = int(input("Count how many times this number appears: "))
        print(f"{s} appears {my_list.find_count(s)} times")

print("\n Goodbye \n")
