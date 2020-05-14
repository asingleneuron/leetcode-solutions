class Node:
    def __init__(self):
        self.keys = {}
        self.next = None
        self.wordends = False


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = None

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        root = self.root

        for ch in word:
            # print(ch)
            if self.root is None:
                self.root = Node()
                root = self.root
                root.keys[ch] = Node()
                root = root.keys[ch]
            elif ch not in root.keys:
                root.keys[ch] = Node()
                root = root.keys[ch]
            else:
                root = root.keys[ch]
                # root.keys[ch] = Node()
                # print("Handle this")
        root.wordends = True

    def display(self):
        print(self.root)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        # self.display()
        # print("In search of : ",word)
        if self.root is None:
            return False

        root = self.root
        for w in word:
            # print(w, root.keys)
            if w not in root.keys:
                return False
            else:
                root = root.keys[w]

        return root.wordends

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        # print("In startsWith of : ",prefix)
        if self.root is None:
            return False

        root = self.root
        for w in prefix:
            # print(w, root.keys)
            if w not in root.keys:
                return False
            else:
                root = root.keys[w]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)