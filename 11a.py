
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

grid_serial_number = 8868
grid = []
for x in range(300):
    row = []
    for y in range(300):
        row.append(power_level(x+1, y+1, grid_serial_number))
    grid.append(row)

square = []
for x in range(298):
    row = []
    for y in range(298):
        p = 0
        for i in range(3):
            for j in range(3):
                p+= grid[x+i][y+j]
        row.append(p)
    square.append(row)

max_power = -100
x_max_power = 0
y_max_power = 0

for x in range(298):
    for y in range(298):
        if square[x][y] > max_power:
            max_power = square[x][y]
            x_max_power = x
            y_max_power = y
            print(x_max_power + 1, y_max_power + 1, max_power)

