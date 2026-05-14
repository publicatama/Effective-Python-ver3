#-----------------------------------------
#tracebackによる高度な例外報告

#

#def inner_func(message):
#    assert False, message

#def other_func(message):
#    inner_func(message)
    
#other_func("Oops!")

#Traceback (most recent call last):
  #File "c:\Users\disor\Desktop\effectivePython\87.py", line 12, in <module>
    #other_func("Oops!")
    #~~~~~~~~~~^^^^^^^^^
  #File "c:\Users\disor\Desktop\effectivePython\87.py", line 10, in other_func
    #inner_func(message)
    #~~~~~~~~~~^^^^^^^^^
  #File "c:\Users\disor\Desktop\effectivePython\87.py", line 7, in inner_func
    #assert False, message
    #       ^^^^^
#AssertionError: Oops!

#このように順番に伝播していくが、１つでエラーがおきると、並行して同じレベルで動いているほかの処理まで巻き込んで止まってしまうリスクがある。
#対処法として、リクエストハンドラをtry文で囲む方法がある

class Request:
    def __init__(self, body):
        self.body = body
        self.response = None

def do_work(data):
    assert False, data
    #...

def handle(request):
    try:
        do_work(request.body)
    except BaseException as e:
        print(repr(e))
        request.response = 400 #不正なリクエストエラー
    
request = Request("My message")
handle(request)
#AssertionError('My message')

#👆だけではデバッグに必要な情報が不足しているため、tracebackを使って情報を補完させられる

import traceback

def handle2(request):
    try:
        do_work(request.body)
    except BaseException as e:
        traceback.print_tb(e.__traceback__) #変更した
        print(repr(e))
        request.response = 400 #不正なリクエストエラー
        
request = Request("My message2")
handle2(request)

#File "c:\Users\disor\Desktop\effectivePython\87.py", line 55, in handle2
    #do_work(request.body)
    #~~~~~~~^^^^^^^^^^^^^^
  #File "c:\Users\disor\Desktop\effectivePython\87.py", line 35, in do_work
   # assert False, data
           #^^^^^
#AssertionError('My message2')
#ちゃんと👆のように、トレースバックが持つファイル名、行番号、ソースコード業、関数名などもすべて捕捉できる

def handle3(request):
    try:
        do_work(request.body)
    except BaseException as e:
        stack = traceback.extract_tb(e.__traceback__) #変更した
        for frame in stack:
            print(frame.name)
        print(repr(e))
        request.response = 400
        
request = Request("My message3")
handle3(request)

#handle3
#do_work
#AssertionError('My message3')

#tracebackを使うことで、より詳細なエラーハンドリングも可能である
#発生した例外のログをJSON形式を格納することを考える。

import json

def log_if_error(file_path, target, *args, **kwargs):
    try:
        target(*args, **kwargs)
    except BaseException as e:
        stack = traceback.extract_tb(e.__traceback__)
        stack_without_wrapper = stack[1:]
        trace_dict = dict(
            stack=[item.name for item in stack_without_wrapper],
            error_type = type(e).__name__,
            error_message=str(e),
        )
        json_data = json.dumps(trace_dict)
        with open(file_path, "a") as f:
            f.write(json_data)
            f.write("\n")
            
log_if_error("my_log.json1", do_work, "First_error")
log_if_error("my_log.json1", do_work, "Second_error")
with open("my_log.json1") as f:
    for line in f:
        print(line, end="")
        
#{"stack": ["do_work"], "error_type": "AssertionError", "error_message": "First_error"}
#{"stack": ["do_work"], "error_type": "AssertionError", "error_message": "Second_error"}