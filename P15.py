class Army:
    def __init__(self,name,loc,strength = 1,isalive = True):
        self.name = name
        self.loc = loc
        self.strength = strength
        self.isalive = isalive

    def __repr__(self):
        print(self.name + " " + self.loc + " " + str(self.strength) + " " + str(self.isalive))


armies = {}
armymap = {}
supporters = {}
supportees = {}

def createarmy(name,loc):
    a = Army(name, loc)
    if name in armies:
        del(armies[name])
    armies[name] = a
    armymap[loc] = [name]

def process(input):
    for i in input:
        val = i.split(" ")
        if val[2]== "Hold":
            createarmy(val[0],val[1])
        elif val[2] == "Move":
            createarmy(val[0],val[1])
        elif val[2] == "Support":
            createarmy(val[0],val[1])
            if(not val[3] in armies):
                createarmy(val[3],"temp")
    if "temp" in armymap:
        del[armymap["temp"]]

    val.clear()
    for i in input:
        val = i.split(" ")
        if val[2] == "Move":
            move(val[0],val[3])
        elif val[2] == "Support":
            support(val[0],val[3])

    result()


    # for loc,alist in armymap.items():
    #     if len(alist) > 0:
    #         print(loc,alist)
    # for supporter,supportee in supporters.items():
    #     print(supporter,supportee)
    # for supportee,supporter in supportees.items():
    #     print(supportee,supporter)


def move(army,loc):
    oldloc = armies[army].loc
    armymap[oldloc].remove(army)
    if loc in armymap:
        armymap[loc].append(army)
    else:
        armymap[loc] = [army]
    armies[army].loc = loc

    armylist = armymap.get(loc,None)
    if armylist is not None and len(armylist) > 0:
        for a in armylist:
            supporterList = supporters.get(a,None)
            if supporterList is not None and len(supporterList) > 0:
                for s in supporterList:
                    armies[s].strength -= 1
                    supporteeList = supportees[s]
                    if supporteeList is not None and len(supporteeList) > 0:
                        supporteeList.remove(a)
                        supportees[s] = supporteeList
                del(supporters[a])

def support(army,newarmy):
    armies[newarmy].strength += 1
    if army in supporters:
        supporters[army].append(newarmy)
    else:
        supporters[army] = [newarmy]

    if newarmy in supportees:
        supportees[newarmy].append(army)
    else:
        supportees[newarmy] = [army]

def result():
    for loc in armymap:
        alist = armymap[loc]
        if len(alist) == 0:
            continue
        maxStrength = max(armies[a].strength for a in alist)
        count = 0
        for t in alist:
            if armies[t].strength < maxStrength:
                armies[t].isalive = False
            else:
                count+=1
        if count > 1:
            for t in alist:
                if armies[t].strength == maxStrength:
                    armies[t].isalive = False

    print("Result")
    for armyObj in armies.values():
        if armyObj.isalive:
            print(armyObj.name," "+armyObj.loc)
        else:
            print(armyObj.name," "+"[dead]")

process(["A Paris Support B","B Bohemia Support C","C London Support A","A Paris Move Bohemia","C London Move Paris"])
process(["A Munich Support B","B Bohemia Move Prussia","C Prussia Hold", "D Warsaw Move Munich"])
process(["A Munich Support B",
        "B Bohemia Support C",
        "C Warsaw Support A",
        "D SF Move Munich",
        "E Oakland Move Bohemia",
        "F Burlingame Move Warsaw"])
process(["A Munich Support D",
                "B Bohemia Support D",
                "C Craig Support J",
                "D Prussia Move France",
                "E Warsaw Support I",
                "F Burlingame Support I",
                "G Millbrae Support I",
                "H Frankton Support J",
                "I Clayton Move France",
                "J Michael Move France",
                "K Spain Support D",
                "L Lombard Support I"])

