#-----------------------------------------------
#setdefaultやdefaultdictが適切でない場合

pictures = {}
path = "profile_1234.png"

if (handle := pictures.get(path)) is None:
    try:
        handle = open(path, "a+b")
    except OSError:
        print(f"Failed to open path {path}")
        raise
    else:
        pictures[path] = handle

handle.seek(0)
image_data = handle.read()

#setdefaultを使う場合
try:
    handle = pictures.setdefault(path, open(path, "a+b"))
except OSError:
    print(f"Failed to open path {path}")
    raise
else:
    handle.seek(0)
    image_data = handle.read()

#👆のコードは問題が多い。常にsetdefaultが呼び出されてキーがすでに辞書にあってもopenが毎回呼び出される

#defaultdictを使う場合 エラーになる


from collections import defaultdict

def open_picture(profile_path):
    try:
        return open(profile_path, "a+b")
    except OSError:
        print(f"Failed to open path {path}")
        raise
'''
pictures = defaultdict(open_picture)
handle = pictures[path]
handle.seek(0)
image_data = handle.read()
argument: 'profile_path'
'''
#-----------------------------------------------
#欠落したキーを披露ための処理を追加

class Pictures(dict):
    def __missing__(self, key):
        value = open_picture(key)
        self[key] = value
        return value

pictures = Pictures()
handle = pictures[path]
handle.seek(0)
image_data = handle.read()
#キーに依存するデフォルト値を持つ場合は、派生クラスを定義して__missing__()メソッドを使うのがよい。
