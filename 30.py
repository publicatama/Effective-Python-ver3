#-----------------------------------------
#5章：関数
#関数の引数はミュータブル

def my_func(items):
    items.append(4)
    
x = [1,2,3]
my_func(x)
print(x)

#bにaをこの形で渡すと、aの値も変更されてしまう 参照渡し
a = [7,6,5]
b = a
my_func(b)
print(a)

#-----------------------------------------
def capitalize_items(items):
    for i in range(len(items)):
        items[i] = items[i].capitalize()
    
my_items = ["hello", "world"]
items_copy = my_items[:] #👈ここでコピー
capitalize_items(items_copy)
print(items_copy)
print(my_items) #👈コピーと別で保管できている

#辞書にはコピー専用のメソッドあり
def concat_pairs(items):
    for key in items:
        items[key] = f"{key}={items[key]}"

my_pairs = {"foo": 1, "bar": 2}
pairs_copy = my_pairs.copy() #コピー作成めそっど
concat_pairs(pairs_copy)
print(pairs_copy)
print(my_pairs)

#-----------------------------------------
#ユーザ定義クラスも呼び出し側でミュータブル

class Myclass:
    def __init__(self, value):
        self.value = value

x = Myclass(10)

def my_func(obj):
    obj.value = 20
    
my_func(x)
print(x.value)

#Pythonでは引数は参照渡しとなる
#関数で入力引数を変更する場合は、名前付けやドキュメントで変更を明確にし、むやみに変更しない
#受け取ったコレクションはコピーしておけば、関数による意図しない挙動を回避できる。重要！
