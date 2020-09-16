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
        idx = 0
        queue = []
        while tmp.data:
            #queue.insert(idx, tmp.data)
            print(tmp.data)
            tmpp = tmp
            tmp = tmpp.next
        print(queue)

if __name__ == '__main__':
    q = queue()
    q.enQueue(3)
    q.enQueue(5)
    q.enQueue(2)
    q.deQueue()
    print('q.front.data', q.front.data)
    print('q.rear.data', q.rear.data)
    q.showQueue()