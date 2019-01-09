from collections import defaultdict

INPUT = "7-input.test"
INPUT = "7-input.txt"

all_steps = set()
order = []
requirements = defaultdict(list)

with open(INPUT, 'r') as infile:
    for line in infile:
        before = line[5]
        after = line[36]
        all_steps.add(before)
        all_steps.add(after)

        requirements[after].append(before)
        print(before, after)

remaining_steps = sorted(list(all_steps))
#print(remaining_steps)
#print(requirements)

def get_depended_on():
    depended_on = set()
    for step_list in requirements.values():
        for step in step_list:
            depended_on.add(step)
    return depended_on

while remaining_steps:
    for step in remaining_steps:
        if step not in requirements.keys():
            order.append(step)
            remaining_steps.remove(step)
            to_delete = set()
            for key, required_list in requirements.items():
                if step in required_list:
                    required_list.remove(step)
                if not required_list:
                    to_delete.add(key)
            for key in to_delete:
                del requirements[key]
            break
    #print(remaining_steps)
    #print(requirements)

    print (''.join(order))




