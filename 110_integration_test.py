#-----------------------------------------
#integration_test.pyを定義する

from unittest import TestCase,main

def setUpModule():
    print("* Module setUp")

def tearDownModule():
    print("* Module clean-up")

class IntegrationTest(TestCase):
    def setUp(self):
        print("* Test setUp")
        
    def tearDown(self):
        print("* Test clean-up")
    
    def test_end_to_end1(self):
        print("* Test 1")
    
    def test_end_to_end2(self):
        print("* Test 2")
        
if __name__ == "__main__":
    main()

