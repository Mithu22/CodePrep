class TrieNode:
    def __init__(self):
        self.next = 26 * [None]
        self.lst = []
        self.index = -1

def isPalindrome(word,i,j):
    while(i<j):
        if word[i] != word[j]:
            return False
        i += 1
        j -= 1
    return True

def addWord(root,word,idx):
    for j in range(len(word)-1,-1,-1):
        if root.next[ord(word[j])-ord('a')] is None:
            root.next[ord(word[j])-ord('a')] = TrieNode()
        if isPalindrome(word,0,j):
            root.lst.append(idx)
        root = root.next[ord(word[j])-ord('a')]
    root.lst.append(idx)
    root.index = idx

def search(words,i,root,res):
    for j in range(0,len(words[i])):
        if root.index >= 0 and root.index != i and isPalindrome(words[i],j,len(words[i])-1):
            res.append([i,root.index])
        root = root.next[ord(words[i][j])-ord('a')]
        if root is None:
            return

    for j in root.lst:
        if j == i:
            continue
        res.append([i,j])

def isPal(word):
    for i in range(0,int(len(word)/2)):
        if word[i] != word[len(word)-1-i]:
            return False
    return True

def palindromePairs(words,res):
    wordmap = {}
    for i in range(0,len(words)):
        wordmap[words[i]] = i
    for i in range(0,len(words)):
        left = 0
        right = 0
        while left <= right:
            s = words[i][left:right]
            j = wordmap.get(s[::-1],None)
            if j != None and j != i and isPal(words[i]
                                                     [right if left==0 else 0 :
                                                      len(words[i]) if left==0 else left]):
                res.append([i,j] if left==0 else [j,i])
            if right < len(words[i]):
                right += 1
            else:
                left += 1



words = ["abcd","dcba","lls","s","sssll"]
res = []
root = TrieNode()
for w in range(0,len(words)):
    addWord(root,words[w],w)
for w in range(0,len(words)):
    search(words,w,root,res)
print(res)
res.clear()
palindromePairs(words,res)
print(res)
