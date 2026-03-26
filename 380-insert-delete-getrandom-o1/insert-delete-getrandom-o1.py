import random
class RandomizedSet:

    def __init__(self):
        self.s={}
        self.lst=[]
        

    def insert(self, val: int) -> bool:
        if val in self.lst:
            return False
        self.lst.append(val)
        self.s[val]=len(self.lst)-1
        return True
        

    def remove(self, val: int) -> bool:
        if not val in self.lst:
            return False
        idx=self.s[val]
        self.lst[idx]=self.lst[-1]
        self.s[self.lst[-1]] = idx
        self.lst.pop()
        del self.s[val]

        return True
        

    def getRandom(self) -> int:
        index = random.randint(0, len(self.lst) - 1)
        return self.lst[index]
        

