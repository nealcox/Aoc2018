from collections import defaultdict
from collections import namedtuple


Point = namedtuple('Point', ['x', 'y'])
original_points = []

INPUT = "6-input.test"
INPUT = "6-input.txt"

max_distance = 32
max_distance = 10000


def point_is_valid(p):
    return (p.x >= minx and p.x <= maxx and p.y >= miny and p.y <= maxy)

def fill_grid(distance):
    changed_points = []
    for dx in range(-distance, distance +1):
        dy = distance - abs(dx)
        for i, p in enumerate(original_points):
            q = Point(p.x + dx, p.y + dy)
            if point_is_valid(q):
                if q in changed_points:
                    if grid[q] != i:
                        grid[q] = -1
                else:
                    if q not in grid.keys():
                        grid[q] = i
                        changed_points.append(q)
            q = Point(p.x + dx, p.y - dy)
            if point_is_valid(q):
                if q in changed_points:
                    if grid[q] != i:
                        grid[q] = -1
                else:
                    if q not in grid.keys():
                        grid[q] = i
                        changed_points.append(q)
    if len(changed_points) > 0:
        return True

def score_grid(distance):
    changed_points = []
    for dx in range(-distance, distance +1):
        dy = distance - abs(dx)
        
        q = Point(averagex + dx, averagey + dy)
        r = Point(averagex + dx, averagey - dy)
        scoreq = 0
        scorer = 0
        for p in original_points:
            scoreq += abs(p.x - q.x) + abs(p.y - q.y)
            scorer += abs(p.x - r.x) + abs(p.y - r.y)
        if scoreq < max_distance:
            grid[q] = scoreq
            changed_points.append(q)

        if scorer < max_distance:
            grid[r] = scorer
            changed_points.append(r)

       # print(f"q: {q}, score: {scoreq}\nr: {r}, {scorer}")

    if len(changed_points) > 0:
        return True

def print_grid():
    for y in range(miny, maxy+1):
        for x in range(minx, maxx + 1):
            p = Point(x,y)
            if p in grid.keys() and grid[p] > -1:
                c = grid[p]
            else:
                c = '.'
            print(c, end="")
    print()

with open(INPUT, 'r') as infile:
    for line in infile:
        line_as_list = line.strip().split(',')
        x,y = int(line_as_list[0]), int(line_as_list[1])
        original_points.append(Point(x,y))

minx = float("inf")
maxx = -float("inf")
miny = float("inf")
maxy = -float("inf")

totalx = 0
totaly = 0
grid = {}
original_at_x = defaultdict(int)
original_at_y = defaultdict(int)

for i, p in enumerate(original_points):
    #print(p.x,p.y)
    if p.x < minx:
        minx = p.x
    if p.x > maxx:
        maxx = p.x
    if p.y < miny:
        miny = p.y
    if p.y > maxy:
        maxy = p.y
    totalx += p.x
    totaly += p.y
    original_at_x[p.x] += 1
    original_at_y[p.y] += 1


minx = minx -1
maxx = maxx +1
miny = miny -1
maxy = maxy +1
averagex = int(totalx / len(original_points))
averagey = int(totaly / len(original_points))
average_point = Point(averagex, averagey)

score_average_point = 0
for p in original_points:
    score_average_point += abs(p.x - averagex) + abs(p.y - averagey)
#print(f"average point {average_point}\nscore {score_average_point}")


if score_average_point >= max_distance:
    print("FUCK, FUCK, FUCK")
change_made = True
distance = 0
while change_made:
#    change_made = fill_grid(distance)
#    distance += 1
    change_made = score_grid(distance)
    distance += 1


print(len(grid))
#
#infinite_range_points = set()
#
#for y in range(miny, maxy + 1):
#    infinite_range_points.add(grid[Point(maxx,y)])
#    infinite_range_points.add(grid[Point(minx, y)])
#
#for x in range(minx, maxx + 1):
#    infinite_range_points.add(grid[Point(x,maxy)])
#    infinite_range_points.add(grid[Point(x, miny)])
#
##print(infinite_range_points)
#
#count_for_each_original_point = defaultdict(int)
#for p, original_point in grid.items():
#    count_for_each_original_point[original_point] += 1
#
#for i in range(len(original_points)):
#    if i not in infinite_range_points:
#        print(i, count_for_each_original_point[i])
