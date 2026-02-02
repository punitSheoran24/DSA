class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        dictionary = {}
        for n in arr:
            if n in dictionary:
                dictionary[n] += 1
            else:
                dictionary[n] = 1
        s = {val for val in dictionary.values()}
        if len(s) == len(dictionary):
            return True
        return False
