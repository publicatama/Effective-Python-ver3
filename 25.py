#-----------------------------------------------
#Python3.13 👈ちゃんとデータを入れた順序を保持
baby_names = {
    "cat": "kitten",
    "dog": "puppy"
}
print(baby_names)

print(list(baby_names.keys()))
print(list(baby_names.values()))
print(list(baby_names.items()))
print(list(baby_names.popitem()))

#-----------------------------------------------

def my_func(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")
my_func(goose = "gosling", kangaroo = "joey")

#-----------------------------------------------

class Myclass:
    def __init__(self):
        self.alligator = "hatchling"
        self.elephant = "calf"
a = Myclass()
for key, value in a.__dict__.items():
    print(f"{key} = {value}")

#-----------------------------------------------

votes = {
    "otter" : 1281,
    "polar bear" : 587,
    "fox" :863, 
}

def populate_ranks(votes, ranks):
    names = list(votes.keys())
    names.sort(key=votes.get, reverse = True)
    for i, name in enumerate(names, 1):
        ranks[name] = i

def get_winner(ranks):
    return next(iter(ranks))


ranks = {}
populate_ranks(votes, ranks)
print(ranks)
winner = get_winner(ranks)
print(winner)

#-----------------------------------------------

from collections.abc import MutableMapping

class SortedDict(MutableMapping):
    def __init__(self):
        self.data = {}
    
    def __getitem__(self, key):
        return self.data[key]
    
    def __setitem__(self, key, value):
        self.data[key] = value
    
    def __delitem__(self, key):
        del self.data[key]
        
    def __iter__(self):
        keys = list(self.data.keys())
        keys.sort()
        for key in keys:
            yield key
    
    def __len__(self):
        return len(self.data)
    
sorted_ranks = SortedDict()
populate_ranks(votes, sorted_ranks)
print(sorted_ranks.data)
winner = get_winner(sorted_ranks)
print(winner)
#順序が正しくない！

#-----------------------------------------------

def get_winner(ranks):
    for name, rank in ranks.items():
        if rank == 1:
            return name
winner = get_winner(sorted_ranks)
print(winner) 

#-----------------------------------------------

'''
def get_winner(ranks):
    if not isinstance(ranks, dict):
        raise TypeError("must provide a dict instance")
    return next(iter(ranks))

get_winner(sorted_ranks)
'''

#-----------------------------------------------

from typing import Dict, MutableMapping

def populate_ranks(votes: Dict[str, int], rank: Dict[str, int]) -> None:
    names = list(votes.keys())
    names.sort(keys=votes.__getitem__, reverse=True)
    for i, name in enumerate(name, i):
        ranks[name] = i

def get_winner(ranks: Dict[str, int]) -> str:
    return next(iter(ranks))

class SortedDict(MutableMapping[str, int]):
    #👇は適当
    def __init__(self):
        self.data = "ss"
    
votes = {
    "otter" : 1281,
    "polar bear" : 587,
    "fox" :863, 
}

sorted_ranks = SortedDict()
populate_ranks(votes, sorted_ranks)
print(sorted_ranks.data)
winner = get_winner(sorted_ranks)
print(winner)

#-----------------------------------------------
#dict型を扱う際の注意として、挿入順序に依存しないコードを核　実行時にdict型のインスタンスかどうかチェック　型アノテーションと静的解析を使う

