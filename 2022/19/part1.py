import re
import numpy as np

input = open('input.txt', 'r').read().strip()

# input = """Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
# Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian."""
  
blueprints_raw = [[int(d[0])for d in re.finditer('\d+', l)] for l in input.splitlines()]

blueprints = np.array([[[b[1], 0, 0, 0], [b[2], 0, 0, 0], [b[3], b[4], 0, 0], [b[5], 0, b[6], 0]] for b in blueprints_raw])

optimum_geodes = [ ( t - 1 ) * t // 2 for t in range( 24 + 1 ) ]

def sim(blueprint):
    maximum_robots = np.array([np.max(blueprint[:,0]), blueprint[2,1], blueprint[3,2], np.inf])
    
    max_geodes = 0
    
    new_robots = np.eye(4, dtype=int)
    
    def search(robots, resources, target_robot, time):
        nonlocal max_geodes
        if (
            robots[target_robot] >= maximum_robots[target_robot] or
            target_robot == 2 and robots[1] == 0 or 
            target_robot == 3 and robots[2] == 0 or
            resources[3] + robots[3] * time + optimum_geodes[time] <= max_geodes
        ):
            return
        
        while time:
            if np.all(blueprint[target_robot] <= resources):
                resources = resources + robots - blueprint[target_robot]
                robots += new_robots[target_robot]
                for new_target in range(4):
                    search(np.copy(robots), np.copy(resources), new_target, time - 1)
                return
            
            resources += robots
            time -= 1
        
        max_geodes = max(max_geodes, resources[3])
    
    for target in range(4):
        search(np.array([1, 0, 0, 0]), np.zeros(4, dtype=int), target, 24)
    
    return max_geodes


result = sum(n * sim(bp) for n, bp in enumerate(blueprints, 1))
print(f"Result: {result}",)