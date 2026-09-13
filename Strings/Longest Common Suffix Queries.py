#3093. Longest Common Suffix Queries

class TrieNode:
    def __init__(self):
        self.children = {}
        self.index = -1
        self.length = float('inf')


class Solution:
    def stringIndices(self, wordsContainer, wordsQuery):

        root = TrieNode()

        # insert reversed words into trie
        for i, word in enumerate(wordsContainer):

            rev = word[::-1]
            node = root

            # update best answer at root
            if len(word) < node.length:
                node.length = len(word)
                node.index = i

            for ch in rev:

                if ch not in node.children:
                    node.children[ch] = TrieNode()

                node = node.children[ch]

                # store shortest word index
                if len(word) < node.length:
                    node.length = len(word)
                    node.index = i

        ans = []

        # process queries
        for word in wordsQuery:

            rev = word[::-1]
            node = root

            for ch in rev:

                if ch not in node.children:
                    break

                node = node.children[ch]

            ans.append(node.index)

        return ans   