class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        reverse_string = words[::-1]
        return " ".join(reverse_string)