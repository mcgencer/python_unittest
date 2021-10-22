import unittest
from buyukbul import buyukbul
class MyTestCase(unittest.TestCase):
    def test_buyukbul(self):
        self.assertNotEqual((buyukbul(1,2,3)), (buyukbul(4,5,6)))
        self.assertNotEqual((buyukbul(8,5,7)), (buyukbul(9,2,1)))
        self.assertNotEqual((buyukbul(1,1,2)), (buyukbul(2,2,2))) #hatalı

if __name__ == '__main__':
    unittest.main()
