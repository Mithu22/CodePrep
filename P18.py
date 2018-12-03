from queue import Queue
def findMoves(input):
    target = "123456780"
    start = ""
    for i in range(0,len(input)):
        for j in range(0,len(input[0])):
            start += str(input[i][j])
    moves = [[1,3],[0,2,4],[1,5],[0,4,6],[1,3,5,7],[2,4,8],[3,7],[4,6,8],[5,7]]
    visited = set()
    res = 0
    states = Queue()
    states.put(start)
    visited.add(start)
    while not states.empty():
        for i in range(0,states.qsize()):
            cur = states.get()
            if cur == target:
                return res
            zero = cur.find('0')
            for m in moves[zero]:
                next = swap(cur,zero,m)
                if visited.__contains__(next):
                    continue
                visited.add(next)
                states.put(next)
        res += 1
    return -1

def swap(cur,zero,m):
    next = list(cur)
    temp = next[m]
    next[m] = '0'
    next[zero] = temp
    return ''.join(next)

input = [[3,1,4],
          [6,2,0],
          [7,5,8]
        ]

print(findMoves(input))

