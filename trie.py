from collections import defaultdict

class Trie():
    def __init__(self):
        self.root = Node()

    def build(self, word ):
        self.__build(word, 0, self.root)

    def __build(self, word, i, node):
        if i >= len(word):
            return

        nextnode = node.add(word,i)

        self.__build(word, i + 1 , nextnode)

    def getWords(self):
        return self.__getWords(self.root)

    ## get the words of some node
    def __getWords(self, node):
        ans = []
        ans.extend( node.words)

        for child in node.childs.values():
            ans.extend(self.__getWords(child))

        return ans


    ## return the largest prefix if two or more words have common prefix
    def wordsWihtLargestCommonPrefix(self):
        largest = [-1]
        largestNode =[None]

        self.__wordsWihtLargestCommonPrefix(self.root, 1, largest, largestNode)

        node = largestNode[0]

        if node == None:
            ## means no common prefix words
            assert largest[0] == -1
            return (-1, None)

        return (largest[0], self.__getWords(node))

    def __wordsWihtLargestCommonPrefix(self, node, depth, largest, largestNode):
        for c, child in node.childs.items():
            if child.nums >= 2:
                if depth > largest[0]:
                    largest[0] = depth
                    largestNode[0] = child

                self.__wordsWihtLargestCommonPrefix(child, depth + 1, largest, largestNode)


class Node():
    def __init__(self):
        self.childs = defaultdict(Node)

        self.nums = 0 # NO. of words going through this node
        self.words = [] # only store the words in the leaf



    def add(self, word, i):
        c = word[i]
        if self.childs.get(c) == None:
            self.childs[c] = Node()

        node = self.childs[c]
        node.nums += 1

        if i == len(word) - 1:
            node.words.append(word)
        return node

