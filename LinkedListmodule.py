class Node:
     def __init__(self, data):
         self.item = data
         self.ref = None

class LinkedList:
     # ---------------Create an empty linked list -------------
     
     def __init__(self):
         self.start_node = None
         
     # --------------- Traverse the linked list  ----------------------
     
     def traverse_list(self):
         print("Linked List: ", end = " ")
         if self.start_node is None:
             print("List is empty")
             return
         else:
             n = self.start_node
             while n is not None:
                 print(n.item, end =" " )
                 n = n.ref
         print(" ")        
                 
    #  ------------- Insert at start  ----------------------
    
     def insert_at_start(self, data):
            new_node = Node(data)
            new_node.ref = self.start_node
            self.start_node = new_node


    #  ------------- Insert at end  ----------------------
    
     def insert_at_end(self, data):
            new_node = Node(data)
            if self.start_node is None:
                 self.start_node = new_node
                 return
            n = self.start_node
            while n.ref is not None:
                  n = n.ref
            n.ref = new_node

     #  ------------ Insert in middle  ----------------------
     
     def insert_after_item(self, x, data):
             n = self.start_node
             print(n.ref)
             while n is not None:
                 if n.item == x:
                      break
                 n = n.ref
             if n is None:
                 print("Item not in list")
             else:
                 new_node = Node(data)
                 new_node.ref = n.ref
                 n.ref = new_node
                 
      #  ------------ Count nodes ---------------------------           

     def get_count(self):
          if self.start_node is None:
               return 0
          n = self.start_node
          count = 0
          while n is not None:
               count = count+1
               n = n.ref
          return count

       #  ------------- Search List for an item  ------------

     def search_item(self,x):
           if self.start_node is None:
               print(" List has no items")
               return
           n = self.start_node
           while n is not None:
               if n.item == x:
                    print("Item found")
                    return True
               n = n.ref
           print("Item not found")
           return False

        # -------------- Delete first item  ------------------

     def delete_at_start(self):
            if self.start_node is None:
                print("Linked list is empty!")
                return
            self.start_node = self.start_node.ref

        # -------------- Delete last item  --------------------

     def delete_at_end(self):
         if self.start_node is None:
                print("Linked list is empty!")
                return
         n = self.start_node
         while n.ref.ref is not None:
             n= n.ref
         n.ref= None

    # --------------- Delete a certain item ---------------
         
     def delete_element(self,x):
         if self.start_node is None:
                print("Linked list is empty!")
                return
         if self.start_node.item == x:
                self.start_node = self.start_node.ref
                return
         n = self.start_node
         while n.ref is not None:
              if n.ref.item == x:
                  break
              n = n.ref
         if n.ref is None:
             print("item not found")
         else:
             n.ref = n.ref.ref

             
