import functools
class Interval:
    def __init__(self,start,end):
        self.start = start
        self.end = end

    def __repr__(self):
        print(str(self.start) + " " + str(self.end))

def missed(intervals):
    res = []
    intervals = sorted(intervals,key = lambda i:i.start)
    availablestart = intervals[0].start
    for i in intervals:
        if i.start <= availablestart:
            availablestart = max(availablestart,i.end)
            continue
        res.append(Interval(availablestart,i.start))
        availablestart = i.end
    return res

intervals = []
intervals.append(Interval(1,2))
intervals.append(Interval(2,3))
intervals.append(Interval(3,4))
intervals.append(Interval(5,8))
for i in missed(intervals):
    i.__repr__()




