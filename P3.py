class Lists:
    def __init__(self,inputlist):
        self.input = inputlist
        self.row = 0
        self.col = 0
        self.rflag = 0

    def hasNext(self):
        if len(self.input) == 0 or self.input is None:
            return False

        r = self.row
        c = self.col

        while r < len(self.input):
            if c < len(self.input[r]):
                return True
            else:
                r += 1
                c = 0
        return False

    def __repr__(self):
        for i in self.input:
            print(i)

    def next(self):
        if self.hasNext():
            val = self.input[self.row][self.col]
            self.rflag = 1
            self.col += 1
            if self.col >= len(self.input[self.row]):
                self.col = 0
                self.row += 1
            return val

    def remove(self):
        try:
            if self.rflag:
                r = self.row
                c = self.col
                if c == 0:
                    r-=1
                    c = len(self.input[r])-1
                    l = self.input[r]
                else:
                    c -= 1
                    l = self.input[r]
                del(l[c])
                if len(l)==0:
                    self.input.remove(l)
                    self.row-=1
                if self.col > 0:
                    self.col-=1
                self.rflag = 0
            else:
                raise Exception("Remove called without a next")
        except Exception as inst:
            print(type(inst))
            print(inst.args[0])



lt = Lists([[1,2],[3,4,5],[6,7]])
print(lt.hasNext())
print(lt.next())
lt.remove()
print(lt.next())
lt.remove()
print(lt.next())
lt.remove()
print(lt.next())
print(lt.next())
print(lt.next())
print(lt.next())
lt.remove()
print(lt.remove())
lt.__repr__()
