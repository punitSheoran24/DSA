
class Trie:
    def __init__(self):
        self.root={}

    def insert(self, word: str) -> None:
        h=self.root
        for w in word:
            if w not in h:
                h[w]={}
            h=h[w]
        h['.']='.'
        

    def search(self, word: str) -> bool:
        h=self.root
        for w in word:
            if w not in h:
                return False
            h=h[w]
        return '.' in h

    def startsWith(self, prefix: str) -> bool:
        h=self.root
        for w in prefix:
            if w not in h:
                return False
            h=h[w]
        return True


        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)