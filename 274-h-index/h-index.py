# class Solution:
#     def hIndex(self, citations: list[int]) -> int:
#         n = len(citations)
#         h = 0
#         for i in range(1, n + 1):
#             count = 0
#             for j in range(n):
#                 if i <= citations[j]:
#                     count += 1
#             if count >= i:
#                 h = max(h, i)
#         return h
class Solution:
    def hIndex(self, citations: list[int]) -> int:
        n = len(citations)
        res = [0] * (n + 1)

        for c in citations:
            if c > n:
                res[n] += 1
            else:
                res[c] += 1
        h = 0
        c = 0
        for i in range(len(res) - 1, -1, -1):
            c += res[i]
            if c >= i and i > h:
                h = i

        return h
