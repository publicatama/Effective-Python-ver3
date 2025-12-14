#-----------------------------------------------
from random import randint

random_bits = 0
for i in range(32):
    if randint(0,1):
        random_bits |=1 << i

print(bin(random_bits))
      
#-----------------------------------------------
flavor_list = ["vanila","chocolate", "pecan", "strawberry"]
for flavor in flavor_list:
    print(f"{flavor} is delicious")

#みづらい
for i in range(len(flavor_list)):
    flavor = flavor_list[i]
    print(f"{i + 1}: {flavor}")

#みやすいenumerate
it = enumerate(flavor_list)
print(next(it))
print(next(it))

for i, flavor in enumerate(flavor_list):
    print(f"{i + 1}: {flavor}")
    
#もっと短く
for i, flavor in enumerate(flavor_list, 1):
    print(f"{i}: {flavor}")  

#-----------------------------------------------