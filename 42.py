#-----------------------------------------
#代入式を使って内包表記の繰り返しを減らす
stock = {
    "nails": 125,
    "screws": 35,
    "wingnuts": 8,
    "washers": 24,   
}

order = ["screws", "wingnuts", "clips"]

def get_batches(count, size):
    return count // size

result = {}
for name in order:
    count = stock.get(name, 0)
    batches = get_batches(count, 8) #最低出荷基準を8とする
    if batches:
        result[name] = batches
        
print(result)

found = {
    name: get_batches(stock.get(name, 0), 8)
    for name in order
    if get_batches(stock.get(name, 0), 8)
}

has_bug = {
    name: get_batches(stock.get(name, 0), 4)
    for name in order
    if get_batches(stock.get(name, 0), 8)
}
print("Expected:", found)
print("Found:", has_bug)

#👆だと同じ文を複数個所に配置しており、間違えることもあるので内容表記に代入式を使ってみる

found1 = {
    name : batches for name in order if (batches := get_batches(stock.get(name, 0),8))
}

print("Expected1:", found1)
#-----------------------------------------

#内包表記の中で定義されたtenthを内包表記の外で参照しようとするとエラーとなる
'''
result = {name: (tenth := count // 10) for name, count in stock.items() if tenth > 0}
'''

#修正👇 外で定義した変数を中で参照するように書き換え
result = {name: tenth for name, count in stock.items() if (tenth := count // 10) > 0}
print(result)

half = [(squared := last**2) for count in stock.values() if (last := count // 2) > 10]
print(f"Last item of {half} is {last}**2 = {squared}")

for count in stock.values():
    last = count // 2
    squared = last**2

print(f"{count} // 2 = {last}; {last} ** 2 = {squared}")

half = [count1 // 2 for count1 in stock.values()]
print(half)
#print(count1) #エラー

found = (
    (name, batches) for name in order if (batches := get_batches(stock.get(name, 0), 8))
)
print(next(found))
print(next(found))
#print(next(found)) #ここでもう枯れているのでエラーとなる
