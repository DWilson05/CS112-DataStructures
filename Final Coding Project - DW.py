class Node:
    def __init__(self, new_album, new_artist):  # creates new nodes able to store two inputs
        self.item = new_album    # album input
        self.artist = new_artist    # artist input
        self.ref = None


class Queue:
    # ---------------Create an empty Queue -------------
    def __init__(self):
        self.first = None
        self.last = None

    # --------------- Traverse the Queue  ----------------------
    def traverse_list(self):
        print("Queue: ", end=" ")    # formatting for start
        if self.first is None:    # if nothing is in the queue
            print("Queue is empty")
            return
        else:
            n = self.first    # n is first node
            count = 1
            while n is not None:     # while n does not reach the end
                print(f"{count}.)", f"{n.item} By: {n.artist}", end="   ")  # output & formatting
                n = n.ref     # next node
                count += 1   # increase count for formatting
        print(" ")

        #  ------------- Add to the end ----------------------

    def add(self, new_album, new_artist):  # takes to variables to put into new node
        new_node = Node(new_album, new_artist)   # new node
        if self.first is None:      # if the queue is empty
            self.first = new_node
            self.last = new_node
            return
        self.last.ref = new_node    # changes pointers to insert new node into queue
        self.last = new_node

    #  ------------ Count nodes ---------------------------

    def get_count(self):
        if self.first is None:    # if queue empty return 0
            return 0
        n = self.first
        count = 0
        while n is not None:     # traverse queue
            count = count + 1     # increase count each node
            n = n.ref   # looking at next node
        return count

    # -------------- Pop  ------------------

    def remove(self):
        if self.first is None:    # if empty queue
            print("Queue is empty!")
            return
        x = self.first.item     # get rid of first item in que
        if self.first == self.last:
            self.last = None
        self.first = self.first.ref
        return x


album_queue = Queue()

choice = 0
while choice != 6:   # when choice equals 5 the loop/program will exit
    print("\n------------------------------")   # formatting menu
    print(" Album Listening Queue:\n")
    print(" 1 = Add Album to the Queue ")
    print(" 2 = Play First Album ")
    print(" 3 = Display Album Queue ")
    print(" 4 = Display Queue Count ")
    print(" 5 = Clear Queue ")
    print(" 6 = Exit ")
    print("------------------------------")
    choice = int(input("\n Enter Choice: "))    # asks for user choice according to menu

    if choice == 1:   # add to queue
        album = input("\n Enter Album to Add: ")
        artist = input(" Enter Album's Artist: ")
        album_queue.add(album, artist)    # que takes in album and artist variables
        print(album, "By:", artist, "Added to Queue")
    elif choice == 2:   # remove first element in queue
        first = album_queue.remove()
        print(f"Currently Playing {first}...")
        print(first, "Removed From Queue")
    elif choice == 3:    # Traverse through queue and output
        album_queue.traverse_list()  # calls traverse_list function for queue
    elif choice == 4:   # calls get_count function to display count for que
        number_of_albums = album_queue.get_count()
        print("There are", number_of_albums, "Albums in the Queue")
    elif choice == 5:    # clear queue
        if album_queue.get_count() == 0:    # if the queue is empty it will print
            print("\n The Queue is Empty ")
        for i in range(album_queue.get_count()):   # for the length of the que it will repeat
            album_queue.remove()     # removes first item in queue
            print("\n Albums Removed ")
    elif choice > 6:    # Error checker for user
        print(" You Entered Choice:", choice)
        print(" Please Enter a Number From (1 - 5)")
    elif choice < 1:    # Error checker for user
        print(" You Entered Choice:", choice)
        print(" Please Enter a Number From (1 - 5)")

print("\n------------------------------")
print("          Goodbye! ")
print("------------------------------\n")
