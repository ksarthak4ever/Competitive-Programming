class TrieNode():
    def __init__(self, val = None):
        self.val = val
        self.isEnd = False
        self.children = {}

class Autocomplete():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for l in word:
            if l not in cur.children:
                cur.children[l] = TrieNode(l)
            cur = cur.children[l]
        cur.isEnd = True 

    def search(self, word):
        cur = self.root
        for l in word:
            if l in cur.children:
                cur = cur.children[l]
            else:
                return False
        return cur.isEnd

    def startsWith(self, prefix):
        cur = self.root
        for l in prefix:
            if l in cur.children:
                cur = cur.children[l]
            else:
                return False
        return True

test = Autocomplete()
test.insert('Sarthak')
test.insert('Kumar')
print(test.startsWith('Sa'))