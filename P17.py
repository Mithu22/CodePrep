import math
def round(prices,target):
    floored = [math.floor(x) for x in prices]
    remaining = abs(target-sum(floored))
    ceils = sorted(enumerate(prices),key = lambda x:math.floor(x[1])+1-x[1])
    for i in range(0,remaining):
        idx = ceils[i][0]
        floored[idx] = math.ceil(ceils[i][1])
    return floored



print(round([1.2, 2.5, 3.6, 4.0],10))

