#-----------------------------------------
#yield fromでジェネレータを組み合わせる

def move(period, speed):
    for _ in range(period):
        yield speed
        
def pause(delay):
    for _ in range(delay):
        yield 0

def animate():
    for delta in move(4, 5.0):
        yield delta
    for delta in pause(3):
        yield delta
    for delta in move(2, 3.0):
        yield delta

def render(delta):
    print(f"delta: {delta:.1f}")

def run(func):
    for delta in func():
        render(delta)

run(animate)

#yield fromを使って親ジェネレータに制御を返す前にネストした子ジェネレータから値をyieldできる。

def animate_composed():
    yield from move(4, 5.0)
    yield from pause(3)
    yield from move(2, 3.0)
    
run(animate_composed)

#yield fromを使えば、ネストされた複数のジェネレータを単一の結合されたジェネレータとして構成できる
#可読性も上がるし、パフォーマンスも向上する

