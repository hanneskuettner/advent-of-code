import networkx as nx

cavern = nx.Graph()
for i, l in enumerate(open('input.txt').readlines()):
  for j, r in enumerate(l.strip()):
    cavern.add_node((i, j), risk=int(r))
    if i > 0:
      cavern.add_edge((i-1, j), (i , j))
    if j > 0:
      cavern.add_edge((i, j-1), (i, j))

target = (i, j)
      
path = nx.algorithms.shortest_path(cavern, (0, 0), target, weight=lambda u, v, d: cavern.nodes[u]["risk"] + cavern.nodes[v]["risk"])

print(sum(cavern.nodes[n]["risk"] for n in path) - cavern.nodes[(0, 0)]["risk"])