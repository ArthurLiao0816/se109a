class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class queue:
    def __init__(self):
        self.front = self.rear = None
    
    def enQueue(self, item):
        tmp = node(item)
        if self.rear == None:
            self.front = self.rear = tmp
            return
        self.rear.next = tmp
        self.rear = tmp
        
    def deQueue(self):
        if self.front == None:
            return
        temp = self.front
        self.front = temp.next
        if self.front == None:
            self.rear = None

    def showQueue(self):
        tmp = self.front
        queue = []
        while tmp.data:
            queue.append(tmp.data)
            tmpp = tmp
            if tmpp.next == None:
                break
            tmp = tmpp.next
        print("queue ->", queue)

if __name__ == '__main__':
    q = queue()
    q.enQueue(2)
    q.enQueue(9)
    q.enQueue(4)
    q.enQueue(8)
    q.enQueue(7)
    q.deQueue()
    q.deQueue()
    print('q.front.data', q.front.data)
    print('q.rear.data', q.rear.data)
    q.showQueue()