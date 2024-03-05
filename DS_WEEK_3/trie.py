class Node:
    def __init__(self):
        self.children = {}
        self.iscomplete=False
class Trie():
    def __init__(self):
        self.root=Node()
    def insert_to(self,word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
        node.iscomplete = True
   
    def search(self,word):
        node=self.root
        for char in word:
            if char not in node.children:
                return False
            node=node.children[char]
        return node.iscomplete
    
    
    def print_trie(self):
        self._print_trie(self.root,'')
    def _print_trie(self,node,current_node):
        if node.iscomplete:
            print(current_node)
        for char ,child_node in node.children.items():
            self._print_trie(child_node,current_node+char)
    def prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def suggest(self,prifix):
        suggestion=[]
        node=self.root
        for char in prefix:
            if char not in node.children:
                return suggestion
            node=node.children[char]
        self._suggestion_trie(node,prifix,suggestion)
        return suggestion
    def _suggestion_trie(self,node,current_prifix,suggestion):
        if node.iscomplete:
            suggestion.append(current_prifix)
        for char,child_node in node.children.items():
            self._suggestion_trie(child_node,current_prifix+char,suggestion)
    def delete(self,word):
        self._delete_helper(self.root,word,0)
    def _delete_helper(self,node,word,index):
        if index==len(word):
            if node.iscomplete:
                node.iscomplete=False
            return
        char=word[index]
        if char not in node.children:
            return
        child_node=node.children[char]
        self._delete_helper(child_node,word,index+1)
        if not child_node.iscomplete and not child_node.children:
            del node.children[char]



    


trie=Trie()
# t.print_trie()
word = ["apple", "apricot", "banana", "bat"]
for words in word:
    trie.insert_to(words)

trie.print_trie()
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
print(trie.search("apple"))


