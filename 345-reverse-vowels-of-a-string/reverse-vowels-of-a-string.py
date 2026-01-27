class Solution:
    def reverseVowels(self, s: str) -> str:
        print(s)
        vowels = ['a', 'e', 'i', 'o', 'u']
        str_list = list(s)
        i = 0
        j = len(s) - 1
        while i < j:
            if str_list[i].lower() in vowels and str_list[j].lower() in vowels:
                str_list[i], str_list[j] = str_list[j], str_list[i]
                i += 1
                j -= 1
            if str_list[i].lower() not in vowels:
                i += 1
            if str_list[j].lower() not in vowels:
                j -= 1
        return ''.join(str_list)
