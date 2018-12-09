def combinationSum(input,target):
    res = []
    input.sort()
    dfs(input,target,0,[],res)
    return res

def dfs(input,target,index,path,res):
    if target < 0:
        return
    if target == 0:
        res.append(path)
        return
    for i in range(index,len(input)):
        if i > index and input[i] == input[i-1]:
            continue
        dfs(input,target-input[i],i+1,path+[input[i]],res)

l = combinationSum([1,1,2,3],5)
for i in l:
    print(i)
