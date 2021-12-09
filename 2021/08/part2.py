input = open('input.txt', 'r').read().strip()

patterns, outputs = zip(*[[p.split() for p in l.split("|")] for l in input.splitlines()])


def to_mask(s):
  m = 0
  for i, l in enumerate(range(ord("a"), ord("h"))):
    m |= (chr(l) in s) << (6 - i)
  return m

def get(pattern, length):
  return [to_mask(p) for p in pattern if len(p) == length]

def matches(pattern, mask):
  return [to_mask(p) for p in pattern if to_mask(p) & mask == mask]

def matches_mask(pattern_masks, mask):
  return [p for p in pattern_masks if p & mask == mask]

def read_display(segments, output):
  number = 0
  # sort segments by "on" elements
  sorted_segments = [(i, s) for i, s in sorted(enumerate(segments), key=lambda t: -bin(t[1]).count("1"))]
  for b, digit in enumerate(output):
    digit_mask = to_mask(digit)
    for i, segment in sorted_segments:
      if digit_mask & segment == segment:
        number += i * 10 ** (len(output) - b - 1)
        break
    
  return number

results = []
for pattern, output in zip(patterns, outputs):
  one = get(pattern, 2)[0]
  seven = get(pattern, 3)[0]
  four = get(pattern, 4)[0]
  eight = get(pattern, 7)[0]
  nine = [p for p in matches(pattern, four | seven) if not p == eight][0]

  segment_6 = nine & ~four & ~seven
  segment_4 = eight & ~nine

  two = matches_mask(get(pattern, 5), segment_4)[0]
  three = matches_mask(get(pattern, 5), one)[0]
  five = [p for p in get(pattern, 5) if p not in [two, three]][0]
  six = five | segment_4

  segment_3 = two & ~seven & ~segment_6 & ~segment_4
  zero = eight & ~segment_3
  
  # read display
  results.append(read_display([zero, one, two, three, four, five, six, seven, eight, nine], output))


result = sum(results)
print("Result: {}".format(result))
