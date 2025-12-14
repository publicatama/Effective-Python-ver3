#-----------------------------------------------
no_snack = ()
snack = ("chips", )
#-----------------------------------------------
snack_calories = {
    "chips": 140,
    "popcorn": 80,
    "nuts": 190,
}
items = list(snack_calories.items())
print(items)
#-----------------------------------------------

item = ("Peanut butter" , "Jelly")
first_item = item[0]
first_half = item[:1]
print(first_item)
print(first_half)
#-----------------------------------------------

pair = ("Chocolate", "Peanuts butter")
#pair[0] = "Honey" #エラー
#-----------------------------------------------

item = ("Peanut butter" , "Jelly")
first, second = item #アンパック
print(first, "and", second)

#-----------------------------------------------

favorite_snacks = {
    "salty": ("pretzels", 100),
    "sweet": ("cookies", 80),
    "veggie": ("carrots", 20),
}
((type1, (name1, calcs1)),
(type2, (name2, calcs2)),
(type3, (name3, calcs3))) = favorite_snacks.items()

print(f"Favorite {type1} is {name1} with {calcs1} calories")
print(f"Favorite {type2} is {name2} with {calcs2} calories")
print(f"Favorite {type3} is {name3} with {calcs3} calories")
#-----------------------------------------------

def bubble_sort1(a):
    for _ in range(len(a)):
        for i in range(1,len(a)):
            if a[i] < a[i-1]:
                temp = a[i]
                a[i] = a[i-1]
                a[i-1] = temp

names = ["pretzels, carrots","arugula","bacon"]
bubble_sort1(names)
print(names)
#-----------------------------------------------

def bubble_sort2(a):
    for _ in range(len(a)):
        for i in range(1,len(a)):
            if a[i] < a[i-1]:
                a[i-1], a[i] = a[i],a[i-1]

names = ["pretzels, carrots","arugula","bacon"]
bubble_sort2(names)
print(names)

#-----------------------------------------------

snacks = [("bacon", 350),("donut", 240),("muffin", 190)]
for i in range(len(snacks)):
    item = snacks[i]
    name = item[0]
    calories = item[1]
    print(f"{i+1}: {name} has {calories} calories")

#-----------------------------------------------
for rank,(name, calories) in enumerate(snacks,1):
    print(f"{rank}: {name} has {calories} calories")
#-----------------------------------------------   
