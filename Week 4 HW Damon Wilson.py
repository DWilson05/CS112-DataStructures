controllersP = {  # controller prices
    "PS4": 40.0,
    "PS5": 70.0,
    "Switch": 65.99,
    "Xbox One": 59.99
}

controllersS = {  # controller stock
    "PS4": 4,
    "PS5": 6,
    "Switch": 6,
    "Xbox One": 10
}

videoGamesP = {  # video game prices
    "Splatoon 3": 39.99,
    "Tears of the Kingdom": 59.99,
    "Baldur's Gate 3": 60.99,
    "Skyrim": 19.99
}

videoGamesS = {  # video game stock
    "Splatoon 3": 3,
    "Tears of the Kingdom": 10,
    "Baldur's Gate 3": 12,
    "Skyrim": 9
}

merchP = {  # merch prices
    "Mario poster": 5.99,
    "Goomba plush": 19.99,
    "Assorted pins": 9.99,
    "T-shirts": 14.99
}

merchS = {  # merch stock
    "Mario poster": 4,
    "Goomba plush": 15,
    "Assorted pins": 34,
    "T-shirts": 41
}

prices = {  # prices by type
    "controllers": controllersP,
    "videoGames": videoGamesP,
    "merch": merchP
}

stock = {  # stock by type
    "controllers": controllersS,
    "videoGames": videoGamesS,
    "merch": merchS
}
# ^^^ Base dictionaries provided by teacher


def addItem():    # adds specific item user wants to dictionaries
    choice = int(input("""
What type of item would you like to add?
1.) Controller
2.) Video Game
3.) Merch
Please Enter (1-3) Here: """))
    newName = (input("What is the name of the new item? "))
    newStock = int(input("How much stock of the new item is available? "))
    newPrice = int(input("What is the price of the new item? "))
    if choice == 1:    # choice of choosing controller vs video game vs merch
        controllersP[newName] = newPrice    # adds new price and controller name to controllers dictionaries
        controllersS[newName] = newStock    # adds new stock number and controller name to controllers dictionaries
        # Sets the key and value for both the stock and price dictionaries
    elif choice == 2:
        videoGamesP[newName] = newPrice
        videoGamesS[newName] = newStock
    elif choice == 3:
        merchP[newName] = newPrice
        merchS[newName] = newStock
    else:    # if the user inputs other that (1-3) it will recall function
        print("Input a Correct Value")
        addItem()
    print(f"{newName} was added with {newStock} for ${newPrice}")


def removeItem():    # removes specific item user wants from dictionaries
    choice = int(input("""
What type of item would you like to remove?
1.) Controller
2.) Video Game
3.) Merch
Please Enter (1-3) Here: """))
    newName = input("What is the name of the item? ")
    if choice == 1:
        errorCheck(newName, 1)    # function to check if the key value newName(user imputed) is in controllers
        controllersP.pop(newName)     # key value with the user imputed name will be removed from both price and stock
        controllersS.pop(newName)
    elif choice == 2:
        errorCheck(newName, 2)
        videoGamesP.pop(newName)
        videoGamesS.pop(newName)
    elif choice == 3:
        errorCheck(newName, 3)
        merchP.pop(newName)
        merchS.pop(newName)
    else:    # user did not input(1-3)
        print("Input a Correct Value")
        removeItem()
    print(f"{newName} was removed from the catalogue")


def lowerStock():    # lower stock value of user specified key
    choice = int(input("""
What type of item would you like to lower its stock?
1.) Controller
2.) Video Game
3.) Merch
Please Enter (1-3) Here: """))
    newName = input("What is the name of the item? ")
    lower = int(input("How much would you like to lower it by? "))
    if choice == 1:
        errorCheck(newName, 1)    # function to check if the key value newName(user imputed) is in controllers
        if lower > controllersS[newName]:    # if the user asks to lower the stock more than is possible
            print("You do not have enough stock available to remove this much")
            menu()
        controllersS[newName] -= lower    # lowers stock value for controller's specific key
    elif choice == 2:
        errorCheck(newName, 2)
        if lower > videoGamesS[newName]:
            print("You do not have enough stock available to remove this much")
            menu()
        videoGamesS[newName] -= lower
    elif choice == 3:
        errorCheck(newName, 3, )
        if lower > merchS[newName]:
            print("You do not have enough stock available to remove this much")
            menu()
        merchS[newName] -= lower
    else:
        print("Input a Correct Value")
        lowerStock()
    print(f"{newName} was lowered by {lower}")


def addStock():    # add to stock value of user specified key
    choice = int(input("""
What type of item would you like to increase its stock?
1.) Controller
2.) Video Game
3.) Merch
Please Enter (1-3) Here: """))
    newName = input("What is the name of the item? ")
    higher = int(input("How much would you like to increase it by? "))
    if choice == 1:
        errorCheck(newName, 1)     # function to check if the key value newName(user imputed) is in controllers
        controllersS[newName] += higher    # controller's key value is increased by user specified amount
    elif choice == 2:
        errorCheck(newName, 2)
        videoGamesS[newName] += higher
    elif choice == 3:
        errorCheck(newName, 3)
        merchS[newName] += higher
    else:
        print("Input a Correct Value")
        lowerStock()
    print(f"{newName}'s stock was increased by {higher}")


def viewStock():    # function to display all shop info
    totalPrice = 0
    for x in prices:
        if x == "controllers":    # for each category will label once with heading
            print("\nControllers:")
        elif x == "videoGames":
            print("\nVideo Games:")
        elif x == "merch":
            print("\nMerch:")
        for i in prices[x]:
            print(f"{i}       ${prices[x][i]}      {stock[x][i]}")
            totalPrice += prices[x][i] * stock[x][i]
    print(f"\nTotal Price: ${round(totalPrice, 2)}")
    # will traverse through each key and value of nested dictionary to display shop


def errorCheck(i, type):
    if type == 1:   # depends on if controller, video game, or merch was selected
        if i not in controllersP:   # if key in controller not found
            print("The controller was not found")
            menu()    # will force user back to menu selection
    elif type == 2:
        if i not in videoGamesP:
            print("The video game was not found")
            menu()
    elif type == 3:
        if i not in merchP:
            print("The merch was not found")
            menu()


def menu():    # main menu screen loops till user selects exit
    while True:
        choice = int(input("""
What would you like to do? (1-6): 
1. Add new item
2. Remove an item   
3. Lower stock
4. Add to stock
5. View stock
6. Quit
    
Enter Choice Here: """))

        if choice == 1:
            addItem()
        elif choice == 2:
            removeItem()
        elif choice == 3:
            lowerStock()
        elif choice == 4:
            addStock()
        elif choice == 5:
            viewStock()
        elif choice == 6:
            print("All Done")
            break
        else:
            continue


viewStock()
menu()
