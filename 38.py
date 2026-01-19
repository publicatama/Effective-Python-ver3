#-----------------------------------------
#fuctools.wrapsを使う

def trace(func):
    def wrapper(*args, **kwargs):
        args_repr = repr(args)
        kwargs_repr = repr(kwargs)
        result = func(*args, **kwargs)
        print(f"{func.__name__}({args_repr}, {kwargs_repr}) -> {result!r}")
        return result
    return wrapper

@trace
def fibonacci(n):
    if n in (0, 1):
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)

#fibonacci = trace(fibonacci)

fibonacci(4) #→ここがテキスト通りにならず
print(fibonacci)

#-----------------------------------------
help(fibonacci)

import pickle

#pickle.dumps(fibonacci) #エラーになる

from functools import wraps

def trace(func):
    @wraps(func) #変更済み
    def wrapper(*args, **kwargs):
        args_repr = repr(args)
        kwargs_repr = repr(kwargs)
        result = func(*args, **kwargs)
        print(f"{func.__name__}({args_repr},{kwargs_repr}) -> `{result!r}")
        return result
    return wrapper


@trace
def fibonacci2(n):
    if n in (0, 1):
        return n
    return fibonacci2(n - 2) + fibonacci2(n - 1)

fibonacci2(4)

help(fibonacci2)

print(pickle.dumps(fibonacci2))

#自作デコレータを使うときは、functoolsモジュールのwraps()デコレータを使うとよい。