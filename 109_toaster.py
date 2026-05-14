#-----------------------------------------
#トーストクラス

class Toaster:
    def __init__(self,timer):
        self.timer = timer
        self.doneness = 3
        self.hot = False

    def _get_duration(self):
        return max(0.1, min(120, self.doneness * 10))
    
    def push_down(self):
        if self.hot:
            return 
        self.hot = True
        self.timer.countdown(self._get_duration(), self.pop_up)
        
    def pop_up(self):
        print("Pop!") #Return the spring
        self.hot = False
        self.timer.end()
    
import threading

class ReusableTimer:
    def __init__(self):
        self.timer = None
    
    def countdown(self, duration, callback):
        self.end()
        self.timer = threading.Timer(duration, callback)
        self.timer.start()
    
    def end(self):
        if self.timer:
            self.timer.cancel()

#---------------------------------------
#toaster = Toaster(ReusableTimer())
#print("Initially hot:  ", toaster.hot)
#toaster.doneness = 1
#toaster.push_down()
#print("After Push down:", toaster.hot)
#print("After time:"   ,toaster.hot)


