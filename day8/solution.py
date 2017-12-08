# load instruction and replace dec/inc with python equivalents -=/+=
instructions = [l.replace(' dec ', ' -= ').replace(' inc ', '+=') for l in open("input.txt").readlines()]

# init global variables to 0
for __i in instructions:
	globals()[__i.split()[0]] = 0

# execute each instruction. <3 python
__m = 0
for __i in instructions:
	exec(__i.rstrip() + ' else 0')
	__m = max([__g for __g in globals().values() if type(__g) is int])


print(max(__g for __k, __g in globals().items() if __k != '__m' and type(__g) is int))
print(__m)