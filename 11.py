#----------------------------------------------- 
a= 0b10111011
b= 0xC5F
print("Binary is %d, hex is %d" %(a,b))

#----------------------------------------------- 
key = "my_var"
value = 1.234
formatted = "%-10s = %.2f" % (key, value)
print(formatted)
#----------------------------------------------- 

#reordered_tuple = "%-10s = %.2f" % (value, key) #エラー
#reordered_string = "%.2f = %-10s" % (key, value) #エラー

pantry = [
    ("avocados", 1.25),
    ("bananas", 2.5),
    ("cherries", 15),
]
for i, (item, count) in enumerate(pantry):
    print("%d: %-10s = %.2f" % (i, item, count))
   

for i, (item, count) in enumerate(pantry):
    print(
        "%d: %-10s = %d"
        % (
            i+1,
            item.title(),
            round(count),
        )
    )

template = "%s loves food. See %s cook."
name = "Max"
formatted = template % (name, name)
print(formatted)

name = "brad"
formatted = template % (name.title(), name)
print(formatted)
#----------------------------------------------- 

key = "my_var"
value = 1.234
old_way = "%-10s = %.2f" % (key, value)
new_way = "%(key)-10s = %(value).2f" % {
    "key": key, 
    "value": value,
}
reordered = "%(key)-10s = %(value).2f" % {
    "value" : value,
    "key" : key,
}

assert old_way == new_way == reordered

#----------------------------------------------- 

name = "Max"
template = "%s loves food. See %s cook."
before = template % (name, name)
template = "%(name)s loves food. See %(name)s cook."
after = template% {"name": name}

assert before == after
#----------------------------------------------- 

for i, (item, count) in enumerate(pantry):
    before = "%d: %-10s = %d" % (
        i+1,
        item.title(),
        round(count),
    )
    after = "%(loop)d: %(item)-10s = %(count)d" % {
        "loop": i+1,
        "item": item.title(),
        "count": round(count),        
    }
assert before == after
#----------------------------------------------- 

soup = "lentil"
formatted = "Today's soup is %(soup)s." % {"soup": soup}
print(formatted)

menu = {
    "soup": "lentil",
    "oyster": "kumamoto",
    "special": "schnitzel",
}
template = (
    "Today's soup is %(soup)s, "
    "buy one get two %(oyster)s oysters, "
    "and our special entree is %(special)s. "
)
formatted = template % menu
print(formatted)

#----------------------------------------------- 
a= 1234.5678
formatted = format(a, ",.2f")
print(formatted)

b="my string"
formatted = format(b, "^20s")
print("*", formatted, "*")

key = "my_var"
value = 1.234
formatted = "{} ={}".format(key, value)
print(formatted)

formatted = "{:<10} ={:.2f}".format(key, value)
print(formatted)

print("%.2f%%" % 12.5)
print("{} replaces {{}}".format(1.23))

#----------------------------------------------- 
formatted = "{1} = {0}".format(key, value)
print(formatted)

formatted = "{0} loes food. See {0} cook.".format(name)
print(formatted)
#----------------------------------------------- 

for i, (item,count) in enumerate(pantry):
    old_style = "#%d: %-10s = %d" % (
        i+1,
        item.title(),
        round(count),
    )
    new_style = "#{}: {:<10s} = {}".format(
        i+1,
        item.title(),
        round(count),
    )
    assert old_style == new_style

formatted = "First letter is {menu[oyster][0]!r}".format(menu=menu)
print(formatted)

#----------------------------------------------- 
#stf.format()にキーワード引数をあてる

old_template = (
    "Today's soup is %(soup)s, "
    "buy one get two %(oyster)s oysters, "
    "and our special entree is %(special)s."
)
old_formatted = old_template % {
    "soup": "lentil",
    "oyster": "kumamoto",
    "special": "schnitzel",
}
new_template = (
    "Today's soup is {soup}, "
    "buy one get two {oyster} oysters, "
    "and our special entree is {special}."
)
new_formatted = new_template.format(
    soup= "lentil",
    oyster= "kumamoto",
    special= "schnitzel", 
)
assert old_formatted == new_formatted


#----------------------------------------------- 
key = "my_var"
value = 1.234
formatted = f"{key} ={value}"
print(formatted)

formatted = f"{key!r:<10} ={value:.2f}"
print(formatted)

#----------------------------------------------- 
f_string = f"{key:<10} = {value:.2f}"
c_tuple = "%-10s = %.2f" % (key, value)
str_args = "{:<10} = {:.2f}".format(key, value)
str_kw = "{key:<10} = {value:.2f}".format(key=key, value=value)
c_dict = "%(key)-10s = %(value).2f" % {"key" : key, "value" : value}

assert c_tuple == c_dict == f_string
assert str_args == str_kw == f_string

#----------------------------------------------- 

for i, (item, count) in enumerate(pantry):
    old_style = "#%d: %-10s = %d" % (
        i+1,
        item.title(),
        round(count),
    )
    new_style = "#{}: {:<10s} = {}".format(
        i+1,
        item.title(),
        round(count),
    )

f_string = f"#{i+1}: {item.title():<10s} = {round(count)}"
    
assert old_style == new_style == f_string

#----------------------------------------------- 
for i, (item, count) in enumerate(pantry):
    print(f"{i+1}: ",
        f"{item.title():<10s} = ",
        f"{round(count)}"
    )
    

places = 3
number = 1.23456
print(f"My number is {number:.{places}f}")
#----------------------------------------------- 