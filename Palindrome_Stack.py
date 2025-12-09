# Python code​​​​​​‌‌‌​‌‌​​​​​​​​‌‌​​​‌‌‌‌‌‌ below
# Define a node class for the linked list
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

# Define a stack class using a linked list
class Stack:
  def __init__(self):
    self.head = None # The head node of the linked list

  def push(self, data):
    new_node = Node(data)       #New Node with Data
    new_node.next = self.head   #New node's next pointer points to last head
    self.head = new_node        #New Head is new Node

  def pop(self):
    if self.isEmpty():           #If Stack is Empty
      return None
    popped = self.head.data      #Popped Node Data
    self.head = self.head.next   #New Head is last element
    return popped

  def peek(self):
    return self.head.data        #Return Head Data without removing it

  def isEmpty(self):
    return self.head is None     #Return True if Head is None

# Define a function that checks if a string is a palindrome using a stack
def isPalindrome(string):

  cleaned_string = ""           
  
  # Clean the string: remove non-alphabetic characters and convert to lowercase
  for ch in string:
    if ch.isalpha():
      cleaned_string += ch.lower()

  stack = Stack()
  for ch in cleaned_string:
    stack.push(ch)              #Push all characters to stack

#Compare popped/last character with current character
  for ch in cleaned_string:
      if(stack.pop() != ch):    
        return False
  return True

# Test the isPalindrome function
string = input("Enter a string: ")
print(isPalindrome(string))


