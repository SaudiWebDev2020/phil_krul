
def rFib(num):
    if num <= 1:
        return 1
    return rFib(num) + rFib(num-1)

def rListLength(node):
    if node == None:
        return 0
    else:
        return rListLength(node.next)
    return rListLength(node) + 1

def rSigma(num):
    if num == 0:
        return 0
    return num + rSigma(num - 1)

def rFactorial(num):
    if num == 0:
        return 0
    return rFactorial(num + 1) * num


class Node():
    def __init__(self, value):
        self.val = value
        self.next = None

class SLList():
    def __init__(self):
        self.head = None
    def add_front(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        return self

my_list = SLList()
my_list.add_front(8).add_front(7).add_front(6)
print(rListLength(my_list.head))