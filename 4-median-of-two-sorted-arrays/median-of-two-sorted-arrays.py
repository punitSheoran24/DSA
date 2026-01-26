class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1 = sorted(nums1)
        n = len(nums1)
        print(nums1)
        if n % 2 == 0:
            n1 = (n // 2) - 1
            n2 = (n // 2)
            return float((nums1[n1] + nums1[n2]) / 2)

        else:
            return float(nums1[n // 2])


        
        