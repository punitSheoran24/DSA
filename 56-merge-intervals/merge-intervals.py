class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        res = []
        i = 0
        inter = sorted(intervals, key=lambda x: x[0])
        while i < len(inter):
            start, end = inter[i][0], inter[i][1]
            while i + 1 < len(inter) and end >= inter[i + 1][0]:
                if not start <= inter[i][0]:
                    start = inter[i + 1][0]
                if not end >= inter[i + 1][1]:
                    end = inter[i + 1][1]
                i += 1
            res.append([start, end])
            i += 1

        return res