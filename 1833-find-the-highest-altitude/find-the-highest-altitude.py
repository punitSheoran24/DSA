class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        max_altitude = 0
        sum = 0
        for n in gain:
            sum += n
            max_altitude = max(max_altitude, sum)
        return max_altitude