#-----------------------------------------------
import random

def flip_coin():
    if random.randint(0, 1) == 0:
        return "Heads"
    else:
        return "Tails"

def flip_is_heads():
    return flip_coin() == "Heads"

flips = [flip_is_heads() for _ in range(20)]
all_heads = False not in flips

#20回も実行する必要がない改善👇
all_heads = True
for _ in range(100):
    if not flip_is_heads():
        all_heads = False 
        break
"""
print("All truthy:")
print(all([1, 2, 3]))
print(1 and 2 and 3)

print("One Falsey:")
print(all([1, 0, 3]))
print(1 and 0 and 3)
"""

#allを使った記載
all_heads = all(flip_is_heads() for _ in range(3))
#print(all_heads)

#正しくない👇
#all_heads = all([flip_is_heads() for _ in range(20)])

def repeated_is_heads(count):
    for _ in range(count):
        yield flip_is_heads() #ジェネレータ
all_heads = all(repeated_is_heads(3))
#print(all_heads)



def flip_is_tails():
    return flip_coin() == "Tails"

"""
print("All Falsey:")
print(any([0, False, None]))
print(0 or False or None)#-----------------------------------------------

print("One Truthy:")
print(any([None, 3, 0]))
print(None or 3 or 0)
"""

all_heads = not any(flip_is_tails() for _ in range(3))
#print(all_heads)

def repeated_is_tails(count):
    for _ in range(count):
        yield flip_is_tails() #ジェネレータ
all_heads = not any(repeated_is_tails(3))

#-----------------------------------------------
for a in (True, False):
    for b in (True, False):
        assert any([a, b]) == (not all([not a, not b]))
        assert all([a, b]) == (not any([not a, not b]))
#見知ったド・モルガンの法則
#-----------------------------------------------