import unittest
from kucukbul import kucukbul
class MyTestCase(unittest.TestCase):
    def test_kucukbul(self):
        self.assertNotEqual((kucukbul(1,2,3)), (kucukbul(2,5,6)))
        self.assertNotEqual((kucukbul(4,3,3)), (kucukbul(3,2,7)))
        self.assertNotEqual((kucukbul(6,4,3)), (kucukbul(4,3,5))) #hatalı

if __name__ == '__main__':
    unittest.main()
