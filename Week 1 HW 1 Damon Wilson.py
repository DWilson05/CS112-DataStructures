print("""
Hello! Get excited for the Pythoniers!!!""")
standing = 25
premium = 20
total = 0
# Variable to Keep track of standing tickets, premium tickets, and the price

while (standing > 0) | (premium > 0):
    # While there are standing or premium tickets the loop will continue
    ticketType = int(input("\nWould you like tickets for 1 – Standing Room or 2 – Premium Seating?: "))
    ticketOrder = int(input("How many tickets would you like?: "))
    # Tracks what kind of ticket and how many the person wants each order
    if (ticketType == 1) & (standing > 0) & (ticketOrder <= standing):
        # depending on the type of ticket, how many are left, and if the order is greater than the amount left
        greetOrder = int(input("How many 'meet and greet' packages would you like?: "))
        if greetOrder > ticketOrder:
            print("You do not have enough people for that many packages")
            continue
            # if the person orders too many meet and greet packages the order will not go through
        total = (ticketOrder * 5) + (greetOrder * 20)
        # calculates total cost per order
        print(f"Great! you spent ${total} for {ticketOrder} Premium Seating ticket(s) "
              f"with {greetOrder} 'meet and greet' package(s)")
        standing -= ticketOrder
        # updates amount of standing tickets left
        print(f"Remaining tickets: {standing} – Standing Room, {premium} – Premium Seating")

    elif (ticketType == 2) & (premium > 0) & (ticketOrder <= premium):
        greetOrder = int(input("How many 'meet and greet' packages would you like?: "))
        if greetOrder > ticketOrder:
            print("You do not have enough people for that many packages")
            continue
        total = (ticketOrder * 7) + (greetOrder * 20)
        print(f"Great! you spent ${total} for {ticketOrder} Premium Seating ticket(s)"
              f" with {greetOrder} 'meet and greet' package(s)")
        premium -= ticketOrder
        # updates amount of premium tickets left
        print(f"Remaining tickets: {standing} – Standing Room, {premium} – Premium Seating")
    else:
        print("The order is not available")
        # user entered a wrong ticket number, ordered too many tickets, or none were left for that section
print("\nLooks like we are all out of tickets!")
# loop will end when all the tickets are sold
