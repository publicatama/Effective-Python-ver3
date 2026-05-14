#-----------------------------------------
#tracebackによる高度な例外報告

#辞書に存在しないキーを参照しようとするとKeyErrorが発生する

my_dict = {}
#my_dict["does_not_exist"]

#Traceback (most recent call last):
#  File "c:\Users\disor\Desktop\effectivePython\88.py", line 7, in <module>
#    my_dict["does_not_exist"]
#KeyError: 'does_not_exist'

#辞書のキーを参照する部分をtryで書けば、KeyErrorを捕捉して処理できる

my_dict = {}
try:
    my_dict["does_not_exist"]
except KeyError:
    print("Could not find key!")

#例外処理中に新たな例外が発生すると表示されるスタックトレースが大きく変化する。KeyErrorを処理している間に新たに定義したMissingErrorを意図的に発生させるとスタックトレースは以下のように

class MissingError(Exception):
    #...
    pass

#try:
#    my_dict["does_not_exist"] #最初のエラーが起きる
#except KeyError:
#    raise MissingError("Oops!") #２つ目のエラーが起きる

#そこで、MissingErrorも捕捉して、__context__属性を表示することでどのように連鎖しているか見る

try:
    try:
        my_dict["does_not_exist"]
    except KeyError:
        raise MissingError("Oops!")
except MissingError as e:
    print("Second", repr(e)) #2こめ
    print("First", repr(e.__context__)) #1こめ

#エラーハンドリングが多層にわたる場合には、例外の連鎖を制御してエラーメッセージを明確にする。raise文のfrom句を使えば例外を連鎖できる。以下のように。

def lookup(my_key):
    try:
        return my_dict[my_key]
    except KeyError:
        raise MissingError

my_dict["my key 1"] =123
print(lookup("my key 1")) #123と表示される
print(lookup("my key 2"))  #以下のようにちゃんとMissing Errorが表示される

#  File "c:\Users\disor\Desktop\effectivePython\88.py", line 48, in lookup
#    return my_dict[my_key]
#           ~~~~~~~^^^^^^^^
#KeyError: 'my key 2'

#During handling of the above exception, another exception occurred:

#Traceback (most recent call last):
#  File "c:\Users\disor\Desktop\effectivePython\88.py", line 54, in <module>
#    print(lookup("my key 2")) #
#          ~~~~~~^^^^^^^^^^^^
#  File "c:\Users\disor\Desktop\effectivePython\88.py", line 50, in lookup
#    raise MissingError
#MissingError


