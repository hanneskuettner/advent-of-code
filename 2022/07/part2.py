from dataclasses import dataclass
from typing import Dict

input = open('input.txt', 'r').read().strip()

@dataclass
class Node:
  name: str
  
  @property
  def size(self):
    return -1
  
@dataclass
class File(Node):
  _size: int
  
  @Node.size.getter
  def size(self):
    return self._size
  
@dataclass
class Dir(Node):
  entries: Dict[str, Node]
  
  @Node.size.getter
  def size(self):
    return sum(e.size for e in self.entries.values())


commands_and_output = [(c.strip(), o) for c, *o in [c.splitlines() for c in input.split('$')[1:]]]

current_path = [Dir("/", {})]
dirs = current_path[:]
for command, output in commands_and_output[1:]:
  if command.startswith("cd"):
    _, dir = command.split()
    if dir == "..":
      current_path.pop()
    else:
      current_path.append(current_path[-1].entries[dir])
  elif command == "ls":
    for type_or_size, name in [l.split() for l in output]:
      if type_or_size == "dir":
        dir = Dir(name, {})
        current_path[-1].entries[name] = dir
        dirs.append(dir)
      else:
        current_path[-1].entries[name] = File(name, int(type_or_size))

AVAILABLE_SPACE = 70000000
NEEDED_SPACE = 30000000
root_size = dirs[0].size

current_space = AVAILABLE_SPACE - root_size
to_delete = next(d for d in sorted(dirs, key=lambda d: d.size) if current_space + d.size > NEEDED_SPACE)
print(f"Result: {to_delete.size}")
