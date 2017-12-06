#!/usr/bin/env python3

ins = [int(l.strip()) for l in open("input.txt").readlines()]
curr = 0
steps = 0
try:
	while True:
		tmp = curr
		curr += ins[tmp]
		ins[tmp] += 1 if ins[tmp] < 3 else -1
		steps += 1
except IndexError:
	print(steps)
