import math
from dataclasses import dataclass
from typing import List, Optional
from itertools import product

@dataclass
class SnailNumber:
  value: Optional[int]
  children: Optional[List]
  prev: Optional[object]
  next: Optional[object]
  
  def __init__(self, n, parent=None, depth=0):
    self.value = n if isinstance(n, int) else None
    self._depth = depth
    self.parent = parent
    self.prev = None
    self.next = None
    self.children = [SnailNumber(d, self, depth + 1) for d in n] if isinstance(n, list) else []
    
    if self.children:
      self.children[0].last_descendant().next = self.children[1].first_descendant()
      self.children[1].first_descendant().prev = self.children[0].last_descendant()
    
    
  def first_descendant(self):
    if self.children:
      return self.children[0].first_descendant()
    return self
  
  def last_descendant(self):
    if self.children:
      return self.children[1].last_descendant()
    return self
    
  def as_list(self):
    return [c.as_list() for c in self.children] if self.children else self.value
  
  def __len__(self):
    return sum(len(c) for c in self.children) if self.children else 1
  
  def __getitem__(self, idx):
    if self.children:
      c0_len = len(self.children[0])
      if idx < c0_len:
        return self.children[0][idx]
      else:
        return self.children[1][idx - c0_len]
    return self
  
  def replace_child(self, child, new_child):
    self.children[self.children.index(child)] = new_child
  
  def _explode(self):
    # add left to prev value and right to next and replace this node in linked list by new node
    lvalue, rvalue = [c.value for c in self.children]
    new_node = SnailNumber(0, self.parent, self._depth)
    
    if self.children[0].prev:
      new_node.prev = self.children[0].prev
      self.children[0].prev.value += lvalue
      self.children[0].prev.next = new_node
    if self.children[1].next:
      new_node.next = self.children[1].next
      self.children[1].next.value += rvalue
      self.children[1].next.prev = new_node
    
    # replace this node in parent with new node
    self.parent.replace_child(self, new_node)
  
  def _split(self):
    lvalue, rvalue = math.floor(self.value / 2), math.ceil(self.value / 2)
    new_node = SnailNumber([lvalue, rvalue], self.parent, self._depth)

    new_node.children[0].next = new_node.children[1]
    new_node.children[1].prev = new_node.children[0]
    
    if self.prev:
      new_node.children[0].prev = self.prev
      self.prev.next = new_node.children[0]
    if self.next:
      new_node.children[1].next = self.next
      self.next.prev = new_node.children[1]
      
    self.parent.replace_child(self, new_node)
  
  def _try_explode(self):
    if self.children and self._depth >= 4 and not any(c.children for c in self.children):
      self._explode()
      return True
    
    for c in self.children:
      if c._try_explode():
        return True
    return False
  
  def _try_split(self):
    if self.value is not None and self.value > 9:
      self._split()
      return True

    for c in self.children:
      if c._try_split():
        return True
    return False
  
  def _reduce(self):
    return self._try_explode() or self._try_split()
    

  def __add__(self, other):
    n = SnailNumber([self.as_list(), other.as_list()])
    while n._reduce(): 
      pass
    
    return n
  
  @property
  def magnitude(self):
    if self.children:
      return self.children[0].magnitude * 3 + self.children[1].magnitude * 2
    return self.value
  
  def to_str(self):
    if self.children:
      return f"[{self.children[0].to_str()},{self.children[1].to_str()}]"
    return str(self.value)

input = open('input.txt', 'r').read().strip()

numbers = [eval(l) for l in input.splitlines()]
numbers = [SnailNumber(n) for n in numbers]

max_magnitude = 0
for a, b in product(numbers, repeat=2):
  m = (a + b).magnitude
  if m > max_magnitude:
    max_magnitude = m

result = max_magnitude
print("Result: {}".format(result))
