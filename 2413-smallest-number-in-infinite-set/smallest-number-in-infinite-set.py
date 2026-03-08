import heapq
class SmallestInfiniteSet:

    def __init__(self):
        self.s=set()
        self.cur=1
        

    def popSmallest(self) -> int:
        if self.s:
            min_val=min(self.s)
            self.s.remove(min_val)
            return min_val

        else:
            self.cur+=1
            return self.cur-1
        

    def addBack(self, num: int) -> None:
        if self.cur>num:
            self.s.add(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)