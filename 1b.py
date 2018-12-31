INPUT = "1a-input.txt"

current_frequency = 0
seen = []
first_double = None

def loopinput():
    global current_frequency, seen
    with open(INPUT, 'r') as infile:
        for line in infile:
            change = int(line)
            current_frequency += change
            print(change, current_frequency)
            if current_frequency in seen:
                return current_frequency
            seen.append(current_frequency)
        return None

while first_double == None:
    first_double = loopinput()

