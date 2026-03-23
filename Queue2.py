


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = Node("dummy")   # dummy head
        self.tail = self.head       # initialize tail
        self.size = 0

    def getsize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0
    
    def enqueue(self, value):
        self.tail.next = Node(value)
        self.tail = self.tail.next
        self.size += 1

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
            return None
        removed = self.head.next
        self.head.next = removed.next
        self.size -= 1
        if self.size == 0:   # reset tail when queue becomes empty
            self.tail = self.head
        return removed.data

    def front(self):
        if self.isEmpty():
            print("Queue is empty")
            return None
        return self.head.next.data


# Test
myQueue = Queue()

myQueue.enqueue(1)
myQueue.enqueue(2)
print(myQueue.front())   # ➝ 1
myQueue.dequeue()
myQueue.enqueue(3)
print(myQueue.dequeue()) # ➝ 2
myQueue.dequeue()
print(myQueue.front())   # ➝ Queue is empty