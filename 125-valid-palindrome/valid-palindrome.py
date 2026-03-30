class Solution:
    def isPalindrome(self, s: str) -> bool:
        res=''
        for x in s.lower():
            if x.isalnum():
                res+=x
        return res==res[::-1]
        