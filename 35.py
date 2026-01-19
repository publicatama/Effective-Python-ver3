#-----------------------------------------
#キーワード引数

def remainder(number, divisor):
    return number % divisor

assert remainder(20, 7) == 6

#いろんな組み合わせ
remainder(20,7)
remainder(20, divisor=7)
remainder(number = 20, divisor = 7)
remainder(divisor = 7, number = 20) #逆でもいい！

#位置引数はキーワード引数の前に置かないといけない　👇はエラーになる
'''remainder(number=20 , 7)
'''

#各引数は一度だけ指定できる 下もnumberを2回指定しようとしているのでエラー
'''remainder(20 , number = 7)  
'''

#-----------------------------------------
my_kwargs = {
    "number": 20,
    "divisor": 7,
}
assert remainder(**my_kwargs) == 6

my_kwargs2 = {
    "divisor": 7,
}
assert remainder(number = 20, **my_kwargs2) == 6

my_kwargs3 = {
    "number": 20,
}

other_kwargs = {
    "divisor": 7,
}
assert remainder(**my_kwargs3, **other_kwargs) == 6


def print_parameter(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

print_parameter(alpha = 1.5, beta = 9, gamma = 4)

#キーワードが引数が備える利点 ３つある
#1.初見で関数呼び出しの意味吾明確になること
#remainder(20, divisor=7)これとかわかりづらいよね

#2.関数定義時にデフォルト値を定義できること

def flow_rate(weight_diff, time_diff):
    return weight_diff / time_diff

weight_a = 2.5
weight_b = 3
time_a = 1
time_b = 4
weight_diff = weight_b - weight_a
time_diff = time_b - time_a
flow = flow_rate(weight_diff, time_diff)
print(f"{flow:.3} kg per second")

#改良
def flow_rate(weight_diff, time_diff, period):
    return (weight_diff / time_diff) * period

flow_per_second = flow_rate(weight_diff, time_diff,1)
#これで毎回1を振るのは面倒なのでデフォルトで1を設定してしまおう

def flow_rate(weight_diff, time_diff, period=1):
    return (weight_diff / time_diff) * period

flow_per_second = flow_rate(weight_diff, time_diff)
flow_per_hour = flow_rate(weight_diff, time_diff, period = 3600)


#3.既存の関数呼び出し元と互換性を保ちつつ関数に引数を追加しやすい
#さらに、1kgあたりの流量を計算したいとする

def flow_rate(weight_diff, time_diff, period=1, units_per_kg=1):
    return ((weight_diff / time_diff) / time_diff) * period

pounds_per_hour = flow_rate(
    weight_diff,
    time_diff,
    period= 3600,
    units_per_kg=2.2,
)

print(pounds_per_hour)

#唯一の問題点はデフォルト値付きキーワード引数が位置引数として渡されること

pounds_per_hour = flow_rate(weight_diff, time_diff, 3600, 2.2)
#これだと3600や2.2が何を表すかわからない

#デフォルト値付きキーワード引数は、常にキーワード付き引数として渡すようにすること（位置引数に絶対にしない！）

