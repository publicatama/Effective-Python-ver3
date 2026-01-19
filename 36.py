#-----------------------------------------
#Noneとdocstring

from datetime import datetime
from time import sleep

def log(message, when=datetime.now()):
    print(f"{when}: {message}")
    
#log("こんにちは！！")
#sleep(5)
#log("ふたたびこんにちは！！！")


'''
ログを見ると以下のようになり、時間の表示が実態とあっていない
2025-12-31 03:54:07.400290: こんにちは！！
2025-12-31 03:54:07.400290: ふたたびこんにちは！！！
'''

#-----------------------------------------
#期待通りの成果を得るには、キーワード引数のデフォルト値をNoneにし、実際の挙動をdocstringでドキュメント化する。
#実引数がNoneであることをチェックして適切なデフォルト値を代入する

def log(message, when=None):

    '''
    Args:
        message: 印字するメッセージ。
        when: メッセージが発生した日時。
            デフォルトは現在の時刻
    '''

    if when is None:
        when = datetime.now()
    print(f"{when}: {message}")

log("こんにちは！！")
#sleep(5)
log("ふたたびこんにちは！！！")

#-----------------------------------------
#引数がミュータブルであるときの注意

import json
def decode(data, default={}):
    try:
        return json.loads(data)
    except ValueError:
        return default

foo = decode("bad data")
foo["stuff"] = 5
bar = decode("also bad")
bar["meep"] = 1
print("Foo:", foo)
print("Bar:", bar)

assert foo is bar
#fooとbarは異なる辞書かと思いきや、実は同じ辞書オブジェクトとなっている

#-----------------------------------------
def decode(data, default=None):
    '''JSONデータを文字列からロードする。
    Args:
        data: でコードするJSONデータ
        default: デコードが失敗した場合に返す値。デフォルトは空の辞書。
    '''
    try:
        return json.loads(data)
    except ValueError:
        if default is None: #ここでチェックする
            default = {}
        return default

foo = decode("bad data")
foo["stuff"] = 5
bar = decode("also bad")
bar["meep"] = 1
print("Foo:", foo)
print("Bar:", bar)

assert foo is not bar

#-----------------------------------------

def log_typed(message: str, when: datetime | None = None) -> None:
    '''タイムスタンプ付きでメッセージをログに記録する
    Args:
        message:印字するメッセージ。
        when:メッセージが発生した日時。デフォルトは現在の時刻   
    '''
    if when is None:
        when = datetime.now()
    print(f"{when}: {message}")


log_typed("あいうえおかきくけこ！")
log_typed("日付指定？", "2025-12-30 22:06:54.814751") #指定するとそのままかける

#キーワード引数を動的に初期化する場合は、Noneをデフォルト値として渡す。関数のdocstringで意図された動きを書く
#デフォルト引数Noneは型アノテーションとも調和して機能するので便利！
