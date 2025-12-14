#-----------------------------------------------
i = 3
x = "even" if i % 2 == 0 else "odd"
print(x)

#-----------------------------------------------
def fail():
    raise Exception("Ooprs")

x = fail() if False else 20
print(x)
#-----------------------------------------------

result = [x / 4 for x in range(10) if x % 2 == 0]
print(result)

#-----------------------------------------------
x = (i % 2 == 0 and "even") or "odd"

#-----------------------------------------------
if i % 2 == 0:
    x = "even"
else:
    x = "odd"
    
#-----------------------------------------------    
if i % 2 == 0:
    x = "even"
    print("It was even!")
else:
    x = "odd"
#-----------------------------------------------
if i % 2 == 0:
    x = "even"
elif i % 3 == 0:
    x = "divisble by three"
    print("It was even!")
else:
    x = "odd"
#-----------------------------------------------    
def number_group(i):
    if i % 2  == 0:
        return "even"
    else:
        return "odd"
x = number_group(i)
#----------------------------------------------- 

#長すぎ
"""
x = (my_log_function_call(1,2,3) if i % 2 == 0 else my_other_long_function_call(4,5,6))

x = (
    my_log_function_call(1,2,3) 
    if i % 2 == 0 
    else my_other_long_function_call(4,5,6)
)
"""

#----------------------------------------------- 
#代入式はかっこで囲む必要アリ
"""
x=2
y=1

if x and (z := x > y):

if x and z := x > y:  #エラーになる
"""
#----------------------------------------------- 
#条件式はかっこで囲む必要なしだけどわかりづらくなる
"""
x=2
y=1
 
if x>y if z else w: #わからん
if x> (y if z else w): #わかる
"""

#----------------------------------------------- 
"""
z = dict(
    your_value=(y := 1),
)

#エラー
w = dict(
    other_value=y := 1,
)
"""
#----------------------------------------------- 
v = dict(
    my_value =1 if x else 3,
)
#----------------------------------------------- 