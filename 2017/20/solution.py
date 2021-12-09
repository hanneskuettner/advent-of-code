from collections import defaultdict

def distance(v):
	return abs(v[0]) + abs(v[1]) + abs(v[2])

def check_collisions(ps):
	collisions = defaultdict(list)
	for i, p in enumerate(ps):
		collisions[tuple(p.p)].append(p)

	for p in collisions.values():
		if len(p) > 1:
			for i in p:
				ps.remove(i)


class Particle:
	def __init__(self, s):
		p, v, a = [[int(c) for c in p.split('=')[1][1:-1].split(',')] for p in s.split(', ')]
		self.p = p
		self.v = v
		self.a = a

	def tick(self):
		for i in range(3):
			self.v[i] += self.a[i]
			self.p[i] += self.v[i]

particles = [Particle(l.strip()) for l in open('input.txt').readlines()]

print(min(enumerate(particles), key=lambda p: distance(p[1].a))[0])

for i in range(50):
	for p in particles:
		p.tick()
	check_collisions(particles)

print(len(particles))