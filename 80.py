#-----------------------------------------
#try とfinally

def try_finally_example(filename):
    print("* opening file")
    handle = open(filename, encoding="utf-8")
    try:
        print("* reading data")
        return handle.read()
    finally:
        print("* Calling close()")
        handle.close()
    
filename = "randam_data.txt"
with open(filename, "wb") as f:
    f.write(b"\xf1\xf2\xf3\xf4\xf5")

data = try_finally_example(filename)

try_finally_example("does_not_exist")

#-----------------------------------------
#try except else

import json

def load_json_key(data,key):
    try:
        print("* Loading JSON data")
        result_dict = json.loads(data) #valueerrorがおきるかも
    except ValueError:
        print("* Handling ValueError")
        raise KeyError(key)
    else:
        print("* Looking up key")
        return result_dict[key] #KeyErrorがおきるかも

assert load_json_key('{"foo": "bar"}', "foo")

load_json_key('{"foo": bad payload', "foo")  #有効でないJSON

load_json_key('{"foo": "bar"}', "does not exist")

#-----------------------------------------
#try/except/else/finally
#処理に成功した場合try else finallyブロックが順番に実施される

UNDEFINED = object()

def divide_json(path):
    print("* opening file")
    handle = open(path, "r+") #OSErrorがおきるかも
    try:
        print("* reading data")
        return handle.read() #UnicodeDecodeErrorが起きるかも
        print("* Loading JSON data")
        op = json.loads(data) #ValueErrorが起きるかも
        print("* Performing Calculation")
        value = op["numerator"] /op["denominator"] #ZeroDivisionErrorが起きるかも
    except ZeroDivisionError:
        return UNDEFINED  
    else:
        print("* Writing calculation")
        op["result"] = value
        result = json.dumps(op)
        handle.seek(0) #OSErrorがおきるかも
        handle.write(result) #OSErrorがおきるかも
        return value
    finally:
        print("* Calling close()")
        handle.close() #常に実行


temp_path = "random_data.json"
with open(temp_path, "w") as f:
    f.write('{"nuerator": 1, "denominator": 10}') 

assert divide_json(temp_path) == 0.1

#演算に失敗した場合は、try, except, finallyが順に実行され、elseは実行されない

with open(temp_path, "w") as f:
    f.write('{"nuerator": 1, "denominator": 0}') 
    
assert divide_json(temp_path) is UNDEFINED

#JSONが無効だった場合、try上で例外が発生し、finallyが実行されたあとに、例外が呼び出し元に伝播する。exceptとelseは実行されない

with open(temp_path, "w") as f:
    f.write('{"nuerator": 1, bad data')

divide_json(temp_path)

#このような書き方は各ブロックを直感的に構成するので、非常に扱いやすい
#divide_json中にディスク容量が枯渇したとする

with open(temp_path, "w") as f:
    f.write('{"nuerator": 1, "denominator": 10}') 
    
divide_json(temp_path)

#このときでもOSErrorの例外に行き、Finallyが実行されてファイルが閉じられるのでＯＫ


