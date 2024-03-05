class Node:
    def __init__(self):
        self.children = {}
        self.iscomplete = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
        node.iscomplete = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.iscomplete

    def prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def delete(self, word):
        self.delete_helper(self.root, word, 0)

    def delete_helper(self, node, word, index):
        if index == len(word):
            if node.iscomplete:
                node.iscomplete = False
            return

        char = word[index]
        if char not in node.children:
            return

        child_node = node.children[char]
        self.delete_helper(child_node, word, index + 1)
        if not child_node.iscomplete and not child_node.children:
            del node.children[char]

    def suggest(self, prefix):
        suggestions = []
        node = self.root
        for char in prefix:
            if char not in node.children:
                return suggestions
            node = node.children[char]

        self._get_suggestions(node, prefix, suggestions)
        return suggestions

    def _get_suggestions(self, node, current_prefix, suggestions):
        if node.iscomplete:
            suggestions.append(current_prefix)

        for char, child_node in node.children.items():
            self._get_suggestions(child_node, current_prefix + char, suggestions)

    def print_trie(self):
        self._print_trie(self.root, "", 0)

    def _print_trie(self, node, current_word, depth):
        if node.iscomplete:
            print("  " * depth + current_word)

        for char, child_node in node.children.items():
            self._print_trie(child_node, current_word + char, depth + 1)


# Example usage:
trie = Trie()
words = ["apple", "apricot", "banana", "bat"]
for word in words:
    trie.insert(word)

print("Search 'apple':", trie.search("apple"))
print("Prefix 'ba':", trie.prefix("ba"))

print("\nTrie structure:")
trie.print_trie()

prefix = "ba"
suggestions = trie.suggest(prefix)
print(f"\nSuggestions for prefix '{prefix}': {suggestions}")

trie.delete("apple")
print("\nTrie structure after deleting 'apple':")
trie.print_trie()
