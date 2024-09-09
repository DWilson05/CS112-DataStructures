# Premise: A local bakery sells donuts individually or in dozens. One donut costs $1.75, and a donut dozen costs
# $12.25. Program: Write a program that prompts the user for the number of donuts they want to buy, then prints the
# amount owed with full details.

donutAmount = int(input("\nHello! How many donuts would you like to purchase? "))
dozenAmount = int(donutAmount / 12)
remainder = donutAmount % 12
total = (dozenAmount * 12.25) + (remainder * 1.75)
# Takes input for amount of donuts
# Calculates a dozen amount by rounding donut amount by 12, remainder of donuts, and total cost in different variables

print(f"You have ordered {donutAmount} donuts.")
print(f"That will be {dozenAmount} dozen at $12.25 and {remainder} donuts at $1.75 each.")
print(f"Your total today will be ${total}.")

# Prints out the amount ordered, the different prices, and the total cost
