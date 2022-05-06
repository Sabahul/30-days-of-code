##  inheritance

class level1:
    height='7ft'
    weight='60'
class level2(level1):
    def groot(self):
        print("access")
        pass
obj = level2()
obj.height
obj.groot()
class level3(level2):
    def system(self):
        print("correct")
obj = level3()
obj.groot()
obj.system()
print(obj.height)
print(obj.weight)
