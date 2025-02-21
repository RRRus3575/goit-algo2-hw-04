class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.value = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def put(self, word, value=0):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        node.value = value
    
    
    

class LongestCommonWord(Trie):

    def find_longest_common_word(self, strings) -> str:
        if strings is None or not isinstance(strings, list):
            return ""
        if not strings:  
            return ""
        if not all(isinstance(word, (str, int, float)) for word in strings):
            return ""
        
        strings = [str(word) for word in strings]

        for word in strings:
            self.put(word)

        node = self.root
        prefix = ""

        while node and len(node.children) == 1 and not node.is_end_of_word:
            char = next(iter(node.children))
            prefix += char
            node = node.children[char]
        
        return prefix

if __name__ == "__main__":
    # Тести
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""

    trie = LongestCommonWord()
    strings = [{"key":1}, {"key":1}]
    assert trie.find_longest_common_word(strings) == ""
