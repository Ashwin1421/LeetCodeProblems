class Node:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.flag = False

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tree = {}
        self.root = Node("")

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = Node(char)
            curr = curr.children[char]

        curr.flag = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """

        curr = self.root
        for char in word:
            if curr.children.get(char) is None:
                return False
            if curr.children[char]:
                curr = curr.children[char]

        if curr.flag:
            return True
        else:
            return False



    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        curr = self.root
        for char in prefix:
            if curr.children.get(char) is None:
                return False
            if curr.children[char]:
                curr = curr.children[char]

        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)