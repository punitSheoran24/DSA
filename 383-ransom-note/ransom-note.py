class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote)>len(magazine):
            return False
        d = defaultdict(int)
        for s in magazine:
            d[s]+=1
        for s in ransomNote:
            if s not in d or d[s]<=0:
                return False
            d[s]-=1
        return True
        