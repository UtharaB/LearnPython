# Python Program to implement Queues with the help of Stacks and LIFO concept
# Queue is FIFO. However we implement this using LIFO stacks enqueue_stack and dequeue_stack which add or remove elements in LIFO concept

class Queue:
   def __init__(self):
      self.enqueue_stack = []
      self.dequeue_stack = []

   # Add a new item to Queue
   def enqueue(self, item):
      self.enqueue_stack.append(item)
      return None

   # Remove oldest item from Queue
   def dequeue(self):
      if len(self.dequeue_stack) == 0:
         while(len(self.enqueue_stack) > 0):
            data = self.enqueue_stack.pop()
            self.dequeue_stack.append(data)
      if len(self.dequeue_stack) == 0:
         return None
      else:
         return self.dequeue_stack.pop()


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
         Q.enqueue(item)

      case 2:
         popped = Q.dequeue()
         if popped is None:
            print("Queue is empty!")
         else:
            print(f"Dequeued element is {popped}")

      case 3:
         if len(Q.enqueue_stack + Q.dequeue_stack) == 0:
            print("Queue is empty!")
         else:
            print_list = Q.dequeue_stack.copy()
            print_list.reverse()
            print_list += Q.enqueue_stack
            print(f"Current Queue is {print_list}")

      case 4:
         break_loop = True

      case _:
         print("Invalid choice! Enter 1-4\n")

   if break_loop:
      break

         
      
      

   
   


      

