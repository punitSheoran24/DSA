class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        pairs=[]
        potions.sort()
        for spell in spells:
            start,end=0,len(potions)-1
            while start<end:
                mid=(start+end)//2
                if spell*potions[mid]>=success:
                    end=mid
                else:
                    start=mid+1
            if potions[start]*spell>=success:
                pairs.append(len(potions)-start)
            else:
                pairs.append(0)
        return pairs
            
        
        