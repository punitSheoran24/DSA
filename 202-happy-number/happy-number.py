class Solution:
    def isHappy(self, n: int) -> bool:
        map={n}
        while n!=1:
            s=0
            while n>0:
                r=n%10
                n//=10
                s+=r*r
            if s in map:
                return False
            n=s
            map.add(s)
        return True
            
            