class TrieNode:
    
    def __init__(self, value):
        self.value = value
        self.children = {}
    
    def add_child(self, word):
        if not word:
            return

        c = word[0]
        if c not in self.children:
            self.children[c] = TrieNode(c)
        self.children[c].add_child(word[1:])
    
    def child(self, char):
        if char not in self.children:
            return None
        return self.children[char]


class Trie:

    def __init__(self):
        self.members = {}
        self.words = set()

    def insert(self, word: str) -> None:
        if not word:
            return

        self.words.add(word)
        c = word[0]
        if c not in self.members:
            self.members[c] = TrieNode(c)
        self.members[c].add_child(word[1:])


    def search(self, word: str) -> bool:
        return word in self.words
        

    def startsWith(self, prefix: str) -> bool:
        c = prefix[0]
        if c not in self.members:
            return False
        
        curr_node = self.members[c]
        curr_idx = 0
        while curr_idx < len(prefix) - 1:
            curr_node = curr_node.child(prefix[curr_idx + 1])
            if not curr_node:
                return False
            curr_idx += 1
        return True