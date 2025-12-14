#----------------------------------------------- 
#print("foo bar")

my_value = "foo bar"
print(str(my_value))
print("%s" % my_value)
print(f"{my_value}")
print(format(my_value))
print(my_value.__format__("s"))
print(my_value.__str__())
#----------------------------------------------- 

int_value = 5
str_value = "5"
print(int_value)
print(str_value)
print(f"Is {int_value} == {str_value}?")

#----------------------------------------------- 

a = "\x07"
print(repr(a))

b = eval(repr(a))

assert a == b

print(repr(int_value))
print(repr(str_value))

print("Is %r == %r?" % (int_value, str_value))
print(f"Is {int_value!r} == {str_value!r}?")

#----------------------------------------------- 

class OpaqueClass:
    def __init__(self,x,y):
        self.x = x
        self.y = y

obj = OpaqueClass(1, "foo")
print(obj)


#改善
class BetterClass:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"BetterClass({self.x!r}, {self.y!r})"

obj = BetterClass(2, "bar")
print(obj)
print(str(obj))

#strの返り血を人間が読みやすくする
class StringifiableBetterClass(BetterClass):
    def __str__(self):
        return f"({self.x}, {self.y})"
    
obj2 = StringifiableBetterClass(2,"bar")
print("Human Readable:", obj2)
print("Printable:", repr(obj2))
#-----------------------------------------------