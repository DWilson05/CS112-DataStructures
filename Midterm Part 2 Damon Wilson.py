class Node:
    def __init__(self, location, coordinates, rating, tags):  # add data for location, coords, rating, and tags
        self.location = location
        self.coordinates = coordinates
        self.rating = rating
        self.tags = tags
        self.ref = None


class LocationProgram:
    # ---------------Create an empty linked list -------------

    def __init__(self):  # store data about the student name
        self.start_node = None

    # --------------- View and print out course  ----------------------

    def view_location(self):  # prints all locations out and data for each node
        if self.start_node is None:
            print(" No coordinates were added\n")
            return
        else:
            n = self.start_node
            while n is not None:  # traverses through each node
                print(f""" {n.location}:
 Coordinates: {n.coordinates}
 Rating: {n.rating} 
 {n.tags}
""")
                n = n.ref

        #  ------------- Insert at start  ----------------------

    def insert_location(self, location, coordinates, rating, tags):  # inserts new node with data
        new_node = Node(location, coordinates, rating, tags)
        new_node.ref = self.start_node
        self.start_node = new_node

        #  ------------- Search for a location  ------------

    def search_location(self, locationName):  # will search for node with location name and show data
        if self.start_node is None:
            print(" No locations have been added to the system")
            return
        n = self.start_node
        while n is not None:
            if n.location == locationName:  # if it matches it will show
                print(f"""{n.location}:
Coordinates: {n.coordinates}
Rating: {n.rating} 
{n.tags}
""")
                return True
            n = n.ref
        print(f" {locationName} was not found, try another")
        return False


# ----------------------- add the location to list -----------------------------

def add_location(location_name):  # add a location to linked list
    coordinate_1 = input("What is coordinate 1: ")  # adds coordinate 1 for tuple
    coordinate_2 = input("What is coordinate 2: ")  # takes coordinate 2 for tuple
    my_tuple = (coordinate_1, coordinate_2)
    rating = int(input("What rating would you like to give the location(1-5): "))
    my_set = set()
    while True:  # will continue to take tags from user
        t = input('Enter new tag (quit to exit): ')
        if t == 'quit':
            break
        else:
            my_set.add(t)
    location_list.insert_location(location_name, my_tuple, rating, my_set)  # adds new node with data


# ----------------------- MAIN -----------------------------
location_list = LocationProgram()  # creates single linked list

choice = 0
while choice != 4:
    print("""
------------------------------------
   ~~ Location Program ~~
------------------------------------

1 = Make a new Entry
2 = Find an entry
3 = View all entries
4 = Exit
""")
    choice = int(input("\n Enter Choice: "))
    if choice == 1:
        userLocation = input("What location would you like to add? ")
        add_location(userLocation)
    elif choice == 2:
        userLocation = input("What location would you like to search for? ")
        location_list.search_location(userLocation)
    elif choice == 3:
        location_list.view_location()
