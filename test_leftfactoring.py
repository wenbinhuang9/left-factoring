import unittest


from  leftfactoring import  leftFactoring
class MyTestCase(unittest.TestCase):
    def test_left_factoring(self):

        leftFactoring("./production")

if __name__ == '__main__':
    unittest.main()
