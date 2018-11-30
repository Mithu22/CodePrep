def paginate(input,pgsize):
    hosts = set()
    results = []
    if input is None or pgsize == 0:
        return results

    i = 0
    end = False
    it = input.__iter__()
    count = 0
    try:
        while len(input) > 0:
            cur = it.__next__()
            host = cur.split(",")[0]
            if host not in hosts or end:
                hosts.add(host)
                results.append(cur)
                input.remove(cur)
                it = input.__iter__()
                count += 1
            if count == pgsize:
                hosts.clear()
                count = 0
                if len(input)>0:
                    results.append(" ")
                    end = False
                it = input.__iter__()

            if len(input) > 0 and cur == input[len(input)-1]:
                end = True
                it = input.__iter__()
    except StopIteration:
        pass


    return results

#strs = ["1,28,310.6,SF","4,12,222,SF","20,9,55,Oak","6,1,333,Brooklyn",
 #       "6,10,222,Oakbrook","1,99,995,LA","6,85,888,Tennessee","7,98,887,AZ",
  #      "6,12,999,Iowa","2,22,222,Bridgeport","2,88,885,Rochester","3,7,77,TN","2,97,987,Orlando"]

strs = ["1,28,300.1,SanFrancisco",
"4,5,209.1,SanFrancisco",
"20,7,208.1,SanFrancisco",
"23,8,207.1,SanFrancisco",
"16,10,206.1,Oakland",
"1,16,205.1,SanFrancisco",
"6,29,204.1,SanFrancisco",
"7,20,203.1,SanFrancisco",
"8,21,202.1,SanFrancisco",
"2,18,201.1,SanFrancisco",
"2,30,200.1,SanFrancisco",
"15,27,109.1,Oakland",
"10,13,108.1,Oakland",
"11,26,107.1,Oakland",
"12,9,106.1,Oakland",
"13,1,105.1,Oakland",
"22,17,104.1,Oakland",
"1,2,103.1,Oakland",
"28,24,102.1,Oakland",
"18,14,11.1,SanJose",
"6,25,10.1,Oakland",
"19,15,9.1,SanJose",
"3,19,8.1,SanJose",
"3,11,7.1,Oakland",
"27,12,6.1,Oakland",
"1,3,5.1,Oakland",
"25,4,4.1,SanJose",
"5,6,3.1,SanJose",
"29,22,2.1,SanJose",
"30,23,1.1,SanJose"]
res = paginate(strs,12)
print(res)



