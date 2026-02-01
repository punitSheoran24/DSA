class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        i = 0
        j = k
        longest = 0
        vowel = {'a', 'e', 'i', 'o', 'u'}
        for n in range(k):
            if s[n] in vowel:
                longest += 1
        temp = longest
        while j < len(s):
            if s[j] in vowel:
                temp += 1
            if s[i] in vowel:
                temp -= 1
            j += 1
            i += 1
            longest = max(longest, temp)
        return longest
