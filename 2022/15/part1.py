import re
import numpy as np

input = open('input.txt', 'r').read().strip()

Y_TARGET = 2000000

sensor_beacon_coords = np.array([[int(x.group()) for x in re.finditer(r'-?\d+', l)] for l in input.splitlines()])

sensors = sensor_beacon_coords[:, :2]
beacons = sensor_beacon_coords[:, 2:]

min_x = min(sensors[:,0].min(), beacons[:,0].min())
max_x = max(sensors[:,0].max(), beacons[:,0].max())

# determine sensors sensing distances by looking at distance to beacon
sensing_distances = np.sum([np.abs(sensors[:,0] - beacons[:,0]), np.abs(sensors[:,1] - beacons[:,1])], axis=0)
# determine distance to Y_TARGET by looking at y offset
distance_to_y_target = np.abs(sensors[:,1] - Y_TARGET)

# the sensor only impacts target line if the sensing distance is greater equal than the distance to the target
mask = sensing_distances >= distance_to_y_target

# looking at the pattern of one sensor we can see that the amount of 
# space occupied by one sensor is how "deep" the target is within the 
# area of effect of the sensor. This deepness we will call overlap distance.
# A sensor that is 2 squares away from the target and has a total range of 9
# has an overlap distance of 7
overlap_distances = sensing_distances[mask] - distance_to_y_target[mask]

# now we only need to determine the start and end points of each sensor on the target row
# and find their overlaps
starts = sensors[mask, 0] - overlap_distances
ends = sensors[mask, 0] + overlap_distances
ranges = np.vstack([starts, ends]).T

# sort them by start and then by end
sorted_ranges = np.array(sorted(ranges, key=lambda r: r[0] * max_x + r[1]))

# sum up the ranges
last_range_end = sorted_ranges[0,0]
count = 0
for start, end in sorted_ranges:
    if end < last_range_end:
        continue
    if start < last_range_end:
        start = last_range_end
    
    last_range_end = end
    count += end - start
    
print(count)
    