class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1=set(nums1)
        s2=set(nums2)
        lst1=[]
        for num in s1:
            if num not in s2:
                lst1.append(num)
        lst2=[]
        for num in s2:
            if num not in s1:
                lst2.append(num)
        
        return [lst1,lst2]
        