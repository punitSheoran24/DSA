class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.strip().split(' ')
        reverse_string = ''
        n = len(words)
        for i in range(n - 1, -1, -1):
            if words[i]:
                reverse_string += words[i] + ' '
        return reverse_string.strip()