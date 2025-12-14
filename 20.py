#-----------------------------------------------
"""
for i in range(3):
    print(f"Inside {i=}")
print(f"After  {i=}")
"""

#-----------------------------------------------
"""
categories = ["Hydrogen", "Uranium", "Iron", "Other"]
for i, name in enumerate(categories):
    if name == "Iron":
        break
print(i)

for i, name in enumerate(categories):
    if name == "Lithium":
        break
print(i)

"""
#-----------------------------------------------
#リストが空のためエラーとなる
categories = []
for i, name in enumerate(categories):
    if name == "Lithium":
        break
print(i)


#-----------------------------------------------
my_numbers = [37, 13, 128, 21]
found = [i for i in my_numbers if i % 2 == 0]
print(i)

#このようにループが終わったあとにループ変数が取得できるが使わない方がいい（エラーが起きることもある）

#-----------------------------------------------