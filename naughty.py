"""The Naughty Way

This is a very bad way of implementing a Secret Santa that has a very high
likelihood of allocating someone to buy a gift for themself.
"""
from random import sample  # remember shuffle is in place

from christmas import merry_christmas, EVERYONE, secret_santa

num_people = len(EVERYONE)

# 🎅 Santa Says Hello
merry_christmas()
secret_santa()

# Draw names out of the hat.
secret_santa = zip(
    list(sample(EVERYONE, k=num_people)), list(sample(EVERYONE, k=num_people))
)

print(*[f"{ss[0]} gives a 🎁 to {ss[1]}" for ss in secret_santa], sep="\n")
