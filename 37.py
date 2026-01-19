#-----------------------------------------
#キーワード専用と位置専用引数で明確さを強調したい

#ZeroDivisionErro例外が発生したらfloat("inf")を返し、OverflowError例外が発生したら0を返すような処理

def safe_division(
    number,
    divisor,
    ignore_overflow,
    ignore_zero_division,
):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float("inf")
        else:
            raise

result1 = safe_division(1.0, 10**500, True, False)
print(result1)

result2 = safe_division(1.0, 0 ,False, True)
print(result2)

#👆のコードではブール値引数の位置を混同しやすくなっている
#これについては、デフォルト引数を使えば関数は常に例外を適用できるようになる

def safe_division_b(
    number,
    divisor,
    ignore_overflow=False,
    ignore_zero_division=False,
):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float("inf")
        else:
            raise
        
result3 = safe_division_b(1.0, 10**500, ignore_overflow=True)
print(result3)

result4 = safe_division_b(1.0, 0 ,ignore_zero_division=True)
print(result4)

assert safe_division_b(1.0, 10**500, True, False) == 0

#このような複雑な関数については、関数呼び出しの意味が明確になる要因キーワード専用引数を使う。

def safe_division_c(
    number,
    divisor,
    *, #追加
    ignore_overflow=False,
    ignore_zero_division=False,
):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float("inf")
        else:
            raise
        
#safe_division_c(1.0, 10**500, True, False)  #👈これは位置引数で参照できない
        

result5 = safe_division_b(1.0, 0 ,ignore_zero_division=True)
print(result5) #キーワード引数とデフォルト値は機能！

try:
    result = safe_division_c(1.0, 0)
except ZeroDivisionError:
    pass

assert safe_division_c(number=2, divisor=5) == 0.4
assert safe_division_c(divisor=5, number=2) == 0.4
assert safe_division_c(2, divisor=5) ==0.4
#👆みたいに位置とキーワード引数を混ぜて渡しちゃうかも

'''👇はエラーになっちゃう引数名変えたから
def safe_division_d(
    numerator, #変更済み
    denominator, #変更済み
    *,
    ignore_overflow=False,
    ignore_zero_division=False,
):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float("inf")
        else:
            raise

safe_division_d(number=2, divisor=5)
'''

def safe_division_e(
    numerator, 
    denominator,
    /, #追加
    *,
    ignore_overflow=False,
    ignore_zero_division=False,
):
    try:
        return numerator / denominator
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float("inf")
        else:
            raise
   
assert safe_division_e(2, 5) == 0.4



def safe_division_f(
    numerator, 
    denominator,
    /,
    ndigits = 10, #変更済み
    *,
    ignore_overflow=False,
    ignore_zero_division=False,
):

    try:
        fraction = numerator / denominator #変更済み
        return round(fraction, ndigits) #変更済み
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float("inf")
        else:
            raise
        
result7 = safe_division_f(22,7)
print(result7)

result8 = safe_division_f(22,7,5)
print(result8)

result9 = safe_division_f(22,7,ndigits=2)
print(result9)
#ndigitsは/と*の間に置いているので、位置でもキーワード引数でもOK
