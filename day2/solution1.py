#!/usr/bin/env python3

rows = [[int(v) for v in l.split()] for l in open('input.txt').readlines()]

print(sum([max(r) - min(r) for r in rows]))