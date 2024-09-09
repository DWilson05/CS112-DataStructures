class Node:
    def __init__(self, data):
        self.item = data
        self.ref = None
        self.next = None
        self.prev = None
        # sets up next, prev, ref, and item commands


class LinkedList:
    # ---------------Create an empty linked list -------------

    def __init__(self):
        self.start_node = None

    # --------------- Traverse the linked list  ----------------------

    def traverse_list(self):
        print("Linked List: ", end=" ")
        if self.start_node is None:     # if list empty list is empty will be returned
            print("List is empty")
            return
        else:
            n = self.start_node     # takes first node
            while True:             # traverses list and prints each node value
                print(n.item, end=" ")
                n = n.next
                if n == self.start_node:        # if back at start loop ends
                    break
        print(" ")

        #  ------------- Insert at start  ----------------------

    def insert_at_start(self, data):
        new_node = Node(data)   # creates new node
        if not self.start_node:     # if there is nothing in list new node is first node
            self.start_node = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:           # else: the new node is inserted and the node orders change
            last_node = self.start_node.prev
            new_node.next = self.start_node
            new_node.prev = last_node
            self.start_node.prev = new_node
            last_node.next = new_node
            self.start_node = new_node

        #  ------------- Insert at end  ----------------------

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            self.start_node.next = self.start_node  # since the list is empty, its next is self
            self.start_node.prev = self.start_node  # its previous is also self
            return
        n = self.start_node
        while n.next is not self.start_node:  # while next node is not the “start” node
            n = n.next  # moving through the list
            n.next = new_node  # add new node before the “start” node
            new_node.prev = n  # previous of the new node
            new_node.next = self.start_node  # next after the new node is the start node
            self.start_node.prev = new_node  # update start node’s previous to the new node

        #  ------------ Insert in middle  ----------------------

    def insert_after_item(self, x, data):
        n = self.start_node
        while n is not self.start_node:
            if n.next == x:     # if next node is desired target
                break
            n = n.next
        if n is None:       # target is not found
            print("Item not in list")
        else:
            new_node = Node(data)
            new_node.next = n.next
            new_node.prev = n
            n.next.prev = new_node

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

    def search_item(self, target):
        if self.start_node is None:
            print(" List has no items")
            return
        n = self.start_node
        if n.item == target:    # item found at start
            print("Found at start")
        else:
            while True:        # loop through nodes if found will end
                if n.item == target:
                    print("Item found")
                    break
                if n.next == self.start_node:   # if reaches start again will end
                    print("Not found")
                    break

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

        # --------------- Return Next ---------------

    def get_next(self, target):
        if self.start_node is None:     # print empty if lis is empty
            print("List is Empty")
            return
        n = self.start_node
        if n.item == target:
            print(f"{n.next.item} is next after {n.item}")
        else:
            while True:    # traverse through nodes and see if the node has target value
                if n.item == target:     # if it finds the target loop will end
                    print(f"{n.next.item} is next after {n.item}")
                    break
                if n.next == self.start_node:     # if it hits the start again the loop ends
                    print("Not found.")
                    break

        # --------------- Return Previous ---------------

    def get_previous(self, target):
        if self.start_node is None:    # print empty if lis is empty
            print("List is Empty")
            return
        n = self.start_node
        if n.item == target:          # if the first node is the first target
            print(f"{n.prev.item} is before {n.item}")
        else:
            while True:             # traverse through nodes and see if the node has target value
                if n.item == target:   # if it finds the target loop will end
                    print(f"{n.prev.item} is before {n.item}")
                    break
                if n.next == self.start_node:     # if it hits the start again the loop ends
                    print("Not found.")
                    break
                n = n.next


# ----------------------- MAIN -----------------------------


my_list = LinkedList()

choice = 0
while choice != 12:
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
    print(" 10 = Return the next value ")
    print(" 11 = Return the previous value ")
    print(" 12 = Exit")
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
        nTarget = int(input(" What number would you like to find the next value for: "))
        my_list.get_next(nTarget)
    elif choice == 11:
        nTarget = int(input(" What number would you like to find the previous value for: "))
        my_list.get_previous(nTarget)

print("\n Goodbye \n")
