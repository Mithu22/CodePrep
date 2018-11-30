class FilePath:
    def __init__(self):
        self.pathmap = {}

    def create(self,path,val):
        if self.pathmap.get(path) is not None:
            return "Error"
        lastslash = path.rfind("/")
        subpath  = self.pathmap.get(path[:lastslash])
        if lastslash > 0 and subpath is None:
            return "Error"
        self.pathmap[path] = val
        return "Success"

    def get(self,path):
        return self.pathmap.get(path,"Error")

f = FilePath()
print(f.create("/a",1))
print(f.get("/a"))
print(f.create("/a/b",2))
print(f.get("/a/b"))
print(f.create("/c/d",1))
print(f.get("/c"))

