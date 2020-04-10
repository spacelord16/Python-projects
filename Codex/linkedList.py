class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.head is None:
            self.head = NewNode
            return
        last = self.head
        while (last.next):
            last = last.next
        last.next = NewNode

    def printlist(self):
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval = printval.next


list = LinkedList()
list.head = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
list.head.next = e2
e2.next = e3
list.AtEnd("Thu")
