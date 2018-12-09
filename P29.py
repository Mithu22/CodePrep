import sys
import heapq as hq
class Wizard:
    def __init__(self,id):
        self.id = id
        self.dist = sys.maxsize

    def __lt__(self,other):
        return self.dist < other.dist

    def __gt__(self,other):
        return self.dist > other.dist

    def __le__(self,other):
        return self.dist <= other.dist

    def __ge__(self,other):
        return self.dist >= other.dist

    def __eq__(self,other):
        return self.dist == other.dist

def path(wizards,source,target):
    if wizards is None or len(wizards)==0:
        return 0

    n = len(wizards)
    parent = [0] * n
    wizmap = {}
    for i in range(0,n):
       wizmap[i]=Wizard(i)
       parent[i] = i

    wizmap[source].dist = 0
    pq = []
    hq.heappush(pq,wizmap[source])
    while len(pq) > 0:
        cur = hq.heappop(pq)
        neighbors = wizards[cur.id]
        for n in neighbors:
            next = wizmap[n]
            weight = pow((next.id-cur.id),2)
            if cur.dist + weight < next.dist:
                parent[next.id] = cur.id
                if pq.__contains__(next):
                    pq.remove(next)
                    hq.heapify(pq)
                next.dist = cur.dist + weight
                hq.heappush(pq,next)


    res = []
    t = target
    while t != source:
        res.append(t)
        t = parent[t]
    res.append(source)
    return res

result = path([[1,5,9],[2,3,9],[4],[],[],[9],[],[],[],[]],0,9)
result.reverse()
print(result)
