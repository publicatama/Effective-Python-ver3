#-----------------------------------------
#assertとRaise

#Assert式でFalseと評価されたときはAssertionErrorを返す

list_a = [1, 2, 3]
assert list_a, "a empty"

#list_b = []
#assert list_b, "b empty" #例外発生

#raiseとifを使ってカラリストを検出

class EmptyError(Exception):
    pass

list_c = []
#if not list_c:
#    raise EmptyError("c empty")

#raiseからの例外はtry\exceptで捕捉できる

try:
    raise EmptyError("From raise statement")
except EmptyError as e:
    print(f"Caught: {e}")
    
#assertの例外もtyr/exceptで捕捉できる

try:
    assert False, "From assert statement"
except AssertionError as e:
    print(f"Caught: {e}")
    
#raise文ので発生するエラーは、関数のインターフェースの一部とみなされ、発生する例外は呼び出し側で捕捉されて適切に処理されることを期待する
#assert文で発生する例外は、呼び出し元で捕捉されることを想定していない。開発者がロギングする際などに役立つ

class RatingError(Exception):
    #・・・
    pass

class Rating:
    def __init__(self, max_rating):
        if not (max_rating > 0):
            raise RatingError("Invalid max_rating")
        self.max_rating = max_rating
        self.ratings = []
    
    def rate(self, rating):
        if not (0 < rating <= self.max_rating):
            raise RatingError("Invalid rating")
        self.ratings.append(rating)
    
movie = Rating(5)
movie.rate(5)
movie.rate(7) #例外発生　ここでちゃんとInvalid　Ratingが取得できる


class RatingInternal:
    def __init__(self, max_rating):
        assert max_rating > 0, f"Invalid {max_rating=}"
        self.max_rating = max_rating
        self.ratings = []
    
    def rate(self, rating):
        assert 0 < rating <= self.max_rating, f"Invalid {max_rating=}"
        raise RatingError("Invalid rating")
        self.ratings.append(rating)

movie = RatingInternal(5)
movie.rate(5)
movie.rate(7) #Raises


#やってはいけない握りつぶし
# ❌ やってはいけない「握りつぶし」の例
try:
    movie = RatingInternal(5)
    movie.rate(7) 
except AssertionError:
    # エラーが出たけど、とりあえず無視して次に進もう
    pass

#なぜ握りつぶしてはいけないのか？
#バグの隠蔽: assert が失敗したということは、「プログラムが想定外の状態にある」ということです。これを無視して続行すると、データが壊れたり、後続の処理で原因不明のクラッシュを引き起こしたりします。  
#デバッグ不能: 本来ならログにエラー箇所が残るはずが、握りつぶすと「なぜか動いているが、結果がおかしい」という最も厄介な状態になります。
#セキュリティリスク: ITエンジニアの視点では、セキュリティチェックなどを assert で行い、それを握りつぶしてしまうと、本来通すべきでない処理が実行されるリスクに直結します。
#「握りつぶさない」＝「異常事態が起きたら、あえてそのままクラッシュ（あるいは上位でログ出力）させ、開発者が修正すべきサインとして扱う」 という意味です。

#ポイント
#① ユーザー入力には raise、内部ロジックには assert
#ユーザーが入力した値や、外部APIから届いたデータなど「制御できないもの」のチェックには raise を使い、具体的なエラーメッセージを返しましょう。  
#「この関数を呼ぶ時点で、この変数は絶対に正数であるはずだ」といった自分たちの書いたコード間の約束事には assert を使います。

#② -O オプションの罠を知っておく
#Pythonには実行時に python -O script.py と最適化フラグを立てると、すべての assert 文が削除されて実行されるという仕様があります。  
#重要: したがって、ビジネスロジックやセキュリティに関わる重要なチェック（例：支払金額がマイナスでないか）を assert で書いてはいけません。それらが無効化されると、システムが崩壊するからです。  

#③ AssertionError はキャッチしない
#コード内で except AssertionError: と書く必要性はほぼありません。もしキャッチして処理を続けたいなら、それは assert ではなく raise（独自の例外）を使うべき場面です。

#ざっくりと
#assert は「バグがあるなら今すぐここで止まれ！」という、開発者から自分自身への警告灯です。一方、raise は「使い方が間違っていますよ」という、利用者への親切な案内と考えるのがよい