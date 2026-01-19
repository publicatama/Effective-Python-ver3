#-----------------------------------------
#アンパック構文

def get_stats(numbers):
    return min(numbers), max(numbers)

lengths = [63, 73, 72, 60, 67, 66, 71, 61, 72, 70]
minimum, maximum = get_stats(lengths) #２つの返り値
print(f"min: {minimum}, Max: {maximum}")
#結果がタプルで返され、それをアンパックして得られている

#-----------------------------------------
first, second = 1,2
assert first == 1
assert second == 2

def my_function():
    return 1, 2

first, second = my_function()
assert first == 1
assert second == 2
#-----------------------------------------

def get_avg_ratio(numbers):
    average = sum(numbers) / len(numbers)
    scaled = [x / average for x in numbers]
    scaled.sort(reverse = True)
    return scaled

longest, *middle, shortest = get_avg_ratio(lengths)
print(f"longest: {longest:>4.0%}")
print(f"Shortest: {shortest:>4.0%}")

#-----------------------------------------
def get_median(numbers):
    count = len(numbers)
    sorted_numbers = sorted(numbers)
    middle = count // 2
    if count % 2 == 0:
        lower = sorted_numbers[middle -1]
        upper = sorted_numbers[middle]
        median = (lower + upper) / 2
    else:
        median = sorted_numbers[middle]
    return median

def get_stats_more(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    count = len(numbers)
    average = sum(numbers) / count
    median = get_median(numbers)
    return minimum, maximum, average, median, count

minimum, maximum, average, median, count = get_stats_more(lengths)
print({minimum}, {maximum})
print({average}, {median}, {count})

#正
minimum, maximum, average, median, count = get_stats_more(lengths)
#誤！
minimum, maximum,  median, average, count = get_stats_more(lengths)
   
print({minimum}, {maximum})
print({average}, {median}, {count})

#行を折り返す必要もある（PEP8に従うと）
minimum, maximum, average, median, count = get_stats_more(
    lengths)

minimum, maximum, average, median, count = get_stats_more(lengths)
    
(minimum, maximum, average, 
 median, count) = get_stats_more(lengths)

(minimum, maximum, average, median, count
) = get_stats_more(lengths)

#長すぎるアンパックは使わない　
#な長すぎる場合は、軽量クラスを使ってインスタンスを繰り返す方がいい

from dataclasses import dataclass

@dataclass
class Stats:
    minimum: float
    maximum: float
    average: float
    median: float
    count: int

def get_stats_obj(numbers):
    return Stats(
        minimum = min(numbers),
        maximum = max(numbers),
        count = len(numbers),
        average = sum(numbers) / len(numbers),
        median = get_median(numbers),
    )

result = get_stats_obj(lengths)
print(result)














