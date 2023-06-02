import main
import unittest

class IntegerArithmeticTestCase(unittest.TestCase):
        def testAdd(self):  
        # test method names begin with 'test'

            self.assertEqual((1 + 2), 3)
            self.assertEqual(0 + 1, 1)

if __name__ == '__main__':
        unittest.main()