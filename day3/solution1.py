#!/usr/bin/env python3
import math
import sys
req = int(sys.argv[1])

def shell_start(layer):
	return 4 * layer * (layer - 1) + 2

def calc_layer(val):
	lower = 1
	layer = 0
	while val >= lower:
		layer += 1
		lower = shell_start(layer)
	return layer - 1

def calc_dist_to_mid(val, layer):
	start = shell_start(layer)
	return abs(layer - (val - start + 1) % (layer * 2))


print(calc_layer(req) + calc_dist_to_mid(req, calc_layer(req)))