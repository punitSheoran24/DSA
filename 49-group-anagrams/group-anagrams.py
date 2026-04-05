class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map={}
        for i in range(len(strs)):
            sort=sorted(strs[i])

            if ''.join(sort) in map:
                map[''.join(sort)].append(strs[i])
            else:
                map[''.join(sort)]=[strs[i]]
        
        return list(map.values())

            


        

        