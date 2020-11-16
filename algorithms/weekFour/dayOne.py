# Node
#    - Constructor
#       -val
#       - next
# SinglyLinkList
#    -Constructor
#        - head
#    - addFront(val)
#        - add a new node to the beginning of the list
#    - removeFront()
#       - removes and returns the first node of the list
#    - container(val)
#       - returns a boolean on whether or not the val is in the list
#    -  addBack(val)
#        - add new node to the end of the list
#    - removeBack()
#       - removes and returns the last node of the list

def Node():
    def __init__(self, value):
        self.val = value
        self.next = None

def SLList():
    def __init__(self):
        self.head = None
    def add_front(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        return self