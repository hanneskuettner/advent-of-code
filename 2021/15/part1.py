import networkx as nx
import numpy as np

grid = np.genfromtxt("input.txt", dtype=int, delimiter=1)
cavern = nx.grid_2d_graph(*grid.shape, create_using=nx.DiGraph)
for (_, v), e in cavern.edges.items():
    e["risk"] = grid[v]
    
source, *_, target = cavern.nodes
length = nx.shortest_path_length(cavern, source, target, weight="risk")

print(length)