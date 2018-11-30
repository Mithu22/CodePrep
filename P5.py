class Buddy:
    def __init__(self,name,similarity,wishlist):
        self.name = name
        self.similarity = similarity
        self.wishlist = wishlist

    def __repr__(self):
        print("Name " + str(self.name) + " Similarity  " + str(self.similarity))

def findBuddies(myList,friendLists):
    buddymap = {}
    buddies = []
    b = 1
    for i in friendLists:
        buddymap[b] = i
        sim = i.intersection(myList)
        if len(sim) > len(myList)/2:
            buddies.append(Buddy(b,len(sim),i))
        b += 1

    buddies = sorted(buddies,key=lambda buddy:buddy.similarity)
    for b in buddies:
        b.__repr__()

mywishList = set(["a","b","c","d","e"])
buddyList = [set(["a","b","c","d","e"]),set(["a","d","b","c","e"]),set(["a","b","c"])]
findBuddies(mywishList,buddyList)
