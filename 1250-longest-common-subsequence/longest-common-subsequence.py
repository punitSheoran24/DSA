class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        prev = [0] * (m + 1)
        lst = [0] * (m + 1)
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    lst[j + 1] = prev[j] + 1
                else:
                    lst[j + 1] = max(lst[j + 1], lst[j])
            prev = lst[:]

        return lst[-1]
