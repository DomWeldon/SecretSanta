"""The Nice Way

This way simply shuffles the list of people and then treats them as a circle
and produces a Hamiltonian path by assigning each person the next person in
the cycle. Sequence approach means it works for an odd number of people.
"""
from itertools import cycle
from random import sample  # remember shuffle is in place

from christmas import merry_christmas, EVERYONE, secret_santa  # 🎅

num_people = len(EVERYONE)

# 🎅 Santa Says Hello
merry_christmas()
secret_santa()

# Let's make a graph...
ss = cycle(list(sample(EVERYONE, k=num_people)))
i, prev = 0, next(ss)

while i < num_people:
    current = next(ss)
    print(f"{prev} gives a 🎁 to {current}")
    i, prev = i + 1, current
