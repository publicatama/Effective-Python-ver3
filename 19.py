#-----------------------------------------------
for i in range(3):
    print("ループ", i)
else:
    print("Elseブロック！")
#-----------------------------------------------
for i in range(3):
    print("ループ", i)
    if i == 1:
        break
else:
    print("Elseブロック！")

#-----------------------------------------------
for x in []:
    print("実行されない")
else:
    print("For elseブロック！")

#-----------------------------------------------
while False:
    print("実行されない")
else:
    print("While elseブロック！")

#-----------------------------------------------
a = 4
b = 9

#動くが筆者は書かない
for i in range(2,min(a,b) + 1):
    print("テスト中", i)
    if a % i == 0 and b % i == 0:
        print("互いに素ではない")
        break
else:
    print("互いに素")
    
#-----------------------------------------------
#方法１
def coprime(a,b):
    for i in range(2,min(a,b) + 1):
        if a % i == 0 and b % i == 0:
            return False
    return True

assert coprime(4,9)
assert not coprime(3,6)
#-----------------------------------------------
#方法2
def coprime_alternate(a,b):
    is_coprime = True
    for i in range(2,min(a,b) + 1):
        if a % i == 0 and b % i == 0:
            is_coprime = False
    return is_coprime

assert coprime(4,9)
assert not coprime(3,6)

#-----------------------------------------------