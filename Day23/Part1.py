import networkx as nx

g = nx.Graph()

for line in open("input.txt").read().splitlines():
    a, b = line.split("-")
    g.add_edge(a, b)

count=0
for c in nx.enumerate_all_cliques(g):
    if len(c) == 3:
        if "t" == c[0][0] or "t" == c[1][0] or "t" == c[2][0]:
            count+=1
print(count)

