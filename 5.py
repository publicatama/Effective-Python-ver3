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