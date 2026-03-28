class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n1 = len(needle)
        n2 = len(haystack)
        if n1 > n2:
            return -1
        for i in range(n2):
            if haystack[i : n1 + i] == needle:
                return i
        return -1
