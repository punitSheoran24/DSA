class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        res = []
        i = 0
        while i < len(asteroids):
            if asteroids[i] > 0 or len(res) == 0 and asteroids[i] < 0:
                res.append(asteroids[i])
            elif asteroids[i] < 0 and len(res) > 0:
                if res[-1] < 0:
                    res.append(asteroids[i])
                elif res[-1] < abs(asteroids[i]):
                    res.pop()
                    continue
                elif abs(res[-1]) == abs(asteroids[i]):
                    res.pop()
            i += 1
        return res