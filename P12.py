def regmatch(source,pattern):
    T= [[False for j in range(len(pattern)+1)] for i in range(len(source)+1)]
    T[0][0] = True
    for i in range(1,len(T[0])):
        if pattern[i-1] == '*':
            T[0][i] = T[0][i-2]

    for i in range(1,len(T)):
        for j in range(1,len(T[0])):
            if pattern[j-1] == source[i-1] or pattern[j-1]=='.':
                T[i][j] = T[i-1][j-1]
            elif pattern[j-1] == '+':
                T[i][j] = T[i][j-1]
                if pattern[j - 2] == '.' or pattern[j - 2] == source[i - 1]:
                    T[i][j] = T[i][j] or T[i - 1][j]
            elif pattern[j-1] == '*':
                T[i][j] = T[i][j-2]
                if pattern[j-2]=='.' or pattern[j-2] == source[i-1]:
                    T[i][j] =  T[i-1][j]
            else:
                T[i][j] = False

    for i in T:
        print(i)
    return T[len(source)][len(pattern)]

print(regmatch("aaa","ab*a*c*a"))
print(regmatch("abcy","a*b.*y"))