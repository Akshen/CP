"""
3 Functions 
- Insert
- Search
- Startswith

"""

class TreeNode:

    def __init__(self, value):
        self.value = value
        self.children = {}
        self.endhere = False

class Trie:
    def __init__(self):
        """
        Initialize your data structure here
        """
        self.root = TreeNode(None)

    def insert(self, word):
        """
        Inserts a word into the trie
        """
        parent = self.root
        size = len(word)
        for i, char in enumerate(word):
            if char not in parent.children:
                parent.children[char] = TreeNode(char)
            parent = parent.children[char]
            if i==(size-1):
                parent.endhere = True
        
    def search(self, word):
        parent = self.root
        for char in word:
            if char not in parent.children:
                return False
            parent = parent.children[char]
        return parent.endhere

    def startwith(self, initials):
        parent = self.root
        for char in initials:
            if char not in parent.children:
                return False
            parent = parent.children[char]
        return True

triee = Trie()
triee.insert("Akshen")
print(triee.search("Akshen"))
print(triee.search("D"))
print(triee.startwith("Ak"))
print(triee.startwith("D"))
