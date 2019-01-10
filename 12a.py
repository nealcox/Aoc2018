test = False #True
NUM_GENERATIONS = 500#00000000
target_generations = 50000000000

if test:
    initial_state = "#..#.#..##......###...###"
    rules = { ".#.##":"#",
            "...##":"#",
            "..#..":"#",
            "#.#..":".",
            "...#.":".",
            ".#...":"#",
            ".....":".",
            "#....":".",
            "#...#":".",
            "###.#":"#",
            "..###":".",
            "###..":"#",
            "##.##":"#",
            "##.#.":"#",
            "..#.#":".",
            ".###.":".",
            ".#.#.":"#",
            ".##..":"#",
            ".####":"#",
            "##...":".",
            "#####":".",
            "..##.":".",
            "#.##.":".",
            ".#..#":".",
            "##..#":".",
            "#.#.#":"#",
            "#.###":"#",
            "....#":".",
            "#..#.":".",
            "#..##":".",
            "####.":"#",
            ".##.#":".",
            }

else:
    initial_state = "####..##.##..##..#..###..#....#.######..###########.#...#.##..####.###.#.###.###..#.####..#.#..##..#"

    rules = { ".#.##":".",
            "...##":"#",
            "..#..":".",
            "#.#..":".",
            "...#.":".",
            ".#...":"#",
            ".....":".",
            "#....":".",
            "#...#":"#",
            "###.#":".",
            "..###":"#",
            "###..":".",
            "##.##":".",
            "##.#.":"#",
            "..#.#":"#",
            ".###.":".",
            ".#.#.":".",
            ".##..":"#",
            ".####":".",
            "##...":".",
            "#####":".",
            "..##.":".",
            "#.##.":".",
            ".#..#":"#",
            "##..#":".",
            "#.#.#":"#",
            "#.###":".",
            "....#":".",
            "#..#.":"#",
            "#..##":".",
            "####.":"#",
            ".##.#":"#",
            }

tick = 0
old_score = 0
cycle_length = 0
max_left = 0
max_right = 0
plants = []
generations = []
for i,pot in enumerate(initial_state):
    if pot == '#':
        plants.append(i)
generations.append(sorted(plants))

while tick < NUM_GENERATIONS:
    tick = tick + 1
    
    if tick % 1000 == 0:
        print(tick)
    left = min(generations[tick-1]) - 5
    right = max(generations[tick-1]) + 5
    plants = []
    for pot in range (left, right):
        pots_state = ""
        for i in range(pot - 2, pot + 3):
            if i in generations[tick-1]:
                pots_state = pots_state + "#"
            else:
                pots_state = pots_state + "."
        next_state = rules[pots_state]
        if next_state == '#':
            plants.append(pot)
    if min(plants) < max_left:
        max_left = min(plants)
    if max(plants) > max_right:
        max_right = max(plants)
    this_generation = sorted(plants)
    if this_generation in generations:
        cycle_length = tick
        tick += (NUM_GENERATIONS // cycle_length) * cycle_length
        
        print(f"Cycle found, length {cycle_length}")
        print(f"0: {generations[0]}")
        print(f"{cycle_length}: {generations[{cycle_length}]}")

        print(f"Changing time from {cycle_length} to {tick}")
    score = sum(generations[-1])
    print(tick - 1, score, score - old_score)
    old_score = score
    generations.append(this_generation)

def print_puzzle():
    padding = "." * (3 - max_left)
    print(padding,'0')
    for i, generation in enumerate(generations):
        state = []
        for j in range(max_left,max_right+1):
            if j in generation:
                state.append('#')
            else:
                state.append('.')
        print(f"{i:3d}", ''.join(state))
if test:
    print_puzzle()
print(sum(generations[-1]))

print (88 * (target_generations - NUM_GENERATIONS + 1) + score)

