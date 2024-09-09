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


class Stack:
    # ---------------Create an empty linked list -------------

    def __init__(self):
        self.top = None  # empty Stack has no top

    # --------------- Traverse the linked list  ----------------------

    def traverse_list(self):  # linked list traversal
        print("Stack: ", end=" ")
        if self.top is None:  # if the Stack is empty return
            print("Stack is empty")
            return
        else:  # traverse through Stack until the end
            n = self.top
            while n is not None:
                print(n.item, end=" ")
                n = n.ref
        print(" ")

    #  ------------- PUSH  ----------------------

    def Push(self, data):  # add data
        new_node = Node(data)  # make a new node and pass it the data
        new_node.ref = self.top  # new node references previous node
        self.top = new_node  # new node is the new top

    #  ------------ Count nodes ---------------------------

    def get_count(self):  # traverse through the nodes and count them
        if self.top is None:
            return 0
        n = self.top
        count = 0
        while n is not None:
            count = count + 1
            n = n.ref
        return count

    # -------------- Pop  ------------------

    def Pop(self):  # remove the top
        if self.top is None:  # if there is no top stack is empty
            print("Stack is empty!")
            return
        x = self.top.item  # store the top item in x
        self.top = self.top.ref  # item before the top is now the new top
        return x  # return the item that was at the top


# --------------- add item to list #1 ------------------

itemList = []


def addItem():
    item = input("Input a word: ")     # takes input
    if item not in itemList:    # if item is not in list
        itemList.append(item)    # adds to item list
        print("The list:", itemList)
    else:
        print("The Input was already in the list")  # item was already in the list
        print("The list:", itemList)


# --------------- add DOB to dictionary #2 ------------------

def addDOB():
    day = int(input("On what day were you born: "))
    month = int(input("On what month (numerical): "))
    year = int(input("What Year: "))
    birthday = {"Day": day,
                "Month": month,
                "Year": year
                }
    print(f"")
    for x in birthday:   # for each key it will print key and value
        print(f"{x}: {birthday[x]}")


# --------------- add location to linked list #3 ------------------

location_list = LinkedList()


def addLocation():
    zipcode = int(input("Enter Your Zipcode: "))
    state = input("Enter the State: ")
    newTuple = (zipcode, state)   # creates tuple with zip and State
    location_list.insert_at_start(newTuple)     # creates node with tuple
    location_list.traverse_list()    # prints linked list


# --------------- add integers to stacks #4 ------------------

def addIntegers():
    even_stack = Stack()
    odd_stack = Stack()
    while True:
        integer = int(input("Enter a integer (0 to exit): "))
        if integer == 0:
            break
        elif integer % 2 == 0:
            even_stack.Push(integer)   # if even adds to even stack
        else:
            odd_stack.Push(integer)  # if odd adds to odd stack
    even_stack.traverse_list()   # traverse and prints even stack
    odd_stack.traverse_list()    # traverse and prints odd stack


# --------------- add sets to linked list #5 ------------------

def addSets():
    set_list = LinkedList()
    while True:
        my_set = set()
        for i in range(3):    # repeats 3 times
            words = input(" Enter Here: ")
            my_set.add(words)     # takes input and adds to set
        set_list.insert_at_start(my_set)    # inserts set into linked list
        newChoice = input(" Continue: (y/n)")   # asks if they want to continue
        if newChoice == "n":   # breaks if the select n
            break
    set_list.traverse_list()    # traverses set linked list and prints


choice = 0
while choice != 6:
    print("\n Extra Credit Demo Program:")
    print(" 1 = Add input to list ")
    print(" 2 = Enter Birthday ")
    print(" 3 = Enter location ")
    print(" 4 = make odd and even stack ")
    print(" 5 = add sets to linked list ")
    print(" 6 = EXIT ")

    choice = int(input("\n Enter Choice: "))

    if choice == 1:
        addItem()
    elif choice == 2:
        addDOB()
    elif choice == 3:
        addLocation()
    elif choice == 4:
        addIntegers()
    elif choice == 5:
        addSets()

print("\n Goodbye \n")
