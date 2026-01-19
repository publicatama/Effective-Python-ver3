#-----------------------------------------
#スター引数について

def log(message, values):
    if not values:
        print(message)
    else:
        values_str = ", ".join(str(x) for x in values)
        print(f"{message}: {values_str}")
    
log("私の数字は", [1,2])
log("こんにちは", []) 

#-----------------------------------------
#スター引数を使ってみる

def log(message, *values):
    if not values:
        print(message)
    else:
        values_str = ", ".join(str(x) for x in values)
        print(f"{message}: {values_str}")
    
log("私の数字は", [1,2])
log("こんにちは")

#-----------------------------------------
#アンパックと似ている
favorite = [7, 33, 99]
log("お気に入りの色", *favorite) 

#-----------------------------------------
#可変長一引数は、関数に渡されるときにタプルとなること

def my_generator():
    for i in range(10):
        yield i

def my_func(*args):
    print(args)

it = my_generator()
my_func(*it) 

#可変長引数を受け取る際は、その数が少ないとわかっている場合にしよう
#また、将来的に新しい一引数を追加すると、その関数の呼び出し元をすべて修正する必要がある
#中途半端に修正すると元の関数の動作がおかしくなる

def log_seq(sequence, message, *values):
    if not values:
        print(f"{sequence} - {message}")
    else:
        values_str = ",".join(str(x) for x in values)
        print(f"{sequence} - {message}: {values_str}")

log_seq(1, "お気に入り", 7, 33)
log_seq(1, "こんちゃ")

#ここで位置引数を追加 sequenceの位置がずれたので調整が必要になるということ
log_seq("お気に入りの数値", 7, 33)   

#*argsとすれば関数が可変数一引数となる
#ジェネレータに対して*を使うと一機にタプルに格納されるためメモリクラッシュの危険性
#*argsを受け取る関数に新しく位置引数を入れると挙動が狂う（👆で確認済み）