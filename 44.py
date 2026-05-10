#-----------------------------------------
#おおきな内包表記にはジェネレータ式を利用する
'''
value = [len(x) for x in open("my_file.txt")]
print(value)
#[100, 57, 15, 1, 12, 75, 5, 86, 89, 11]
'''

myfile = [100, 57, 15, 1, 12, 75, 5, 86, 89, 11]

it = (x for x in myfile)
print(it) #ジェネレータオブジェクトを生成する

print(next(it))
print(next(it))

roots = ((x, x**0.5) for x in it)
print(next(roots))

#大きな入力ストリームンある場合はジェネレータ式を使うと最適に処理できる！