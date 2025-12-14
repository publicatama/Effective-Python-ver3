#-----------------------------------------------
search_key = "red"
my_dict = {"red": 1, "blue": 2, "green": 3}
#エラー
"""
for key in my_dict:
    if key == "blue":
        my_dict["yellow"] = 4

        
#エラー
for key in my_dict:
    if key == "blue":
        del my_dict["green"]
"""

for key in my_dict:
    if key == "blue":
        my_dict["green"] = 4
print(my_dict)

#-----------------------------------------------
my_set = {"red", "blue", "green"}
#エラー
"""
for color in my_set:
    if color == "blue":
        my_set.add("yellow")
"""
#問題なし
for color in my_set:
    if color == "blue":
        my_set.add("green")
print(my_set)

#-----------------------------------------------

my_list = [1, 2, 3]
for number in my_list:
    print(number)
    if number == 2:
        my_list[0] = -1

print(my_list)

"""
my_list = [1,2,3]
for number in my_list:
    print(number)
    if number == 2:
        my_list.insert(0, 4)
"""
#👆は無限ループとなる（何回も2番目の要素が次にくるため

#👇イテレータの現在位置以降ならOK
my_list = [1,2,3]
for number in my_list:
    print(number)
    if number == 2:
        my_list.append(4)

print(my_list)

#-----------------------------------------------

my_dict = {"red": 1, "blue": 2, "green": 3}
keys_copy = list(my_dict.keys()) #コピーする

for key in keys_copy:
    if key == "blue":
        my_dict["green"] = 4

print(my_dict)

my_list = [1,2,3]
list_copy = list(my_list)

for number in list_copy:
    print(number)
    if number == 2:
        my_list.insert(0, 4)
print(my_list)


my_set = {"red", "blue", "green"}
set_copy = set(my_set) #コピー

for color in set_copy:
    if color == "blue":
        my_set.add("yellow")
print(my_set)


#動作が遅くなりそうなときは。。
my_dict = {"red": 1, "blue": 2, "green": 3}
modifications = {}

for key in my_dict:
    if key == "blue":
        modifications["green"] = 4
my_dict.update(modifications)

print(my_dict)

#いてレート中には反映されないことに注意
my_dict = {"red": 1, "blue": 2, "green": 3}
modifications = {}

for key in my_dict:
    if key == "blue":
        modifications["green"] = 4
    value = my_dict[key]
    if value == 4:
        modifications["yellow"] = 5
my_dict.update(modifications)

print(my_dict)

#修正したもの👇
my_dict = {"red": 1, "blue": 2, "green": 3}
modifications = {}

for key in my_dict:
    if key == "blue":
        modifications["green"] = 4
    value = my_dict[key]
    other_value = modifications.get(key)
    if value == 4 or other_value == 4:
        modifications["yellow"] = 5
my_dict.update(modifications)
print(my_dict)
#-----------------------------------------------