class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.value = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def put(self, word, value):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        node.value = value
    
    def _collect(self, node, prefix):
            words = []
            if node.is_end_of_word:
                words.append((prefix, node.value))
            for char, next_node in node.children.items():
                words.extend(self._collect(next_node, prefix + char))
            return words
    
    def keys_with_prefix(self, prefix):        
        node = self.root
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return []
        return self._collect(node, prefix)
    
    def find_words_with_suffix(self, suffix):
        words = [word[0] for word in self._collect(self.root, "")]   
        return [word for word in words if word.endswith(suffix)]
    

class Homework(Trie):
    def count_words_with_suffix(self, pattern) -> int:
        return len(self.find_words_with_suffix(pattern))

    def has_prefix(self, prefix) -> bool:
       result = self.keys_with_prefix(prefix)
       return bool(result)

if __name__ == "__main__":
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    for i, word in enumerate(words):
        trie.put(word, i)

    # Перевірка кількості слів, що закінчуються на заданий суфікс
    assert trie.count_words_with_suffix("e") == 1  # apple
    assert trie.count_words_with_suffix("ion") == 1  # application
    assert trie.count_words_with_suffix("a") == 1  # banana
    assert trie.count_words_with_suffix("at") == 1  # cat

    # Перевірка наявності префікса
    assert trie.has_prefix("app") == True  # apple, application
    assert trie.has_prefix("bat") == False
    assert trie.has_prefix("ban") == True  # banana
    assert trie.has_prefix("ca") == True  # cat
