class Node:
    def __init__(self, data):
        self.item = data
        self.ref = None


class Queue:
    # ---------------Create an empty Queue -------------
    def __init__(self):
        self.first = None
        self.last = None

    # --------------- Traverse the Queue  ----------------------
    def traverse_list(self):
        print("Queue: ", end = " ")
        if self.first is None:
            print("Queue is empty")
            return
        else:
            n = self.first
            while n is not None:
                print(n.item, end =" " )
                n = n.ref
        print(" ")

        #  ------------- Add to the end ----------------------

    def add(self, data):
        new_node = Node(data)
        if self.first is None:
            self.first = new_node
            self.last = new_node
            return
        self.last.ref = new_node
        self.last = new_node

    #  ------------ Count nodes ---------------------------

    def get_count(self):
        if self.first is None:
            return 0
        n = self.first
        count = 0
        while n is not None:
            count = count+1
            n = n.ref
        return count

    # -------------- Pop  ------------------

    def remove(self):
        if self.first is None:
            print("Queue is empty!")
            return
        x = self.first.item
        if self.first == self.last:
            self.last = None
        self.first = self.first.ref
        return x
 
