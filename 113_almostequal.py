#-----------------------------------------
#トーストのユニットテスト

from unittest import TestCase, main

class MyTestCase3(TestCase):
    def test_equal(self):
        a = 1e24 / 1.1e16
        b = 1e24 / 1.101e16
        self.assertAlmostEqual(90.9e6, a, delta=0.1e6)
        self.assertAlmostEqual(90.9e6, b, delta=0.1e6)
    
if  __name__ == "__main__":
    main()