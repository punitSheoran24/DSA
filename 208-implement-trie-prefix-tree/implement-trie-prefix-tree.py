class Node:
    def __init__(self):
        self.children={}
        self.end=False

class Trie:

    def __init__(self):
        self.root=Node()
    def insert(self, word: str) -> None:
        head=self.root
        for w in word:
            if w not in head.children:
                head.children[w]=Node()
            head=head.children[w]
        head.end=True
        

    def search(self, word: str) -> bool:
        head=self.root
        for w in word:
            if w not in head.children:
                return False
            head=head.children[w]
        if not head.end:
            return False
        return True


        

    def startsWith(self, prefix: str) -> bool:
        head=self.root
        for w in prefix:
            if w not in head.children:
                return False
            head=head.children[w]
        return True


        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)