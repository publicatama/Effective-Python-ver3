#----------------------------------------------- 
def take_action(light):
    if light == "red":
        print("Stop")
    elif light == "yellow":
        print("Slow down")
    elif light == "green":
        print("Go")
    else:
        raise RuntimeError
    
take_action("red")
take_action("yellow")
take_action("green")
#----------------------------------------------- 

def take_match_action(light):
    match light:
        case "red":
            print("Stop")
        case "yellow":
            print("Slow down")
        case "green":
            print("Go!")
        case _:
            raise RecursionError

take_match_action("red")
take_match_action("yellow")
take_match_action("green")
#----------------------------------------------- 

"""
def take_constant_action(light):
    match light:
        case RED:
            print("Stop")
        case YELLOW:
            print("Slow down")
        case GREEN:
            print("Go!")
        case _:
            raise RecursionError
"""
#----------------------------------------------- 
RED = "red"
YELLOW = "yellow"
GREEN = "green"

def take_truncated_action(light):
    match light:
        case RED:
            print("Stop")
        
take_truncated_action(GREEN)
#----------------------------------------------- 

def take_debug_action(light):
    match light:
        case RED:
            print(f"{RED=}, {light=}")
take_debug_action(GREEN)

def take_unpacking_action(light):
    try:
        (RED,) = (light,)
    except TypeError:
    
    #else:
        print(f"{RED=}, {light=}")
#----------------------------------------------- 

import enum

class ColorEnum(enum.Enum):
    RED = "red"
    YELLOW = "yellow"  
    GREEN = "green"

def take_enum_action(light):
    match light:
        case ColorEnum.RED:
            print("Stop")
        case ColorEnum.YELLOW:
            print("Slow down")
        case ColorEnum.GREEN:
            print("Go!")
        case _:
            raise RecursionError
#----------------------------------------------- 

for index, value in enumerate("abc"):
    print(f"index {index} is {value}")

my_tree = (10, (7, None, 9),(13,11,None))

def contains(tree, value):
    if not isinstance(tree, tuple):
        return tree == value
    
    pivot, left, right = tree
    
    if value < pivot:
        return contains(left, value)
    elif value > pivot:
        return contains(right, value)
    else:
        return value == pivot
assert contains(my_tree, 9)
assert not contains(my_tree, 14)

def contains_match(tree, value):
    match tree:
        case pivot, left, _ if value < pivot:
            return contains_match(left, value)
        case pivot, _, right if value > pivot:
            return contains_match(left, value)
        case (pivot, _, _,) | pivot:
            return pivot == value

#----------------------------------------------- 
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

obj_tree = Node(
    value=10,
    left=Node(value=7,right=9),
    right=Node(value=13, left=11),    
)

def contains_class(tree, value):
    if not isinstance(tree, Node):
        return tree == value
    elif value < tree.value:
        return contains_class(tree.left, value)
    elif value > tree.value:
        return contains_class(tree.right, value)
    else:
        return tree.value == value
    
#----------------------------------------------- 
def contains_match_class(tree, value):
    match tree:
        case Node(value=pivot, left=left) if value < pivot:
            return contains_match_class(left,value)
        case Node(value=pivot, right=right) if value > pivot:
            return contains_match_class(right,value)
        case Node(value = pivot) | pivot:
            return pivot == value
#----------------------------------------------- 

record1 = """{"customer": {"last": "Ross", "first": "Bob"}}"""        
record2 = """{"customer": {"entity": "Steve's Painting Co."}}"""          

from dataclasses import dataclass

@dataclass
class PersonCustomer:
    first_name : str
    last_name : str

@dataclass
class BusinessCustomer:
    company_name: str

import json
def deserialize(data):
    record = json.loads(data)
    match record:
        case {"customer": {"last": last_name, "first": first_name}}:
            return PersonCustomer(first_name, last_name)
        case {"customer": {"entity": company_name}}:
            return BusinessCustomer(company_name)
        case _:
            raise ValueError("Unknown Record Type")

print("Record1 ", deserialize(record1))
print("Record2 ", deserialize(record2)) 
#----------------------------------------------- 