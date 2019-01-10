from collections import defaultdict

def power_level(x,y, grid_serial_number):
    rackid = x + 10
    power_level = rackid * y
    power_level += grid_serial_number
    power_level *= rackid
    power_level = (power_level // 100) % 10
    power_level -= 5
    return power_level

assert power_level(122,79,57) == -5
assert power_level(217,196,39) == 0
assert power_level(101,153,71) == 4

power_by_x_y_size_power = defaultdict(list)
power_for_x_y_size = defaultdict(int)

grid_serial_number = 8868
sample_x = 0
sample_y = 0

#grid_serial_number = 18
#sample_x = 30
#sample_y = 40

#grid_serial_number = 42
#sample_x = 20
#sample_y = 60

grid = []
for x in range(300):
    row = []
    for y in range(300):
        row.append(power_level(x+1, y+1, grid_serial_number))
    grid.append(row)

print(f"grid_serial_number: {grid_serial_number}") 
print(f"grid from {sample_x},{sample_y}")
for y in range(20):
    for x in range(20):
        t =grid[sample_x+x][sample_y+y]
        print("{:3d}".format(t), end="")
    print()

def power_by_square_size(x, y, size):
    if (x,y,size) in power_for_x_y_size.keys():
        return power_for_x_y_size[(x,y,size)]

    if size == 1:
        p = grid[x][y]
    else:
        dop = (x == sample_x and y == sample_y and size == 2)
            
        p = power_by_square_size(x, y, size -1)
        if dop:
            print(p)
        for i in range(size):
            p += grid[x+size-1][y+i]
            if dop:
                print(p)
            p += grid[x+i][y+size-1]
            if dop:
                print(p)
        p -= grid[x+size-1][y+size-1]
        if dop:
            print(p)
    power_for_x_y_size[(x,y,size)] = p
    if x == sample_x and y == sample_y and size <= 20:
        print((x,y,size),p,"dict len {}".format(len(power_for_x_y_size.keys())))
    return p


def max_power_by_square_size():
    maxp = -float("inf")
    for x in range(300):
        for y in range(300):
            max_size = 300 - max(x,y)
            for size in range(1,max_size+1):
                for i in range(size):
                    p = power_by_square_size(x,y,size)
                if p > maxp:
                    power_by_x_y_size_power[p].append((x+1,y+1,size, p))
                    maxp = p
            #print(x+1,y+1,size,p)

            
    max_power = max(power_by_x_y_size_power.keys())
    return power_by_x_y_size_power[max_power]

print(max_power_by_square_size())

#Not 79,205,12

#print(power_by_square_size(sample_x, sample_y, 20))
