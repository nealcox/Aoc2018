INPUT = "1a-input.txt"

current_frequency = 0

with open(INPUT, 'r') as infile:
    for line in infile:
        change = int(line)
        current_frequency += change
        print(change, current_frequency)

