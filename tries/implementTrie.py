from string import digits, ascii_uppercase, ascii_lowercase

def insertInTrie(root, word):

    while word:
        letter = word.pop()
        if letter in root.suffixDict:
            root = root.suffixDict[letter]
        else:
            newTrieNode = TrieNode(letter)
            root.suffixDict[letter] = newTrieNode
            root = root.suffixDict[letter]
        
    root.wasFinal = True

class TrieNode:
    def __init__(self, letter):
        self.suffixDict = {}
        self.wasFinal = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word: str) -> None:

        if word is None or len(word) == 0:
            return None

        word = list(word)
        word = word[::-1]
        insertInTrie(self.root, word)

        return

    def search(self, word: str) -> bool:
        word = list(word)
            
        root = self.root
        for letter in word:
            if letter in root.suffixDict:
                root =  root.suffixDict[letter]
            else:
                return False
        
        return root.wasFinal


    def startsWith(self, prefix: str) -> bool:
        prefix = list(prefix)
        root = self.root
        for letter in prefix:
            if letter in root.suffixDict:
                root = root.suffixDict[letter]
            else:
                return False
            
        return True
