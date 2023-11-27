class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self,data):
        node = Node(data,self.head)
        self.head = node
    def insert_at_end(self,data):
        node = Node(data,None)
        penultimate = self.head
        while penultimate.next:
            penultimate = penultimate.next
        penultimate.next = node
    def printlinkedlist(self):
        climax = self.head

        while climax:
            print(climax.data)
            climax = climax.next
    def delete_node_beg(self,data):
        if self.head.data == data:
            self.head = None
        else:
            test = self.head
            while test.next.data != data:
                test = test.next
            test1 = test.next.next
            test.next = test1

    def sorting(self):
        current = self.head
        new_current = current.next
        while current.next.next != None:
            while new_current.next!=None:
                if current.data > current.next.data:
                    current.data,current.next.data = current.next.data,current.data
                new_current = new_current.next
            current = current.next


llp = LinkedList()
llp.insert(3)
llp.insert(4)
llp.insert(8)
llp.insert_at_end(6)
llp.delete_node_beg(4)
llp.sorting()
llp.printlinkedlist()

