from typing import List


def display_matrix(name: str, matrix: List[List[int]]) -> None:
    print(f'{name} MATRIX')
    for r in matrix:
        print(r)
    print()


# It does not seem unreasonable to assume the following two matrixes should behave the same
matrix_one = [[1]*5]*5
matrix_two = [[1 for _ in range(5)] for _ in range(5)]

# If we inspect them, we see what we would expect
display_matrix('FIRST', matrix_one)
display_matrix('SECOND', matrix_two)

'''
However, if we apply a change to each of these matrices, we get odd behavior

For our example we will attempt to increment only the third element of the third row, i.e. (2, 2)

We would expect a call to `display_matrix('FIRST', matrix_one)` to produce:

FIRST MATRIX
[1, 1, 1, 1, 1]
[1, 1, 1, 1, 1]
[1, 1, 2, 1, 1]
[1, 1, 1, 1, 1]
[1, 1, 1, 1, 1]
'''

matrix_one[2][2] += 1
display_matrix('FIRST', matrix_one)

'''
We see however that the third element of *all* rows were incremented!

This is particularly surprising behavior

We can see the same operation applied to the second matrix gives us our desired behavior
'''

matrix_two[2][2] += 1
display_matrix('SECOND', matrix_two)

'''
Ultimately, what is happening here is implicit list referencing.

Meaning that the following:
    matrix = [[some_val] * some_int] * some_int

Is behaving more like:
    matrix = some_int * reference to -> [some_val, some_val, ..., some_val]

Or stated another way:
    underlying_list = [some_val, some_val, ..., some_val]
    matrix = [ref_to_underlying_list, ref_to_underlying_list, ..., ref_to_underlying_list]

Rather than creating `some_int` number of unique lists, python chooses to make one list, 
and then create `some_int` number of references to it.

This behavior is extremely unintuitive and implicit.

We can see that this strange behavior extends out to other heap-allocated data types as well.

When making nested data structures in Python, take care to avoid this sneaky footgun.
'''

# Multiplyer merely making `n` number of references
list_of_dict = [{i:i for i in range(5)}]*5
assert list_of_dict[0] is list_of_dict[1]

# Iterably make `n` number of distict innner data structures
list_of_dict = [{i:i for i in range(5)} for _ in range(5)]
assert list_of_dict[0] is not list_of_dict[1]
