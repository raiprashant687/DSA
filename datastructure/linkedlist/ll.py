class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class Linked_list:
    def __init__(self):
        self.head = None

    def insertatbeg(self,data):
        self.head = Node(data)

ll = Linked_list()
print(ll.insertatbeg(34))