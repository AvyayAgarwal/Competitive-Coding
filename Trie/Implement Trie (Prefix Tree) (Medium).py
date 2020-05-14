# 208. Implement Trie (Prefix Tree) - Medium
# Tags - Design, Trie

class TrieNode:
    def __init__(self, char):
        self.char = char
        self.endFlag = False
        self.children = {}

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode("*")
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        currNode = self.root
        for ch in word:
            if ch in currNode.children:
                currNode = currNode.children[ch]
            else:
                currNode.children[ch] = TrieNode(ch)
                currNode = currNode.children[ch]
        currNode.endFlag = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        currNode = self.root
        for ch in word:
            if ch in currNode.children:
                currNode = currNode.children[ch]
            else:
                return False
        return currNode.endFlag 

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        currNode = self.root
        for ch in prefix:
            if ch in currNode.children:
                currNode = currNode.children[ch]
            else:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)