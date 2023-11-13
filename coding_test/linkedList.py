class Node :
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next

first = Node(1)
second = Node(2)
third = Node(3)

first.next = second
second.next = third
first.value = 6

class LinkedList(object):
    def __init__(self) :
        self.head = None
    def append(self, value):
        new_node = Node(value)
        
        if self.head is None:
            self.head = new_node
            # 맨 뒤의 node가 new_node를 가리켜야 한다.
        else : 
            current = self.head
            while(current.next):
                current = current.next
            current.next = new_node
    def get(self, idx):
        current = self.head
        for _ in range(idx):
            current = current.next
        return current.value
    def insert(self, idx, value):
        new_node = Node(value)
        current = self.head
        if idx == 0:
            new_node.next = self.head
        else:
            for _ in range(idx - 1):
                current = current.next
                new_node.next = current.next
                current.next = new_node
    def remove(self, idx):
        current = self.head
        if idx == 0:
            self.head = self.head.next
        for _ in range(idx - 1):
            current = current.next
            current.next = current.next.next
    def insert_back(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next






ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.remove(3)

        