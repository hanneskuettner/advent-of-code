import networkx as nx

cavern = nx.Graph()
lines = open('input.txt').read().strip().splitlines()

h, w = len(lines), len(lines[0])
for mi in range(5):
  for mj in range(5):
    for i, l in enumerate(lines):
      for j, r in enumerate(l.strip()):
        risk = int(r)
        risk = (risk + mi + mj) // 10 + (risk + mi + mj) % 10
        pi, pj = mi * w + i, mj * h + j
        cavern.add_node((pi, pj), risk=risk)
        if pi > 0:
          cavern.add_edge((pi-1, pj), (pi, pj))
        if pj > 0:
          cavern.add_edge((pi, pj-1), (pi, pj))

target = pi, pj
path = nx.algorithms.shortest_path(cavern, (0, 0), target, weight=lambda u, v, d: cavern.nodes[u]["risk"] + cavern.nodes[v]["risk"])

print(sum(cavern.nodes[n]["risk"] for n in path) - cavern.nodes[(0, 0)]["risk"])