class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        s1 = set(word1)
        s2 = set(word2)
        if s1 != s2 or len(word1) != len(word2):
            return False
        dic1 = {}
        dic2 = {}
        for i in range(len(word1)):
            if word1[i] in dic1:
                dic1[word1[i]] += 1
            if word1[i] not in dic1:
                dic1[word1[i]] = 1
            if word2[i] in dic2:
                dic2[word2[i]] += 1
            if word2[i] not in dic2:
                dic2[word2[i]] = 1

        if sorted(dic1.values()) == sorted(dic2.values()):
            return True
        return False