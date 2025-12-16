# Python code​​​​​​‌‌‌​‌‌​​‌​‌​‌‌​​‌​‌​​​‌‌​ below

# Code simulates the process of printing operation using Queues 
#It is assumed that printer prints 2 pages per minute, and a queue of documents waiting to be printed
# Define a queue class using a list
class Queue:
  def __init__(self):
    self.list = [] # The list to store the elements

  def enqueue(self, data):
    self.list.append(data)  #Add item to Queue
    return None

  def dequeue(self):
    if(self.isEmpty()):
      return None
    else:
      popped = self.list.pop(0) #Pop first item in Queue
      return popped

  def front(self):
    if(self.isEmpty()):
      return None
    else:
      return self.list[0]   #Return first item in the Queue

  def rear(self):
    if(self.isEmpty()):
      return None
    else:
      return self.list[-1]  #Return last item in the Queue

  def size(self):
    return len(self.list)   #Return size of the Queue

  def isEmpty(self):
    return len(self.list)==0 

# An object for Queue class created for Printer Operation 
PrinterQueue = Queue()

# Define a function that simulates the printing process using a queue
def printDocuments(documents):
  printer_output = []
  for item in documents:
    PrinterQueue.enqueue(item)

  while(len(PrinterQueue.list)):
    printed = PrinterQueue.dequeue()
    printer_output.append(f"Document {printed[0]} printed in {printed[1]/2} minutes")

  return printer_output

documents = [("Report", 10), ("Essay", 5), ("Slides", 15)]
printer_output = printDocuments(documents)
print(printer_output)