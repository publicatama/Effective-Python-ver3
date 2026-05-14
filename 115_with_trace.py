#-----------------------------------------
#tracemallocでスタックトレースを出す

import tracemalloc

tracemalloc.start(10)
time1 = tracemalloc.take_snapshot()

import waste_memory

x = waste_memory.run()
time2 = tracemalloc.take_snapshot()

stats = time2.compare_to(time1, "traceback")
top = stats[0]
print("Biggest offender is:")
print("\n".join(top.traceback.format()))

#こんな感じ
#Biggest offender is:
#  File "c:\Users\disor\Desktop\effectivePython\115_with_trace.py", line 11
#    x = waste_memory.run()
#  File "c:\Users\disor\Desktop\effectivePython\waste_memory.py", line 19
#    deep_values.append(get_data())
#  File "c:\Users\disor\Desktop\effectivePython\waste_memory.py", line 12
#    obj = MyObject()
#  File "c:\Users\disor\Desktop\effectivePython\waste_memory.py", line 7
#    self.data = os.urandom(100)
