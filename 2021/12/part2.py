import networkx as nx

input = open('input.txt', 'r').read().strip()

cave = nx.Graph()
for line in input.splitlines():
  cave.add_edge(*line.split('-'))

queue = [("start", set(["start"]), False)]
path_count = 0
while queue:
  current, visited, double = queue.pop()
  new_paths = []
  
  if current == "end":
    path_count += 1
    continue
  
  for label in cave[current]:
    if label == "start":
      continue
    if (label not in visited
        or label.isupper()
        or (not double and label in visited)):
      # unvisited small cave or large cave
      new_paths.append((label, visited | set([label]), double or label.islower() and label in visited))
      
  
  if new_paths:
    queue.extend(new_paths)

result = path_count
print("Result: {}".format(result))
