#-----------------------------------------------
my_test1 = "hello" "world"
my_test2 = "hello" + "world"
assert my_test1 == my_test2
#-----------------------------------------------

x = 1
my_test1 = (
    r"first \part is here with escapes\n, "
    f"string interpokation {x} in here, "
    'this has  "double quotes" inside'
)
print(my_test1)

#-----------------------------------------------

y = 2
my_test2 = r"fir\st" f"{y}" '"third"'
print(my_test2)

my_test3 = r"fir\st", f"{y}" '"third"'
print(my_test3)

my_test4 = [
    "first line\n",
    "second line\n",
    "thied line\n",
]
print(my_test4)

my_test5 = [
    "first line\n",
    "second line\n"
    "thied line\n",
]
print(my_test5)

my_test5 = [
    "first line\n",
    "second line\n" "thied line\n",
]
print(my_test5)

my_test6 = [
    "first line\n",
    "second line\n"
    + "thied line\n",
]
assert my_test5 == my_test6

my_test6 = [
    "first line\n",
    "second line\n" + "thied line\n",
]

#-----------------------------------------------

print("this is my long message "
      "that should be printed out")

#-----------------------------------------------

import sys 

print("this is my long message "
      "that should be printed out",
      end="",
      file=sys.stderr)

#-----------------------------------------------

"""
value = Mydata(123,
                first_value,
                f"my format string {x}"
                f"another value {y}",
                "and here is more text",
                secon_value,
                stream=sys.stderr)

value2 = Mydata(123,
                first_value, 
                f"my format string {x}" + #明示的に結語を記載する
                f"another value {y}",
                "and here is more text",
                secon_value,
                stream=sys.stderr)
                
"""

#-----------------------------------------------