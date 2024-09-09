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
         print("Stack: ", end = " ")
         if self.top is None: # if the Stack is empty return
             print("Stack is empty")
             return
         else:  # traverse through Stack until the end
             n = self.top
             while n is not None:
                 print(n.item, end =" " )
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
               count = count+1
               n = n.ref
          return count

     
   # -------------- Pop  ------------------

     def Pop(self):  # remove the top
            if self.top is None:  # if there is no top stack is empty
                print("Stack is empty!")
                return
            x = self.top.item  # store the top item in x
            self.top = self.top.ref # item before the top is now the new top
            return x # return the item that was at the top
 
