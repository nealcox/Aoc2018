#61, 10
from collections import defaultdict
from collections import namedtuple
import re

INPUT = "10-test-input.txt"
INPUT = "10-input.txt"


def print_board(board, minx, miny):
    for y in range(miny, miny + 20):
        for x in range(minx, minx + 90):
            if board[x,y] == 1:
                print("#", end="")
            else:
                print(".", end="")
        print()

Particle = namedtuple('Particle', ['x', 'y', 'vx', 'vy'])
particles = []
board = defaultdict(int)
with open(INPUT, 'r') as infile:
    for line in infile:
        stuff = re.split('<|>|,|:|x|\n',line)

        particles.append(Particle(int(stuff[1]), int(stuff[2]), int(stuff[4]), int(stuff[5])))
print(particles)
mindx = float("inf")
for second in range(100000):
    maxx = -float("inf")
    minx = float("inf")
    maxy = -float("inf")
    miny = float("inf")
    for particle in particles:
        if particle.x > maxx:
            maxx = particle.x
        if particle.x < minx:
            minx = particle.x
        if particle.y > maxy:
            maxy = particle.y
        if particle.y < miny:
            miny = particle.y
#    print(f"{second} dx: {maxx - minx} dy: {maxy - miny}")
    if maxx - minx < mindx:
        mindx = maxx - minx
    elif maxx - minx >= mindx:
        break

    for i, particle in enumerate(particles):
        particles[i] = Particle(particle.x+particle.vx,particle.y+particle.vy,
                particle.vx, particle.vy)

for i, particle in enumerate(particles):
    particles[i] = Particle(particle.x-particle.vx,particle.y-particle.vy,
            particle.vx, particle.vy)
    board[(particles[i].x, particles[i].y)] += 1



print(second-1)
for i, particle in enumerate(particles):
    board[(particles[i].x, particles[i].y)] += 1
for y in range(miny, miny + 20):
    for x in range(minx, minx + 90):
        if board[x,y] >= 1:
            print("#", end="")
        else:
            print(".", end="")
    print()

