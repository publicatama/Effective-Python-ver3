#-----------------------------------------------
def normalize(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result

visits = [15, 35, 80]
percentages = normalize(visits)
print(percentages)
assert sum(percentages) == 100.0

#-----------------------------------------------
def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)
            
it = read_visits("my_numbers.txt")
percentages = normalize(it)
print(percentages)

#👆これだとイテレータが燃え尽きているのでダメ

#-----------------------------------------------
#イテレータの出力結果を別のリストに保存する
def normalize(numbers):
    numbers_copy = list(numbers)
    total = sum(numbers_copy)
    result = []
    for value in numbers_copy:
        percent = 100 * value / total
        result.append(percent)
    return result

it = read_visits("my_numbers.txt")
percentages = normalize(it)
print(percentages)


#これだと、ジェネレータに対しても動作する

#-----------------------------------------------
#メモリの問題に対処する
def normalize_func(get_iter):
    total = sum(get_iter())
    result = []
    for value in get_iter():
        percent = 100 * value / total
        result.append(percent)
    return result

path  = "my_numbers.txt"
percentages = normalize_func(lambda: read_visits(path))
print(percentages)
assert sum(percentages) == 100.0
#-----------------------------------------------
#都度lambdaを呼び出すのは面倒なので、iterメソッドをクラスに実装する

class ReadVisits:
    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)

visits  = ReadVisits(path)
percentages = normalize_func(lambda: read_visits(path))
print(percentages)
assert sum(percentages) == 100.0

#-----------------------------------------------

def normalize_defensive(numbers):
    if iter(numbers) is numbers: #イテレータ　イテレーションできるものじゃないとダメ
        raise TypeError("コンテナを提供してください")
    total = sum(numbers)
    result = []
    
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result

#-----------------------------------------------

from collections.abc import Iterator

def normalize_defensive(numbers):
    if isinstance(numbers, Iterator): #イテレータ　イテレーションできるものじゃないとダメ
        raise TypeError("コンテナを提供してください")
    total = sum(numbers)
    result = []
    
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result

#-----------------------------------------------

visits_list = [15, 35, 80]
list_percentages = normalize_defensive(visits_list)

visits_obj = ReadVisits(path)
obj_percentages = normalize_defensive(visits_obj)

assert list_percentages == obj_percentages
assert sum(percentages) == 100.0

#-----------------------------------------------

visits = [15, 35, 80]
it = iter(visits)
normalize_defensive(it)

#-----------------------------------------------