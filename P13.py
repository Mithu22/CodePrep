def pourWater(positions,loc,water):
    waters = [0] * len(positions)
    flag = 1
    while water > 0:
        left = loc - 1

        while left >= 0:
            if positions[left] + waters[left] > positions[left+1] + waters [left + 1]:
                break
            left-=1

        if left < 0:
            print("Too much water to fill!")
            flag = 0
            break

        if positions[left+1] + waters[left+1] < positions[loc] + waters[loc]:
            pourIn = left+1
            waters[pourIn] += 1
            water-=1
            continue

        right = loc + 1


        while right < len(positions):
            if positions[right] + waters[right] > positions[right-1] + waters[right-1]:
                break
            right+=1

        if right >= len(positions):
            print("Too much water to fill")
            flag = 0
            break

        if positions[right-1] + waters[right-1] < positions[loc] + waters[loc]:
            pourIn = right-1
            waters[pourIn] += 1
            water -= 1
            continue



        pourIn = loc
        waters[pourIn] += 1
        water-=1

    if flag:
        display(positions,waters)

def display(positions,waters):
    maxHeight = 0
    for i in range(0, len(positions)):
        maxHeight = max(maxHeight,positions[i]+waters[i])


    for h in range(maxHeight,-1,-1):
        for i in range(0,len(positions)):
            if h <= positions[i]:
                print("+",end='')
            elif h > positions[i] and h <= positions[i] + waters[i]:
                print("w",end='')
            else:
                print(" ",end='')
        print("")
    print("")

positions = [5, 4, 2, 1, 2, 3, 2, 1, 0, 1, 2, 4]
pourWater(positions,5,10)







