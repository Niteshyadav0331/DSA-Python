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
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = new_node

    def insertPosition(self, pos, data):
        size = self.calcSize()
        if pos < 1 and pos > size:
            print(f"Can't insert {pos} is not a valid position")

        else:
            temp = self.head
            new_node = Node(data)

        for i in range(1, pos):
            temp = temp.next
            pos -= 1

        new_node.next = temp.next
        temp.next = new_node

    def display(self):
        temp = self.head

        while temp:
            print(temp.data, end = " ")
            temp = temp.next

    def calcSize(self):
        size = 0

        node = self.head

        while node is not None:
            node = node.next
            size += 1

        return size


ll = LinkedList()
ll.insertStart(12)
ll.insertStart(15)
ll.insertStart(17)

ll.insertLast(31)
ll.insertLast(11)
ll.insertLast(21)

ll.insertPosition(2, 23)


ll.display()
