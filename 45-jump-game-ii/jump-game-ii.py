# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         near = far = jumps = 0

#         while far < len(nums) - 1:
#             farthest = 0
#             for i in range(near, far + 1):
#                 farthest = max(farthest, i + nums[i])
            
#             near = far + 1
#             far = farthest
#             jumps += 1
        
#         return jumps
class Solution:
    def jump(self, nums: list[int]) -> int:
        res = 0
        l = r = 0
        while r < len(nums) - 1:
            temp = r
            for i in range(l, r + 1):
                r = max(r, i + nums[i])
            l = temp + 1
            res += 1

        return res

