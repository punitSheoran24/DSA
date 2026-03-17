class Solution:
    def countBits(self, n: int) -> list[int]:
        def helper(n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            binary = format(n, 'b')
            return 1 + helper(int(binary[1:], 2))

        res = []
        for i in range(n + 1):
            res.append(helper(i))
        return res
