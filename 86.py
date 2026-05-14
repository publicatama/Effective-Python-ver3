#-----------------------------------------
#ExceptionクラスとBaseExceptionの違い

#Python公式ドキュメントによれば、プログラマは例外をExceptionクラスから継承して作るべき、とある。
#しかし、例外クラスの階層は、Exceptionの基底クラスであるBaseExceptionがあり、Pythonが内部で持っている例外クラスにはBaseExceptionから継承して作られているものもある。
#例えば、KeyboardInterruptはBaseExceptionから継承されているため、Exceptionで捕捉しようとしてもすべての例外ハンドラをバイパスして、プログラムのエントリポイントまで例外が伝播する。
import sys

def do_processing():
    #...
    pass

def main(argv):
    while True:
        try:
            do_processing() #割り込み
        except Exception as e:
            print("Error:", type(e),e)
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))


#例えば以下のように

def do_processing(handle):
    #...
    pass

def main(argv):
    data_path = argv[1]
    handle = open(data_path, "w")
    while True:
        try:
            do_processing(handle)
        except Exception as e:
            print("Error:", type(e), e)
        except BaseException:
            print("Cleaning up interrupt")
            handle.flush()
            handle.close()
            return 1
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))

#問題は、BaseExceptionがほかの重要な処理も直接継承しているため、これらはユーザーがこのエラーを捕捉しないことを前提に作られているので、プログラムに意図しない悪影響をおよぼす可能性がある。
#そのため、上のようなクリーンアップの処理をしたい場合は、try/finallyを使って実装する。するとExceptionを継承しているか、BaseExceptionを継承しているかに関係なくクリーンアップ処理が確実に実行ｓれる

def main(argv):
    data_path = argv[1]
    handle = open(data_path, "w+")
    try:
        while True:
            try:
                do_processing(handle)
            except Exception as e:
                print("Error:", type(e), e)
    finally:
        print("Cleaning up finally") #いつも動作する
        handle.flush()
        handle.close()   

if __name__ == "__main__":
    sys.exit(main(sys.argv))

#どうしてもBaseExceptionを直接継承した例外を捕捉して処理する場合は、コールスタックの上位までエラーを正しく伝播させることが重要。
#

def main(argv):
    while True:
        try:
            do_processing()
        except Exception as e:
            print("Error:", type(e), e)
        except KeyboardInterrupt:
            found = input("Terminate? [y/n]: ")
            if found == "y":
                raise #エラーを伝播させる
            
if __name__ == "__main__":
    sys.exit(main(sys.argv))
    

#例外処理を強化したロギング実装の場合もBaseExceptionを捕捉する方法が有効

import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            result = e
            raise
        finally:
            print(
                f"Called {func.__name__}"
                f"(*{args!r}, **{kwargs!r})"
                f"got {result!r}"
            )
    return wrapper

@log
def my_func(x):
    x / 0
my_func(123)

#しかし捕捉した例外がBaseExceptionを直接継承している場合、デコレータは予期せぬエラーを引きおこす。

@log
def other_func(x):
    if x > 0:
        sys.exit(1)
other_func(456)

#sys.exitはBaseExceptionから継承されるため、except Excepttionでは捕捉できず、result=eが代入されないままFinallyに進む。そこで定義されていないresultを参照しようとするので、エラーとなる。

#👆のような問題を避けるため、Excepttionの代わりにBaseExcepttionを捕捉するようにするとうまく動く👇

def fixed_log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except BaseException as e: #なおした
            result = e
            raise
        finally:
            print(
                f"Called {func.__name__}"
                f"(*{args!r}, **{kwargs!r})"
                f"got {result!r}"
            )
    return wrapper

@fixed_log

def other_func(x):
    if x > 0:
        sys.exit(1)
other_func(456)

#ちゃんとSystemExit: 1が返る




#この分離はプログラムを安全に終了させるために必要。
#① プログラムの「停止命令」を邪魔しない
#KeyboardInterrupt が Exception に含まれていたら、先ほどの「広範なエラーキャッチ（except Exception）」を書いただけで、ユーザーが Ctrl+C を押してプログラムを止めようとしても、プログラムがそれを「エラー」として飲み込んでしまい、止まらなくなってしまいます。  

#ロバストネスの視点: 「システムを安全に止める」という命令を、通常の計算エラーと混同させないことで、プログラムの制御性を担保しています。  

#② 独自に作成する例外は必ず Exception を継承する
#自作の例外を作る際は、必ず Exception を継承してください。なぜなら、もし BaseException を直接継承してしまうと、他の開発者が except Exception: で「一般的なエラーをすべてログに記録しよう」とした際に、自作の例外だけがログに記録されず、そのままプログラムがクラッシュしてしまうからです。  

#③ どうしてもすべてを捕まえたい場合（極めて稀）
#万が一あらゆる事態（Ctrl+C さえも）をキャッチして何か処理をしたい場合は、except BaseException: と書くことになりますが、これは推奨されません。
#通常は finally ブロックを使って、クリーンアップ処理を行うのが正解です。