#-----------------------------------------------
a = ["a","b","c","d","e","f","g","h"]
print("Middle two:  ", a[3:5])
print("All but ends:", a[1:7])

assert a[:5] == a[0:5]
assert a[5:] == a[5:len(a)]

print(a[:])
print(a[:5])
print(a[:-1])
print(a[4:])
print(a[-3:])
print(a[2:5])
print(a[2:-1])
print(a[-3:-1])

first_twenty_items = a[:20]
print(first_twenty_items)
last_twenty_items = a[-20:]
print(last_twenty_items)

#エラー👇存在しない
#print(a[20])
#-----------------------------------------------

b = a[3:]
print("Before:  ", b)
b[1] = 99
print("After:   ", b)
print("No change:", a)

#-----------------------------------------------

print("Before ", a)
a[2:7] = [99,22,14]
print("After  ",a)

print("Before ", a)
a[2:3] = [47,11]
print("After  ",a)

b = a[:]
assert b == a

#-----------------------------------------------

b = a
print("Before a", a)
print("Before b", b)
a[:] = [101,102,103]
assert a is b
print("After a", a)
print("After b", b)

#-----------------------------------------------