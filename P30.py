#28,26,25,24,27,22,9,14,23

def isoverlap(r1,r2):
    x1 = r1[0]
    y1 = r1[1]
    x2 = r1[2]
    y2 = r1[3]
    x3 = r2[0]
    y3 = r2[1]
    x4 = r2[2]
    y4 = r2[3]
    return x1 < x4 and x3 < x2 and y1 < y4 and y3 < y2

def find(val,parents):
    while parents[val] != val:
        val = parents[val]

    return val

def count(rectangles):
    n = len(rectangles)
    parents = [0] * n
    for i in range(0,n):
        parents[i] = i

    for i in range(0,n-1):
        for j in range(i+1,n):
            if isoverlap(rectangles[i],rectangles[j]):
                root1 = find(i,parents)
                root2 = find(j,parents)
                if root1 != root2:
                    parents[root1] = root2

    print(parents)

    res = set()
    for i in range(0,n):
        res.add(find(i,parents))

    print(len(res))
    print(res)

rectangles = [[-3,-2,2,1],[10,8,15,10],[1,0,7,4],[12,9,16,12],[-2,-1,5,3]]
count(rectangles)
