class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertStart(self, data):
        new_node = Node(data)
        new_node.next = self.head

        self.head = new_node

    def insertLast(self, data):
        new_node = Node(data)
        new_node.next = None

        if self.head is None:
            self.head = new_node

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = new_node

    def insertPosition(self, pos, data):
        size = self.calcSize()
        if pos < 1 and pos > size:
            print(f"Can't insert {pos} is not a valid position")

        elif pos == 0:
            return self.insertStart(data)

        else:
            temp = self.head
            new_node = Node(data)

        for i in range(1, pos):
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node

    def calcSize(self):
        size = 0
        temp = self.head

        while temp is not None:
            temp = temp.next
            size += 1
        return size

    def display(self):
        if self.head is None:
            return

        temp = self.head

        while temp is not None:
            print(temp.data, end = " ")
            temp = temp.next

ll = LinkedList()
ll.insertStart(6)
ll.insertStart(8)
ll.insertStart(10)
ll.insertStart(12)
ll.insertLast(14)
ll.insertLast(16)
ll.insertPosition(2, 5)

ll.display()
