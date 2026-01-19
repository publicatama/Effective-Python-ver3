#-----------------------------------------

def sort_priority(values, group):
    def helper(x):
        if x in group:
            return (0, x)
        return (1, x)
    
    values.sort(key=helper)

numbers = [8, 3, 1, 2, 5, 4,7, 6]
group = {2, 3, 5, 7}
sort_priority(numbers, group)
print(numbers)

#-----------------------------------------

def sort_priority2(numbers, group):
    found = False
    
    def helper(x):
        if x in group:
            found = True
            return (0, x)
        return (1, x)
    
    numbers.sort(key=helper)
    return found 

found = sort_priority2(numbers, group)
print("見つかった:", found)
print(numbers)

#-----------------------------------------

def sort_priority2(numbers, group):
    found = False #スコープ:"sort_priority2"
    
    def helper(x):
        if x in group:
            found = True #スコープ:"helper"
            return (0, x)
        return (1, x)
    
    numbers.sort(key=helper)
    return found 
#👆これはスコープバグと呼ばれることも

#-----------------------------------------

def sort_priority3(numbers, group):
    found = False #スコープ:"sort_priority2"
    
    def helper(x):
        nonlocal found #追加
        if x in group:
            found = True
            return (0, x)
        return (1, x)
    
    numbers.sort(key=helper)
    return found

found = sort_priority3(numbers, group)
print("見つかった:", found)
print(numbers)

#nonlocalを使ってもスコープがわかりづらくなる

#-----------------------------------------
#コードは長いが多少わかりやすくなる
class Sorter:
    
    def __init__(self,group):
        self.group = group
        self.found = False
    
    def __call__(self, x):
        if x in self.group:
            self.found = True
            return(0, x)
        return(1, x)
    
sorter = Sorter(group)
numbers.sort(key=sorter)
print("見つかった！:", sorter.found)
print(numbers)
#シンプルな関数以外ではnonlocalは避ける。わかりづらいし。

