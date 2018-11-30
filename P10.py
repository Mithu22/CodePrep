#1. get comma separated
#2. if comma within quotes, ignore
#3. remove double quotes
#4. if there are two double quotes, remove one
def parseString(input):
    res = []
    s = ""
    result = ""
    within = False
    if input is None or len(input) == 0:
        return None
    for i in range(0,len(input)):
        if within:
            if input[i] == '\"':
                if i < len(input)-1 and input[i+1]=='\"':
                    s += "\""
                    i+=1
                else:
                    within = False
            else:
                s += input[i]
        else:
            if input[i] == '\"':
                within = True
            elif input[i]==',':
                res.append(s)
                s = ""
            else:
                s += input[i]
    res.append(s)
    for r in res:
        result += r + "|"
    result = result[:len(result)-1]
    return result

print(parseString("John,Smith,john.smith@gmail.com,Los Angeles,1"))
print(parseString("Jane,Roberts,janer@msn.com,\"San Francisco, CA\",0"))
print(parseString("\"Alexandra \"\"Alex\"\"\",Menendez,alex.menendez@gmail.com,Miami,1"))
print(parseString("\"\"\"Alexandra Alex\"\"\""))

