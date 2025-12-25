#-----------------------------------------------
counters = {
    "pumpernickel" : 2,
    "sourdough" : 1,
}

key = "wheat"

if key in counters:
    count = counters[key]
else:
    count = 0

counters[key] = count + 1
print(counters)

try:
    count = counters[key]
except KeyError:
    count = 0
counters[key] = count + 1

#これが一番いい！
count = counters.get(key,0)
counters[key] = count + 1

#ここから👇は全部見づらい
if key not in counters:
    counters[key] = 0
counters[key] += 1

if key in counters:
    counters[key] += 1
else:
    counters[key] = 1

try:
    counters[key] += 1
except KeyError:
    counters[key] = 1
    
#-----------------------------------------------
#辞書が複雑なとき

votes = {
    "baguette" : ["Bob", "Alice"],
    "ciabatta" : ["Coco", "Deb"],
}

key = "brioche"
who = "Elmer"
if key in votes:
    names = votes[key]
else:
    votes[key] = names = []
names.append(who)
print(votes)

key = "Bob"
who = "Elmer"

try:
    names = votes[key]
except KeyError:
    votes[key] = names = []

names.append(who)

names = votes.get(key)
if names is None:
    votes[key] = names = []
names.append(who)

#可読性高いif
if (names:= votes.get(key)) is None:
    votes[key] = names = []
names.append(who)

names = votes.setdefault(key, [])
names.append(who)

#-----------------------------------------------
#setdefaultについて

data = {}
key = "foo"
value = []

data.setdefault(key, value)
print("Before", data) #ここでfooがキーに代入されちゃう

value.append("hello")
print("After", data)

count = counters.setdefault(key, 0)
counters[key] = count + 1

#あまりsetdefaultが最適な場合はなさそう
#カウンタのような単純な辞書の場合は、getメソッドが一番よい
