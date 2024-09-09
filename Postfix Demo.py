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


def enter_expression():  # taken in an expression as a string and returns results
	print("Enter a Postfix expression: ")
	expression = input()
	return evaluate_expression(expression)


def evaluate_expression(expression):  # function to evaluate the postfix expression
	my_stack = Stack()  # start a new stack to use
	items = expression.split()  # split function separates strings into a list at space
	for i in items:  # for each item in the expression
		if i.isdigit():  # check if it is a number
			my_stack.Push(int(i))  # store it in the stack if it's a number
		else:  # otherwise it's an operator
			num_two = my_stack.Pop()  # retrieve the top/second number
			num_one = my_stack.Pop()  # retrieve the first number
			result = perform_operation(i, num_one, num_two)  # use the function to perform operation
			my_stack.Push(result)  # push the result into the stack
	return my_stack.Pop()  # when done, return the final result


def perform_operation(operator, num_one, num_two):  # evaluates the operator tp perform operation
	if operator == "+":
		return num_one + num_two
	elif operator == "-":
		return num_one - num_two
	elif operator == "*":
		return num_one * num_two
	elif operator == "/":
		return num_one / num_two


print("Postfix Calculator")
while True:  # while client wants to keep entering expression, keep looping
	choice = int(input("1. Enter Postfix expression, 2. Quit\n"))
	if choice == 1:
		print(enter_expression())  # allow client to enter a new expression
	else:
		break
