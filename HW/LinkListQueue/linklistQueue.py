class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class queue:
    def __init__(self):
        self.front = self.rear = None
    
    def enQueue(self, item):
        if self.rear == None:
            self.front = self.rear = node(item)
        self.rear = node(item)
        if self.front.next == None:
            self.front.next = node(item)

    def deQueue(self):
        if self.front == None:
            return
        temp = self.front
        self.front = temp.next
        if self.front == None:
            self.rear = None

if __name__ == '__main__':
    q = queue()
    q.enQueue(1)
    q.enQueue(2)
    q.enQueue(3)
    q.deQueue()
    print(q.front.data)
    print(q.rear.data)