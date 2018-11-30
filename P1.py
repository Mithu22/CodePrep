def func(n):
    if n <=1:
        return 1
    elif n % 2 == 0:
        return 1 + func(n/2)
    else:
        return 1 + func(3*n+1)

def trigger(n):
    if n < 1:
        return 0
    maxim = 0
    for i in range(1,n+1):
        t = func(i)
        maxim = max(t,maxim)
    return maxim

def funcImproved(n,res):
    if n <= 1:
        return 1
    if n in res.keys():
        return res[n]

    if n % 2 == 0:
        n = n/2
    else:
        n = 3*n + 1
    t = funcImproved(n,res)
    res[n] = t
    return 1 + res[n]


def triggerImproved(n):
    res = {}
    if n < 1:
        return 0
    maxim = 0
    for i in range(1,n+1):
        t = funcImproved(i,res)
        res[i] = t
        maxim = max(t,maxim)
    return maxim

print(trigger(101))
print(triggerImproved(101))