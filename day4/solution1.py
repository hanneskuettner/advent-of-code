#!/usr/bin/env python3

print(sum([1 for l in open('input.txt').readlines() if len(set(l.split())) == len(l.split())]))