"""Brute-Force Hamiltonian Method

This is a basic brute-force method of finding the first Hamiltonian path
in a graph where some people cannot buy gifts for others.
"""
from itertools import combinations
from random import sample  # remember shuffle is in place

import networkx as nx

from christmas import merry_christmas, EVERYONE, secret_santa

num_people = len(EVERYONE)

# 🎅 Santa Says Hello
merry_christmas()
secret_santa()

G = nx.Graph()
for p in EVERYONE:
    G.add_node(p)

possibles = set(list(combinations(EVERYONE, 2)))
haters = set(list(sample(possibles, k=6)))
for a, b in haters:
    print(f"{a} cannot give a 🎁 to {b} or vice versa")

# create a graph where nodes are people and edges mean they *could*
# exchange gifts
haters = haters | {(v, u) for u, v in haters}
for u, v in possibles - haters:
    G.add_edge(u, v)

for i in range(num_people):
    for j in range(num_people):
        for p in nx.all_simple_paths(G, EVERYONE[i], EVERYONE[j]):
            if len(p) == num_people:
                p = iter(p + [p[0]])
                i, prev = 0, next(p)
                while i < num_people:
                    current = next(p)
                    print(f"{prev} gives a 🎁 to {current}")
                    i, prev = i + 1, current
                exit()

# So many people dislike eachother that there is no Hamiltonian path
# There are probably bigger problems here!
print(f"{'🚨'*5} You probably shouldn't be doing a Secret Santa {'🚨'*5}")
