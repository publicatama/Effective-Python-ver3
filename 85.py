#-----------------------------------------
#Exceptionクラスの捕捉

#簡単なパイプライン

def load_data(path):
    #...
    pass
def analyze_data(data):
    #...
    pass
def run_report(path):  #👈5分ごとに実施と想定
   data = load_data(path)
   summary = analyze(data)
   return summary

summary = run_report("pizza_data-2024-01-28.csv")
print(summary)

#ファイルが存在しないようなエラーが発生することがある。その場合は、try/exceptでrun_reportから発生する例外を捕捉して、メッセージでエラーを出力することで対処する

try:
    summary = run_report("pizza_data.csv")
except FileNotFoundError:
    print("Transient file error") #Transient file Errorと出す
else:
    print(summary)

#👆により、FileNotFoundErrorは対処できるが、関数パイプラインで予期せぬ例外外発生することも考えられる。
#取引処理がクラッシュすることの方が問題のため、以下の方法がある
#FileNotFoundErrorだけでなく、より広範なExceptionを捕捉する方法がある

try:
    summary = run_report("pizza_data.csv")
except Exception: #👈FileNotFoundErrorから広げる
    print("Transient file error") #Transient file Errorと出す
else:
    print(summary)

#こう書くことでエラーのほとんどは捕捉できるが、本当の問題がわからなくなってしまう恐れがある。データがあるはずなのに、ひたすらエラーを吐き続けるような状況。

#本当は、analyze_data()と書くべきところをanalyze(data)と書いていたところがまずかったという問題がわからなくなってしまう

run_report("my_data.csv")
#analyze is not definedと出る

#例えば以下のように書くことで、どのようなエラーだったかを明確にする

try:
    summary = run_report("my_data.csv")
except Exception as e:#👈FileNotFoundErrorから広げる
    print("Fail:", type(e), e) #Transient file Errorと出す
else:
    print(summary)
    
#👆のように書けば、Fail: <class 'NameError'> name 'analyze' is not definedと表示され本当のエラーがわかる



#AIからのさらなる提案👇💡

try:
    summary = run_report("data.csv")
except FileNotFoundError:
    print("ファイル待ち中...") # これは想定内なので静かに処理
except Exception as e:
    print(f"要調査のバグ発生: {type(e)} {e}") # これがあなたの書いた「正体を暴く」コード
       # ここで管理者へメールを飛ばすなどの処理を入れる

### ④ 動的言語ゆえの「不意打ち」に備える
#Pythonは実行時まで型や名前のチェックを完全には行わないため[cite: 1]、今回のような `NameError` はどんなに気をつけていても混入する可能性があります。
#対策として、開発環境では `mypy` や `Pyright` といった静的解析ツールを併用し、実行前に「`analyze` なんて関数は存在しませんよ」という警告を出す仕組みを作っておくのが賢い。

#print("Fail:", type(e), e)` と書く癖をつけるだけで、原因不明の「なぜか動かない」という時間を減らせる。
#これをさらに進化させて、「ログとして残す」「重大なものだけ通知する」といった仕組みに繋げるのがよい。