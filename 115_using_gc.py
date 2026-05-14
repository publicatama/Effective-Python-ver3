#-----------------------------------------
#gcを使ってみる

import gc

found_objects = gc.get_objects()
print("Before:", len(found_objects))

import waste_memory

hold_reference = waste_memory.run()

found_objects = gc.get_objects()
print("After: ", len(found_objects))
for obj in found_objects[:3]:
    print(repr(obj)[:100])

#こんな感じに出る👇
#Before: 5288
#After:  16352
#<waste_memory.MyObject object at 0x000001C96A1A06E0>
#<waste_memory.MyObject object at 0x000001C96A1A0730>
#<waste_memory.MyObject object at 0x000001C96A1A0780>

