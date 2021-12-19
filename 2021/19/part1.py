import numpy as np
import itertools
import math

sqeuclidean = lambda x: np.inner(x, x)

def calc_rotations():
  bases = np.vstack([np.eye(3), -np.eye(3)])
  rs = []
  for e1 in bases:
    for e2 in bases:
      if np.dot(e1, e2) == 0:
        e3 = np.cross(e1, e2)
        rs.append(np.array([e1, e2, e3], dtype=int).T)
  return rs

def fingerprint_beacons(beacons):
  return set(sqeuclidean(a - b) for a, b in itertools.combinations(beacons, r=2))

def matching_fingerprints(fingerprints):
  for i, j in itertools.combinations(range(len(fingerprints)), 2):
    if len(fingerprints[i] & fingerprints[j]) >= math.comb(12, 2):
      yield i, j

def fit_to_beacons(beacon_set, related_beacons, scanned_beacons, rotations):
  for r in rotations:
    scanned_rotated = (r @ scanned_beacons.T).T
    for p1 in related_beacons:
      for p2 in scanned_rotated:
        offset = p1 - p2
        if len(beacon_set & (transformed := set(map(tuple, scanned_rotated + offset)))) >= 12:
          return offset, beacon_set | transformed, r

input = open('input.txt', 'r').read().strip()

scanned_beacons = [np.array([list(map(int, l.split(','))) for l in s.split("---\n")[-1].splitlines()]) for s in input.split("\n\n")]

fingerprints = list(map(fingerprint_beacons, scanned_beacons))
rotations = calc_rotations()

beacon_set = set(map(tuple, scanned_beacons[0]))
beacons = scanned_beacons[:]
scanners = {0: np.zeros(3)}
while len(scanners) < len(scanned_beacons):
  for i, j in matching_fingerprints(fingerprints):
    if not (i in scanners) ^ (j in scanners):
      continue
    elif j in scanners:
      i, j = j, i
    scanners[j], beacon_set, rotation = fit_to_beacons(beacon_set, beacons[i], scanned_beacons[j], rotations)
    beacons[j] = (rotation @ beacons[j].T).T + scanners[j]

result = len(beacon_set)
print("Result: {}".format(result))
