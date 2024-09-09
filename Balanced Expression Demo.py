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

# -------------------------------------------------------------------------


def evaluate_parentheses(expression):  # evaluates expression for parentheses
	open_stack = Stack()  # stack to keep opening parentheses
	close_stack = Stack()  # stack to keep closing parentheses
	items = expression.split()  # split the string into a list
	for i in items:  # loop through the list to find parentheses
		if i == "(": # if opening parentheses
			open_stack.Push(i)  # store them in open stack
		elif i == ")":  # if closing parentheses
			close_stack.Push(i)  # store them in closed stack
	opening = open_stack.get_count()  # count open parentheses
	closing = close_stack.get_count()  # count close parentheses
	if opening != closing:  # if counts are not the same - not balanced
		print("Expression ", expression, " is not balanced.")
	else:  # otherwise expression is balanced
		print("Expression ", expression, " has balanced parentheses.")
	print("There are ", opening, " opening parentheses, and ", closing, " closing parentheses.")


def evaluate_expression(expression):
	my_stack = Stack()  # stack to keep opening items
	items = expression.split()  # split the string into a list
	valid = True
	for i in items:  # loop through the list to find [](){}
		if i == "(" or i == "[" or i == "{":  # if opening items
			my_stack.Push(i)  # store them in open stack
		elif i == ")" or i == "]" or i == "}":  # if closing items
			o = my_stack.Pop()  # pop the top item from the stack
			if (o == "(" and i != ")") or (o == "[" and i != "]") or (o == "{" and i != "}"):
				valid = False  # if the items don't match up, no balance
				break
	count = my_stack.get_count()  # ensure nothing is left in the stack
	if valid and count == 0:  # if stack is empty and pairs are valid
		print("Expression ", expression, " is balanced.")
	else:  # items are left in stack or pairs are not valid
		print("Expression ", expression, " is not balanced.")


def get_expression():  # function to retrieve user input
	print("Enter an expression to evaluate: ")
	expression = input()
	evaluate_expression(expression)  # send expression for evaluation


print("Balance Checker")
while True:  # while the user wants to keep evaluating
	try:
		choice = int(input("1. Evaluate, 2. Quit\n"))
	except ValueError:  # handles empty submission
		continue
	if choice == 1:  # do another expression eval
		get_expression()
	else:  # done
		break
