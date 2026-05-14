#-----------------------------------------
#トーストのユニットテスト

from unittest import TestCase, main
from unittest import mock
from toaster import Toaster, ReusableTimer
import threading

class ReusableTimerUnitTest(TestCase):
    
    def test_countdown(self):
        my_func = lambda: None
        with mock.patch("threading.Timer"):
            timer = ReusableTimer()
            timer.countdown(0.1, my_func)
            threading.Timer.assert_called_once_with(0,1, my_func)
            timer.timer.start.assert_called_once()
            
    def test_countdown(self):
        my_func = lambda: None
        with mock.patch("threading.Timer"):
            timer = ReusableTimer()
            timer.countdown(0.1, my_func)
            timer.end()
            timer.timer.cancel.assert_called_once()

if  __name__ == "__main__":
    main()