class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        len1 = len(s)
        len2 = len(t)
        i = j = 0
        while i < len1 and j < len2:
            if t[j] == s[i]:
                i += 1
            j += 1
        if i == len1:
            return True
        return False