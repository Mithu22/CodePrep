from heapq import *
class Heaps:
    def __init__(self):
        self.heaps = [],[]

    def addNum(self,num):
        small,large = self.heaps
        heappush(small,-heappushpop(large,num))
        if len(large) < len(small):
            heappush(large,-heappop(small))

    def findMedian(self):
        small,large = self.heaps
        if len(large) > len(small):
            return large[0]
        else:
            return float((large[0]-small[0])/2)

hp = Heaps()
hp.addNum(1)
hp.addNum(2)
hp.addNum(-3)
print(hp.findMedian())
hp.addNum(4)
print(hp.findMedian())
hp.addNum(5)
print(hp.findMedian())