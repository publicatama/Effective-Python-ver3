#-----------------------------------------
#send()の代わりにイテレータをジェネレータに渡す

#yieldを使えば簡単にジェネレータ関数を定義できるが、ジェネレータ関数は一方向。
#実行中にデータを取得しつつデータを生成する方法はあるのか？

import math

def wave(amplitude, steps):
    step_size = 2 * math.pi /steps
    for step in range(steps):
        radians = step * step_size
        fraction = math.sin(radians)
        output = amplitude * fraction
        yield output
        
def transmit(output):
    if output is None:
        print(f"Output is None") 
    else:
        print(f"Output: {output:>5.1f}")

def run(it):
    for output in it:
        transmit(output)

run(wave(3.0, 8))       