class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head_node = None
        self.tail_node = None

    def Enqueue(self, data):
        new_node = Node(data)
        if(self.head_node is None):
            self.head_node = new_node
            self.tail_node = new_node
        else:
            self.tail_node.next = new_node
            self.tail_node = new_node
        return None
        
    def Dequeue(self):
        if(self.head_node is None):
            print("\nQueue is Empty")
        else:
            out = self.head_node.value
            self.head_node = self.head_node.next
            print(f"\nRemoved {out} from Queue")
        return None


Q = Queue()
break_loop = False

# Loop to take user input
while True:
   try:
      choice = int(input("\nSelect one -\n1. Enqueue \n2. Dequeue \n3. Print Queue \n4. Exit Program \n\n"))

   except ValueError:
      print("\nPlease enter a valid number \n")
      continue

   match (choice):
      case 1:
         item = int(input("\nEnter element to add to Queue \n"))
         Q.Enqueue(item)

      case 2:
         Q.Dequeue()

      case 3:
         if (Q.head_node is None):
            print("Queue is empty!")
         else:
            dispQ = Q.head_node
            while(dispQ != None):
               print(f"\n{dispQ.value}")
               dispQ = dispQ.next
               
      case 4:
         break_loop = True

      case _:
         print("Invalid choice! Enter 1-4\n")

   if break_loop:
      break

