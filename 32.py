#-----------------------------------------
#Noneを返さずに例外を送る

def careful_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

x, y = 1, 0
result = careful_divide(x, y)
if result is None:
    print("無効な入力")
    
#以下は誤り（無効な入力ではないから）    
x, y = 0, 5
result = careful_divide(x, y)
if not result:
    print("無効な入力")
    
#-----------------------------------------
#返り値を２つのタプルに

def careful_divide(a, b):
    try:
        return True, a / b
    except ZeroDivisionError:
        return False, None
    
success, result = careful_divide(x, y)
if not success:
    print("無効な入力")
else:
    print(result)

_, result = careful_divide(x, y)
if not result:
    print("無効")

#-----------------------------------------
#Noneを返さない方法

def careful_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        raise ValueError("無効な入力です")
    
x, y = 5, 1
try:
    result = careful_divide(x, y)
except ValueError:
    print("無効な入力です")
else:
    print(f"結果は {result:.1f} です")
    

#-----------------------------------------
#型アノテーションを使う方法

def careful_divide(a:float, b:float) -> float:
    """aをbで割る。
        
    Raises:
        ValueError: 入力が無効で割り算できない場合
    """
    try:
        return a/b
    except ZeroDivisionError:
        raise ValueError("無効入力")

try:
    result = careful_divide(1, 5)
except ValueError:
    print("無効入力")
else:
    print(f"結果は {result:.1f}です")
    
#これで入力、例外、出力がすべて明らかになり、呼び出し元が間違えるかのうせいが低い
