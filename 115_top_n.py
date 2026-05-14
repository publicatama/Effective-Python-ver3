#-----------------------------------------
#tracemallocを使ってみる

import tracemalloc

tracemalloc.start(10)
time1 = tracemalloc.take_snapshot()

import waste_memory

x = waste_memory.run()
time2 = tracemalloc.take_snapshot()

stats = time2.compare_to(time1, "lineno")
for stat in stats[:3]:
    print(stat)



#こんな感じに出る👇
#c:\effectivePython\waste_memory.py:7: size=1299 KiB (+1299 KiB), count=10000 (+10000), average=133 B
#c:\effectivePython\waste_memory.py:12: size=785 KiB (+785 KiB), count=10000 (+10000), average=80 B
#c:\effectivePython\waste_memory.py:13: size=84.4 KiB (+84.4 KiB), count=100 (+100), average=864 B

このサイズやカウントを調べればどのオブジェクトがプログラムのメモリをどれぐらい食っているかわかる。

