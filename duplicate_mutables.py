from typing import List

x: List = [1, 2, 3]
y: List = x
z: List = x.copy()
w: List = [1, 2, 3]

assert x is y
assert x is not z
assert x == y
assert x == z
assert x is not w
assert x == w

x.append(5)
print(x)  # [1, 2, 3, 5]
print(y)  # [1, 2, 3, 5]
print(z)  # [1, 2, 3]
print()

"""
This behavior is because all variables are essentially pointers
you can get the "address" (not real memory addres) with id(variable)
"""

print(f"id of x: {id(x)}")
print(f"id of y {id(y)}")
print(f"id of z {id(z)}")

print(f"id of 5: {id(5)}")  # fun fact that literals also have an id
print(f"id of False: {id(False)}")
print(f"id of '5' (string): {id('5')}")

first = 5
second = 5

assert first is second
print("ids for first, and second")
print(id(first), id(second))
print()


# literals are not mutable, so the id of second gets changed
second += 1
assert first is not second
print("adding one to second")
print(id(first), id(second))
print()

# an object does not need to be named to have an id
print("nameles dictionary")
print(id({1: x, 2: y, 3: z}))
print()

"""
if you create two mutable variables with the same value, they have different id
if you set one equal to the other, they have the same id, i.e they are literally the same object
"""

dic = {1: x, 2: y, 3: z}
dic2 = {1: x, 2: y, 3: z}
dic3 = dic
print("dic, dic2, dic3")
print(id(dic))
print(id(dic2))
print(id(dic3))
print("updating dic")
dic[4] = [0, 0, 0, 0]
print(id(dic))
print(id(dic2))
print(id(dic3))
print(dic)
print(dic2)
print(dic3)
assert dic is not dic2
assert dic is dic3
assert dic != dic2
assert dic == dic3
