import networkx as nx

input = open('input.txt', 'r').read().strip()

cave = nx.Graph()
for line in input.splitlines():
  cave.add_edge(*line.split('-'))

queue = [["start"]]
path_count = 0
while queue:
  path = queue.pop()
  new_paths = []
  
  if path[-1] == "end":
    path_count += 1
    continue
  
  for label, nbr in cave[path[-1]].items():
    if label == "start":
      continue
    if (label not in path 
        or label.upper() == label 
        or (label in path and all(l.upper() == l or path.count(l) < 2 for l in path))):
      # unvisited small cave or large cave
      new_paths.append(path + [label])
  
  if new_paths:
    queue.extend(new_paths)

result = path_count
print("Result: {}".format(result))
