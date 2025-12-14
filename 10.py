#----------------------------------------------- 
a= b"h\x65llo"
print(type(a))
print(list(a))
print(a)

a="a\0300 propos"
print(type(a))
print(list(a))
print(a)
#----------------------------------------------- 

def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode("utf-8")
    else:
        value = bytes_or_str
    return value

print(repr(to_str(b"foo")))
print(repr(to_str("bar")))


def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode("utf-8")
    else:
        value = bytes_or_str
    return value

print(repr(to_str(b"foo")))
print(repr(to_str("bar")))
#----------------------------------------------- 

print(b"one" + b"two")
print("one" + "two")

#----------------------------------------------- 
#b"one" + "two" #エラー
#"one" + b"two" #エラー

assert b"red" > b"blue"
assert "red" > "blue"

#assert b"red" > "blue" #エラー
#assert "red" < b"blue" #エラー

print(b"foo" == "foo")

blue_bytes = b"blue"
blue_str = "blue"
print(b"red %s" % blue_bytes) 
print("red %s" % blue_str)

#print(b"red %s" % blue_str) #エラー

print("red %s" % blue_bytes)
print(f"red {blue_bytes}")

#----------------------------------------------- 
#with open("data.bin", "w") as f:
#    f.write(b"\xf1\xf2\xf3\xf4\xf5")
#エラー

with open("data.bin", "wb") as f:
    f.write(b"\xf1\xf2\xf3\xf4\xf5")
    
#with open("data.bin", "r") as f:
#    data = f.read()
#エラー

with open("data.bin", "rb") as f:
    data = f.read()
assert data == b"\xf1\xf2\xf3\xf4\xf5"

with open("data.bin", "r", encoding = "cp1252") as f:
    data = f.read()
assert data == "ñòóôō"
#----------------------------------------------- 
