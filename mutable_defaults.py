from typing import Any, List


class SomeClass:
    def __init__(self, thing: bool = False, stuff: List = []):
        self.thing = thing
        self.stuff = stuff

    def __repr__(self):
        return f'SomeClass(thing={self.thing}, stuff={self.stuff})'

    def append(self, elem: Any):
        self.stuff.append(elem)

    def pop(self, ind: int):
        if ind > len(self.stuff):
            raise IndexError(f'Index [{ind}] out of bounds: length self.stuff [{len(self.stuff)}]')
        self.stuff.pop(ind)

# Create an instance of SomeClass w/out values

something = SomeClass()

# Add some values to the default list

something.append('hi')
something.append('there')
something.append('jeff')

# Remove something from the default list

something.pop(1)

# something.stuff should equal ['hi', 'jeff']

print(f'First Instance of {something}\n')

# Delete this instance of the SomeClass Class

del something

# Make a new instance w/out values (i.e. use defaults)

something_else = SomeClass()

# See that the default list for SomeClass is used

print(f'Second Instance of {something_else}')

# Chage something else

something_else.append('bye, jeff')
something_else.thing = True

# Inspect this instance

print(f'Second Instance of {something_else}\n')

# Delete this instance and Make a new one with defaults

del something_else
new_something = SomeClass()

# Inspect this instance
'''
It is important to note here that the `thing` field of the
third instance is `False` as we defined in the signature.

However, the `stuff` list is still populated with values
that were added to previous instances of `SomeClass`.

So behaviorally, this is a very sneaky footgun. It is not
like a static class variable that is shared among all instances
of a class.
'''

print(f'Third Instance of {new_something}')

# Delete this one, Make a Last One, and DON'T use Defaults

del new_something
last_one = SomeClass(thing=False, stuff=[])
print(f'Last Instance of {last_one}')

'''
So the observation is that when the class is evaluated
Python creates these values in-memory. 

These values are handed to later instances of the class.

In the case of mutable types (like the list displayed above),
these values are passed by reference! So rather than getting
a fresh, empty list, the new instances are getting a reference
to a single list.
'''
