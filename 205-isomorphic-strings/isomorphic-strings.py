# class Solution:
#     def isIsomorphic(self, s: str, t: str) -> bool:
#         map = {}
#         for i in range(len(s)):
#             if s[i] not in map and t[i] not in map.values():
#                 map[s[i]] = t[i]
#             elif not map.get(s[i], 0) == t[i]:
#                 return False

#         return True
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        smap = {}
        tmap = {}
        for i in range(len(s)):
            if s[i] not in smap:
                smap[s[i]] = i
            if t[i] not in tmap:
                tmap[t[i]] = i
            if smap[s[i]] != tmap[t[i]]:
                return False
        return True