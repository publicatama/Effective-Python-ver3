#-----------------------------------------------
x = ["red", "orange", "yellow", "green", "blue", "purple"]
odds = x[::2]
evens = x[1::2]
print(odds)
print(evens)

x = b"mongoose"
y = x[::-1]
print(y)

x = "寿司"
y = x[::-1]
print(y)

"""
エラー
w = "寿司"
x = w.encode("utf-8")
y = x[::-1]
z = y.decode("utf-8")
"""

#-----------------------------------------------

x = ["a", "b", "c", "d", "e", "f", "g", "h"]
print(x[::2])
print(x[::-2])

print(x[2::2])
print(x[-2::-2])
print(x[-2:2:-2])
print(x[2:2:-2])

#-----------------------------------------------

y = x[::2]
z = y[1:-1]
print(y)
print(z)

#-----------------------------------------------
