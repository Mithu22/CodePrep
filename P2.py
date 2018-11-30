class LimitedQueue:
    def __init__(self,s):
        self.fixedsize = s
        self.count = 0
        self.head = 0
        self.tail = 0
        self.headlist = self.taillist = []

    def isEmpty(self):
        return self.count == 0

    def size(self):
        return self.count

    def enqueue(self,num):
        if self.tail == self.fixedsize - 1:
            newlist = []
            newlist.append(num)
            self.taillist.append(newlist)
            self.taillist = self.taillist[self.tail]
            self.tail = 0
        else:
           self.taillist.append(num)
        self.tail += 1
        self.count += 1

    def dequeue(self):
        if self.isEmpty():
            return None
        val = self.headlist[self.head]
        self.head += 1
        self.count -= 1
        if self.head == self.fixedsize-1:
            newlist = self.headlist[self.head]
            self.headlist.clear()
            self.headlist = newlist
            self.head = 0
        return val

q = LimitedQueue(5)
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
q.enqueue(8)
q.enqueue(9)
q.enqueue(10)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.size())
print(q.isEmpty())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.enqueue(12))
print(q.isEmpty())
print(q.size())
print(q.dequeue())