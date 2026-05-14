#-----------------------------------------
#TeatCaseでテスト実装.

from unittest import TestCase, main
from 108_utils import to_str

class UtilsTestCase(TestCase):
    def test_to_str_bytes(self):
        self.assertEqual("hello", to_str(b"hello"))
    
    def test_to_str_str(self):
        self.assertEqual("hello", to_str("hello"))
    
    def test_failing(self):
        self.assertEqual("incorrect", to_str("hello"))
    
if __name__ == "__main__":
    main()
    
#エラー内容
#Traceback (most recent call last):
#  File "c:\Users\disor\Desktop\effectivePython\108_utils_test.py", line 15, in test_failing
#    self.assertEqual("incorrect", to_str("hello"))
#    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#AssertionError: 'incorrect' != 'hello'
#- incorrect
#+ hello

#----------------------------------------------------------------------
#Ran 3 tests in 0.002s
#FAILED (failures=1)

