class Node:  # define what a node is
    def __init__(self, data):
        self.item = data  # a node has data
        self.ref = None  # a node references next node


class Stack:
    # ---------------Create an empty linked list -------------

    def __init__(self):
        self.top = None  # empty Stack has no top

    # --------------- Traverse the linked list  ----------------------

    def traverse_list(self):  # linked list traversal
        if self.top is None:  # if the Stack is empty return
            print("Text is empty")
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

    # -------------- Pop ------------------

    def Pop(self):  # remove the top
        if self.top is None:  # if there is no top stack is empty
            print("Text is empty!")
            return
        x = self.top.item  # store the top item in x
        self.top = self.top.ref  # item before the top is now the new top
        return x  # return the item that was at the top


def view_text():
    print("Current Text: ")
    temp_stack = Stack()  # creates new temp stack
    current = main_stack.top  # variable current equals main stack top value
    while current is not None:  # while it is not the last
        temp_stack.Push(current.item)  # add the current to the temp stack
        current = current.ref
    temp_stack.traverse_list()  # it displays the main stack in the reverse order


def edit_text():
    view_text()   # views old text
    print("Enter new text: ")
    new_text = input("")    # takes input and adds to main stack
    main_stack.Push(new_text)


def undo():
    deleted = main_stack.Pop()  # popped from main stack
    print("Undoing: ", deleted)
    deleted_stack.Push(deleted)  # added to deleted stack


def redo():
    redone = deleted_stack.Pop()  # top value is popped from deleted
    print("Redoing: ", redone)
    main_stack.Push(redone)   # added back ot main stack


main_stack = Stack()  # declare a new stack my_stack of class Stack
deleted_stack = Stack()

while True:  # choice menu
    print("\nWhat do you want to do?")
    print(" 1. Edit Text")
    print(" 2. Undo")
    print(" 3. Redo")
    print(" 4. View Text")
    print(" 5. Exit")
    choice = int(input(" Choice: "))

    if choice == 1:  # adding data
        edit_text()
    elif choice == 2:  # removing data and adding to second stack
        undo()
    elif choice == 3:  # redoes decision and adds back to main
        redo()
    elif choice == 4:  # views text
        view_text()
    elif choice == 5:  # quit by breaking out of the While
        break
    else:  # entry is not 1-5
        print("\nInvalid entry, try again.")

print("\n Goodbye \n")
