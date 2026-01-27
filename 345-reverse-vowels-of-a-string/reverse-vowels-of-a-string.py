class Solution:
    def reverseVowels(self, s: str) -> str:
        print(s)
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        str_list = list(s)
        i = 0
        j = len(s) - 1
        while i < j:
            if str_list[i] in vowels and str_list[j] in vowels:
                str_list[i], str_list[j] = str_list[j], str_list[i]
                i += 1
                j -= 1
            elif str_list[i] in vowels:
                j -= 1
            elif str_list[j] in vowels:
                i += 1
            else:
                i += 1
                j -= 1
        return ''.join(str_list)