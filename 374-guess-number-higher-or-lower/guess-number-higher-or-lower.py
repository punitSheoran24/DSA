# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        start,end=1,n
        if guess(end)==0:
            return end
        if guess(start)==0:
            return start
        while True:
            mid=(start+end)//2
            print(mid)
            g=guess(mid)
            if g==1:
                start=mid
            elif g==-1:
                end=mid
            else:
                return mid
        

