from dataclasses import dataclass
from enum import IntEnum
from typing import List

class PacketType(IntEnum):
  Literal = 4
  
@dataclass
class Packet:
  version: int
  type: PacketType

@dataclass
class LiteralPacket(Packet):
  literal: int
  
@dataclass
class ContainerPacket(Packet):
  children: List[Packet]

def parse_int(buf, length):
  return int(buf[:length], 2), buf[length:]

def parse_header(buf):
  version, buf = parse_int(buf, 3)
  type, buf = parse_int(buf, 3)
  return Packet(version, type), buf

def parse_literal(buf):
  literal = ""
  while True:
    literal += buf[1:5]
    i, buf = buf[0], buf[5:]
    if i == "0":
      break
  return int(literal, 2), buf

def parse_sub_packet_bytes(buf):
  length, buf = parse_int(buf, 15)
  packet_buf, buf = buf[:length], buf[length:]
  
  children = []
  while packet_buf:
    p, packet_buf = parse_packet(packet_buf)
    children.append(p)
    
  return children, buf

def parse_sub_packet_count(buf):
  count, buf = parse_int(buf, 11)
  
  children = []
  while len(children) < count:
    p, buf = parse_packet(buf)
    children.append(p)
    
  return children, buf

def parse_packet(buf):
  packet, buf = parse_header(buf)
  
  if packet.type == PacketType.Literal:
    literal, buf = parse_literal(buf)
    packet = LiteralPacket(**packet.__dict__, literal=literal)
  else:
    type_id, buf = parse_int(buf, 1)
    if type_id == 0:
      children, buf = parse_sub_packet_bytes(buf)
    else:
      children, buf = parse_sub_packet_count(buf)
    packet = ContainerPacket(**packet.__dict__, children=children)
  
  return packet, buf
    

input = open('input.txt', 'r').read().strip()

buf = bin(int(input, 16))[2:]
if len(buf) % 4:
  buf = "0" * (4 - len(buf) % 4) + buf

p, _ = parse_packet(buf)

# sum version
def sum_version(p):
  if isinstance(p, ContainerPacket):
    return p.version + sum(sum_version(c) for c in p.children)
  return p.version

result = sum_version(p)
print("Result: {}".format(result))
