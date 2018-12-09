from queue import Queue


def permutations(word):
    if word is None or len(word) == 0:
        return []
    q = Queue()
    q.put(word)
    for i in range(0,len(word)):
        if word[i].isdigit():
            continue
        size = q.qsize()
        for j in range(0,size):
            cur = q.get()
            curlist= list(cur)
            curlist[i] = curlist[i].upper()
            print(curlist)
            q.put(''.join(curlist))
            curlist[i] = curlist[i].lower()
            print(curlist)
            q.put(''.join(curlist))
    return q

q = permutations("AirBnB")
print(q.qsize())
while not q.empty():
    print(q.get())





