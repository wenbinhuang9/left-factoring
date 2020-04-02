import unittest

from  trie import  Trie
class MyTestCase(unittest.TestCase):
    def test_trie(self):
        trie = Trie()

        string_list = ["hello", "hellow", "hel"]
        for word in string_list:
            trie.build(word)

        words = trie.getWords()
        print(words)
        self.assertEqual(len(words) == len(string_list), True)

        self.assertEqual(all([word in string_list for word in words]), True)

    def test_largestCommonPrefix(self):
        string_list = ["hello", "hellow", "hel"]

        trie = Trie()

        for word in string_list:
            trie.build(word)

        longest, words = trie.wordsWihtLargestCommonPrefix()

        print(longest)
        print (words)

        self.assertEqual(longest == 5, True)

        result = ["hello", "hellow"]
        self.assertEqual(all([word in result for word in words]), True)

        string_list = ["ai", "aii", "aiii", "aiiii", "aiiiii", "aiiiiii"]

        for word in string_list:
            trie.build(word)

        longest, words = trie.wordsWihtLargestCommonPrefix()

        self.assertEqual(longest == 6, True)
        result = ["aiiiii", "aiiiiii"]

        print(words)
        self.assertEqual(all([word in result for word in words]), True)


if __name__ == '__main__':
    unittest.main()
