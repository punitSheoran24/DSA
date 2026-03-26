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
            res[min(n,c)]+=1
        h = n
        c = res[n]
        while c<h:
            h-=1
            c += res[h]
        return h
