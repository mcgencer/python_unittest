import unittest
from buyukbul import buyukbul
class MyTestCase(unittest.TestCase):
    def test_buyukbul(self):
        self.assertEqual((buyukbul(1,2,3)), (buyukbul(1,2,3)))
        self.assertEqual((buyukbul(9,3,5)), (buyukbul(4,6,9)))
        self.assertEqual((buyukbul(1,2,3)), (buyukbul(4,3,5))) #hatalı

if __name__ == '__main__':
    unittest.main()
