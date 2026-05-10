#-----------------------------------------
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = []
for x in a:
    squares.append(x**2)
print(squares)

#リスト内方表記

squares2 = [x**2 for x in a]
print(squares2)

alt = map(lambda x: x**2, a)
print(list(alt))
print(alt)

even_squares = [x**2 for x in a if x % 2 == 0]
print(even_squares)

alt = map(lambda x: x**2, filter(lambda x: x % 2 == 0, a))
assert even_squares == list(alt)

#-----------------------------------------
#辞書内方表記　集合内方表記

even_squares_dict = {x: x**2 for x in a if x % 2 == 0}
threes_cubed_set = {x**3 for x in a if x % 3 == 0}
print(even_squares_dict)
print(threes_cubed_set)

#filterとmapでも同じことができるが読みにくい

alt_dict = dict(
    map(
        lambda x: (x, x**2),
        filter(lambda x: x % 2 == 0, a),
    )
)

alt_set = set(
    map(
        lambda x: (x, x**3),
        filter(lambda x: x % 3 == 0, a),
    )
)

print(alt_dict)
print(alt_set)

#filter()とmap()はリストではなくイテレータを返すので、メモリ使用量を抑えられる。
#リスト内包表記ではリスト全体を生成するので、メモリ使用量が爆発するかもしれない。
