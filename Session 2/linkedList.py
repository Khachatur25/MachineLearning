class Node:
    def _init_(self,data=None):
        self.data = data
        self.next = None

class LinkedList:
    def _init_(self):
        self.head = None

    def add_from_end(self,data):
        new_node = Node(data)
        if not self.head:

