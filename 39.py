#-----------------------------------------
#グルー関数にはlambda式よりfunctools.partialを優先する
import functools
import math

def log_sum(log_total, value):
    log_value = math.log(value)
    return log_total + log_value

result = functools.reduce(log_sum, [10, 20, 40], 0)
print(math.exp(result))

#-----------------------------------------

def log_sum_alt(value, log_total):
    log_value = math.log(value)
    return log_total + log_value

result = functools.reduce(
    lambda total, value: log_sum_alt(value, total),
    [10, 20, 40], 0)
print(math.exp(result))

#修正が一回きりなら👆のlambda関数でもいいが、何回もあるのであればヘルパー関数を使おう

def log_sum_for_reduce(total, value):
    return log_sum_alt(value, total)

#ここちょっと日本語変
#追加の情報を渡す場合

def logn_sum(base, logn_total, value): #変更済み
    logn_value = math.log(value, base)
    return logn_total + logn_value

#底の情報を変更する場合を考えたいが、reduceに直接追加することはできない
#lambdaを使うのは一つの手

result = functools.reduce(
    lambda total, value: logn_sum(10, total, value), #変更済み
    [10, 20, 40],
    0,
)

print(math.pow(10, result))

#このように一部の引数を特定の値に固定して、残りは通常通り渡す
#今回だと底を特定の値にして、totalやvalueはそのまま

#このような処理をするとき、functoolsにpartial()という便利な関数がある

result = functools.reduce(
    functools.partial(logn_sum, 10), #変更済み
    [10, 20, 40],
    0,
)

def log_sum_last(logn_total, value, *, base=10): #新しいキーワード引数
    logn_value = math.log(value, base)
    return logn_total + logn_value

log_sum_e = functools.partial( log_sum_last, base = math.e) #baseをeに固定
print(log_sum_e(3, math.e**10))

#lambdaでも書けるがエラーが出やすい
log_sum_e_alt = lambda *a, base=math.e, **kw: log_sum_last(*a, base=base, **kw)

print(log_sum_e.args, log_sum_e.keywords, log_sum_e.func)

#partialは便利なので、基本的にこちらを使うべき。しかし、引数の順序の編子はできないことからその場合はlambdaを使うしかない。
#大半の場合は、これだけでは足りない。単純な関数インターフェースの一部として状態を参照したり変更したりする必要がある。

