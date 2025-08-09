"""
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). 
Make sure your program works on two lists of different sizes.

Extras:

   1. Randomly generate two lists to test this
   2. Write this in one line of Python
"""

import random

# Hard-coded lists from example

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

for i in a:
    if i in b and i not in c:  # Make sure existing elements from list A is not in list B
        c.append(i)
print("New list", c)

# 1. Randomly generate two lists to test this (Extra 1):


def randomize_lists(size, start=1, end=50):
    return random.sample(range(start, end), size)


def find_common_elements(list_a, list_b):
    return list(set(list_a) & set(list_b))  # Sets => only unique values, O(1)


list_a = randomize_lists(10)
list_b = randomize_lists(11)
print(f"List 1 (random): {list_a}")
print(f"List 2 (random): {list_b}")
print(f"Common (random): {find_common_elements(list_a, list_b)}")

# 2. Write this in one line of Python
print(f"One liner, common elements: {list(set(a) & set(b))}")
