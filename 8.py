#----------------------------------------------- 
"""
fresh_fruit = {
    "apple" : 10,
    "banana" :8,
    "lemon" :5,
}

def make_lemonade(count):

def out_of_stock():
    
count = fresh_fruit.get("lemon", 0)
if count:
    make_lemonade(count)
else:
    out_of_stock()

"""

#----------------------------------------------- 
if count := fresh_fruit.get("lemon",0):
    make_lemonade(count)
else:
    out_of_stock()


def make_cider(count):

count := fresh_fruit.get("apple",0)
if count >=4:
    make_cider(count)
else:
    out_of_stock()
    
#----------------------------------------------- 
if (count := fresh_fruit.get("apple",0)) >=4:
    make_cider(count)
else:
    out_of_stock()

#----------------------------------------------- 
def slice_bananas(count):
    
class OutOfBananas(Exception):
    pass

def make_smoothies(count):
    
pieces = 0
count = fresh_fruit.get("banana", 0)
if count >= 2:
    pieces = slice_bananas(count)
try:
    smoothies = make_smoothies(pieces)
except OutOfBananas:
    out_of_stock()
    

#-----------------------------------------------     
count = fresh_fruit.get("banana", 0)
if count >= 2:
    pieces = slice_bananas(count)
else:
    pieces = 0 #移動
try:
    smoothies = make_smoothies(pieces)
except OutOfBananas:
    out_of_stock()

#----------------------------------------------- 

pieces = 0
if (count := fresh_fruit.get("banana", 0)) >= 2:
    pieces = slice_bananas(count)
try:
    smoothies = make_smoothies(pieces)
except OutOfBananas:
    out_of_stock()    
    
#----------------------------------------------- 

if (count := fresh_fruit.get("banana", 0)) >= 2:
    pieces = slice_bananas(count)
else:
    pieces = 0
try:
    smoothies = make_smoothies(pieces)
except OutOfBananas:
    out_of_stock()   

    
#----------------------------------------------- 
count = fresh_fruit.get("banana", 0)
if count >= 2:
    pieces = slice_bananas(count)
    to_enjoy = make_smoothies(pieces)
else:
    count = fresh_fruit.get("apple", 0)
    if count >= 4:
        to_enjoy = make_cider(count)
    else:
        count = fresh_fruit.get("lemon", 0)
        if count:
            to_enjoy = make_lemonade(count)
        else:
            to_enjoy = "Nothing"
#----------------------------------------------- 
#読みやすい！
if (count := fresh_fruit.get("banana", 0)) >= 2:
    pieces = slice_bananas(count)
    to_enjoy = make_smoothies(pieces)
elif (count := fresh_fruit.get("apple", 0)) >= 4:
    to_enjoy = make_cider(count)
elif (count := fresh_fruit.get("lemon", 0)) :
    to_enjoy = make_lemonade(count)
else:
    to_enjoy = "Nothing"
#----------------------------------------------- 

def pick_fruit():
def make_juice(fruit, count):

bottles =[]
fresh_fruit = pick_fruit()
while fresh_fruit:
    for fruit, count in fresh_fruit.items():
        batch = make_juice(fruit, count)
        bottles.extend(batch)
    fresh_fruit = pick_fruit()
    
#----------------------------------------------- 
bottles =[]
while True:
    fresh_fruit = pick_fruit()
    if not fresh_fruit:
        break
    for fruit, count in fresh_fruit.items():
        batch = make_juice(fruit, count)
        bottles.extend(batch)
#----------------------------------------------- 
bottles =[]
while fresh_fruit := pick_fruit():
    for fruit, count in fresh_fruit.items():
        batch = make_juice(fruit, count)
        bottles.extend(batch)
#----------------------------------------------- 