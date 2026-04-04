class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map = {}
        for i in range(len(s)):
            if s[i] not in map and t[i] not in map.values():
                map[s[i]] = t[i]
            elif not map.get(s[i], 0) == t[i]:
                return False

        return True