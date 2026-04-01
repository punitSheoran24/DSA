class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = set()
        res = 0
        left = 0
        n = len(s)
        for right in range(n):
            if s[right] not in map:
                res = max(res, (right - left) + 1)
            else:
                while s[right] in map:
                    map.remove(s[left])
                    left += 1
            map.add(s[right])

        return res