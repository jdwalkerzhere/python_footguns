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

"""
This behavior is because all variables are essentially pointers
you can get the "address" (not real memory addres) with id(variable)
"""

print(id(x))
print(id(y))
print(id(z))

print(id(5))  # fun fact that literals also have an id
print(id(False))
print(id("5"))

first = 5
second = 5

assert first is second
print(id(first), id(second))

# literals are not mutable, so the id of second gets changed
second += 1
assert first is not second
print(id(first), id(second))

# an object does not need to be named to have an id
print(id({1: x, 2: y, 3: z}))

dic = {1: x, 2: y, 3: z}
dic2 = {1: x, 2: y, 3: z}
print(id(dic))
print(id(dic2))
dic[4] = [0, 0, 0, 0]
print(id(dic))
print(id(dic2))
print(dic)

assert dic is not dic2

