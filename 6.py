#-----------------------------------------------
first = (1,2,3)
second = (1,2,3,)
second_wrapped = (
    1,
    2,
    3, #末尾のカンマ
)
third = 1,2,3
fourth = 1,2,3,

assert first == second == third == fourth
#assert first == second == third != fourth #Assertion Errorが出る

#-----------------------------------------------
empty = ()

single_with =(1,)
single_without = (1)
assert single_with != single_without
assert single_with[0] == single_without
#-----------------------------------------------

single_parens = (1,)
single_no_parens = 1,
assert single_parens == single_no_parens
#-----------------------------------------------

"""
to_refund = calculate_refund(
    get_order_value(user, order.id),
    get_tax(user.address, order.dest),
    adjust_discount(user) + 0.1),

print(type(to_refund))
"""

"""
to_refund2 = calculate_refund(
    get_order_value(user, order.id),
    get_tax(user.address, order.dest),
    adjust_discount(user) + 0.1
)
print(type(to_refund2))
"""
#-----------------------------------------------

value_a = (1,)
list_b = [1,]
list_c = [(1,)]
print("A:", value_a)
print("B:", list_b)
print("C:", list_c)

#-----------------------------------------------
"""
def get_coupon_codes(user):
    return[['DEAL20']]

(a1,), = get_coupon_codes(user)
(a2,) = get_coupon_codes(user)
(a3), = get_coupon_codes(user)
(a4) = get_coupon_codes(user)
a5, = get_coupon_codes(user)
a6  = get_coupon_codes(user)

assert a1 not in (a2, a3, a4, a5, a6)
assert a2 == a3 == a5
assert a4 =-a6

"""    
#単一要素のタプルは常に丸かっこで囲むべき
#-----------------------------------------------