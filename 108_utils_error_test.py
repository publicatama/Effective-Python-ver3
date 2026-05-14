#-----------------------------------------
#例外を検証するコンテキストマネージャ

from unittest import TestCase, main
from 108_utils import to_str

class UtilsErrorTestCase(TestCase):
    def test_to_str_bad(self):
        with self.assertRaises(TypeError):
            to_str(object())
    
    def test_to_str_bad_encoding(self):
        with self.assertRaises(UnicodeDecodeError):
            to_str(b"\xfa\xfa")
    
    def test_failing(self):
        self.assertEqual("incorrect", to_str("hello"))
    
if __name__ == "__main__":
    main()
