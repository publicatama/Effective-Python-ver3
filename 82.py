#-----------------------------------------
#contextlibとwith文で再利用可能なtry/finallyを実現

from threading import Lock

lock = Lock()
with lock:
        #ロックしつつ何かする
    pass

lock.acquire()
try:
    #ロックしつつ何かする
    pass
finally:
    lock.release()

#with文の方が、try/finallyよい少量のコードで済む。acquireのあとreleaseをすることを忘れずに済む。

#contextlibを使えば、オブジェクトや関数をwithで簡単に使える

import logging

def my_function():
    logging.debug("Some debug data")
    logging.error("Error log here")
    logging.debug("More debug data")

my_function()

#contextlibを使ってコンテキストマネージャを定義し、ログレベルをlevelに変更し、その後戻す操作ができる

from contextlib import contextmanager

@contextmanager
def debug_logging(level):
    logger = logging.getLogger()
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield
    finally:
        logger.setLevel(old_level)

with debug_logging(logging.DEBUG):
    print("* Inside:")
    my_function()
print("* After:")
my_function

#Asターゲットを有効にする
#コンテキストマネージャは何らかのオブジェクトを返すことがあり、これはwith文のas節で指定したローカル変数に代入されて、withブロック内のコードで利用できる

with open("my_output.txt", "w") as handle:
    handle.write("This is some data!")

#👇のようにもかけるが、上の方がパイソニックである
handle = open("my_output.txt", "w")
try:
    handle.write("This is some data!")
finally:
    handle.close()

#withとas節で書くことで、処理を終えたあとに確実にファイルが閉じられるようになるのでよい。
#close()のボイラープレートも不要となるのがよい

#コンテキストマネージャからasに値を持たせるようにするには、値をyieldしてやればいい
@contextmanager
def debug_logging(level, name):
    logger = logging.getLogger(name)
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield logger
    finally:
        logger.setLevel(old_level)
        
with log_level(logging.DEBUG, "my-log") as my_logger:
    my_logger.debug(f"This is a message for {my_logger.name}!")
    logging.debug("This will not print")

#with文が終わったあとは、ログレベルがデフォルトに戻されているのでlogger.debug()のログメッセージは表示されない

logger = logging.getLogger("my-log")
logger.debug("Debug will not print")
logger.error("Error will print") #Error will print

#ロガーの名前を変更したい場合は、with文のコンテキストマネージャの引数を変更するだけ

#with log_level(logging.DEBUG, "other-log") as my_logger:

