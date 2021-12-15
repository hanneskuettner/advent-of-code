import networkx as nx
import numpy as np

grid = np.genfromtxt("input.txt", dtype=int, delimiter=1)
grid = np.block([[grid + i + j for i in range(5)] for j in range(5)])
grid[grid > 9] -= 9

cavern = nx.grid_2d_graph(*grid.shape, create_using=nx.DiGraph)
for (_, v), e in cavern.edges.items():
    e["risk"] = grid[v]
    
source, *_, target = cavern.nodes
length = nx.shortest_path_length(cavern, source, target, weight="risk")

print(length)