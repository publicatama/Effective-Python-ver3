#-----------------------------------------
#トーストのユニットテスト

from unittest import TestCase, main
from unittest.mock import Mock
from toaster import Toaster, ReusableTimer

class ToasterUnitTest(TestCase):
    
    def test_start(self):
        timer = Mock(spec=ReusableTimer)
        toaster = Toaster(timer)
        toaster.push_down()
        self.assertTrue(toaster.hot)
        timer.countdown.assert_called_once_with(30,toaster.pop_up)

    def test_end(self):
        timer = Mock(spec=ReusableTimer)
        toaster = Toaster(timer)
        toaster.hot = True
        toaster.pop_up()
        self.assertFalse(toaster.hot)
        timer.end.asssert_callsed_once()

if  __name__ == "__main__":
    main()