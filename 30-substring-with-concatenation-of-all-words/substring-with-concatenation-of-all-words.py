# from collections import defaultdict


# class Solution:
#     def findSubstring(self, s: str, words: list[str]) -> list[int]:
#         d = defaultdict(int)
#         for word in words:
#             d[word] += 1
#         n = len(s)
#         n1 = len(words[0])
#         res = []
#         left = right = 0
#         d_copy = d.copy()
#         while right < n:
#             if s[right: right + n1] in d_copy:
#                 left = right
#                 while s[left: left + n1] in d_copy and d_copy[s[left: left + n1]] != 0:
#                     d_copy[s[left:left + n1]] -= 1
#                     left += n1
#                 temp = False
#                 for val in d_copy.values():
#                     if val != 0:
#                         temp = True
#                 if not temp:
#                     res.append(right)
#                 d_copy = d.copy()
#             right += 1
#         return res

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        d = defaultdict(int)
        for word in words:
            d[word] += 1
        n = len(s)
        n1 = len(words[0])
        word_len = n1 * len(words)
        res = []
        left = right = 0
        for right in range(n - word_len + 1):
            if s[right: right + n1] in d:
                d_copy = defaultdict(int)
                left = right
                for _ in range(len(words)):
                    if s[left: left + n1] in d:
                        d_copy[s[left:left + n1]] += 1
                        left += n1
                    else:
                        break
                if d_copy == d:
                    res.append(right)
        return res