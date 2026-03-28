class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        n = len(strs[0])
        if n == 0:
            return ""
        common = ''
        for i in range(n):
            temp = common + strs[0][i]
            for j in range(len(strs)):
                if strs[j][:i + 1] != temp:
                    return common
            common = temp
        return common