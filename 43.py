#-----------------------------------------
#リストではなくジェネレータ

def index_words(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == " ":
            result.append(index +1)
    return result

address = "Four score and seven years ago I love like believe..."
result = index_words(address)
print(result[:10])

#👆のコードは可読性低。可読性をあげつつ段階的に結果を生成するジェネレータ
def index_words_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == " ":
            yield index + 1

it = index_words_iter(address)
print(next(it))
print(next(it))

#結果はyield式に渡される
#ジェネレータから返されたイテレータを組み込み関数list()に渡せば簡単にリストにできる

result = list(index_words_iter(address))
print(result[:10])

#index_words()の問題は結果がすべてリストに保存されてから返ること　メモリ消費がでかくなるかも

def index_file(handle):
    offset = 0
    for line in handle:
        if line:
            yield offset
        for letter in line:
            offset += 1
            if letter == " ":
                yield offset

'''
with open("address.txt", "r") as f:
    it = index_file(f)
    result = itertools.islice(it, 0, 10)
    print(list(result))
'''
#👆は1行ずつ読み込むので、消費メモリも最大1行分に抑えられる。

#リストを返すのではなくジェネレータを返すようにすると、メモリ消費も抑えれるし可読性もあがることがある！
#ジェネレータから返されるイテレータはジェネレータ関数のほんたいないのyield式に渡された値を生成
