#-----------------------------------------
#例外変数の消失に注意

#例外変酢はexceptの外から参照できない
try:
    raise MyError(123)
except MyError as e:
    print(f"Inside `{e=}")

print(f"Outside {e=}") #例外発生
#e is not definedのエラーが出る

#finallyからも例外変数の参照はできない
try:
    raise MyError(123)
except MyError as e:
    print(f"Inside `{e=}")
finally:
    print(f"FInally `{e=}") #例外発生
#e is not definedのエラーが出る

#tryで発生しうる結果を保存しておくとよい
result = "Unexpected exception"
try:
    raise MyError(123)
except MyError as e:
    result = e
except OtherError as e:
    result = e
else:
    result = "Success"
finally:
    print(f"Log {result=}")
#すると、Log result= MyError(123)と返されるのでわかる
#👆のコードでtryより先にresult変数を定義していることに注意しないと、例外が補足されなかった場合にほかの例外が発生する（Undefined)

try:
    raise OtherError(123)
except MyError as e:
    result = e
else:
    result = "Success"
finally:
    print(f"Log {result=}") #発生する

#result is not definedというエラーが発生する

#-----------------------------------------
