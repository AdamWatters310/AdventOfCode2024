import networkx as nx

g = nx.Graph()

for line in open("input.txt").read().splitlines():
    a, b = line.split("-")
    g.add_edge(a, b)

maxcl = []
for c in nx.enumerate_all_cliques(g):
    if len(c) > len(maxcl):
        maxcl = c

print(",".join(sorted(maxcl)))

