#-----------------------------------------
#トーストの統合テスト

from unittest import TestCase, main
from unittest.mock import Mock
from toaster import Toaster, ReusableTimer

class ToasterIntegrationTest(TestCase):
    
    def setUp(self):
        self.timer = ReusableTimer()
        self.toaster = Toaster(self.timer)
        self.toaster.doneness = 0


    def test_wait_finish(self):
        self.assertFalse(self.toaster.hot)
        self.toaster.push_down()
        self.assertTrue(self.toaster.hot)
        self.timer.timer.join()
        self.assertFalse(self.toaster.hot)
        
    def test_cansel_early(self):
        self.assertFalse(self.toaster.hot)
        self.toaster.push_down()
        self.assertTrue(self.toaster.hot)
        self.toaster.pop_up()
        self.assertFalse(self.toaster.hot)


if  __name__ == "__main__":
    main()