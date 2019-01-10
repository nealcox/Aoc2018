
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

def max_power_by_square_size(size):
    square = []
    for x in range(301-size):
        row = []
        for y in range(301-size):
            p = 0
            for i in range(size):
                for j in range(size):
                    p+= grid[x+i][y+j]
            row.append(p)
        square.append(row)

    max_power = -100
    x_max_power = 0
    y_max_power = 0

    for x in range(301-size):
        for y in range(301-size):
            if square[x][y] > max_power:
                max_power = square[x][y]
                x_max_power = x
                y_max_power = y
    return (x_max_power + 1, y_max_power + 1, max_power)

#print(max_power_by_square_size(3))
max_power = -100
x_max_power = 0
y_max_power = 0
for size in range(1,301):
    print(f"size: {size}")
    x, y, power = max_power_by_square_size(size)
    if power > max_power:
        max_power = power
        x_max_power = x
        y_max_power = y
        print (x_max_power + 1, y_max_power + 1, size, max_power)

