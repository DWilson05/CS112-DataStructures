totalValue = 0
farmShop = {"milk": 2.50,
            "eggs": 5.25,
            "bread": 3.75,
            "butter": 2.75,
            "cheese": 6.55
            }
# create dictionary to store price of each item

farmStock = {"milk": 15,
             "eggs": 26,
             "bread": 11,
             "butter": 21,
             "cheese": 5
             }
# create dictionary to store stock of items

print(f"Items   Price   Stock  Total")
for x in farmShop:
    print(f"{x}    ${farmShop[x]}     {farmStock[x]}    ${farmStock[x] * farmShop[x]}")
    totalValue += farmStock[x] * farmShop[x]
print(f"\nThe total value is: ${totalValue}")
