from collections import defaultdict
from collections import namedtuple

INPUT = "7-input.test"
INPUT = "7-input.txt"
base_time = 0
base_time = 60
num_workers = 2
num_workers = 5

Worker = namedtuple('Worker',['step', 'remaining_time'])
workers = []
for _ in range(num_workers):
    workers.append(Worker('.',0))

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


def get_step(remaining_steps):
    for step in remaining_steps:
        if step not in requirements.keys():
            return step
    return None

second = 0
finished = False
while not finished:
    for i, worker  in enumerate(workers):
        if worker.remaining_time == 0:
            if worker.step is not None:
                to_delete = set()
                for key, required_list in requirements.items():
                    if worker.step in required_list:
                        required_list.remove(str(worker.step))
                    if not required_list:
                        to_delete.add(key)
                for key in to_delete:
                    del requirements[key]

            step = get_step(remaining_steps)
            if step == None:
                remaining_time = 0
            else:
                remaining_steps.remove(step)
                remaining_time = ord(step) + base_time - ord('A')
            workers[i] = Worker(step, remaining_time)
        else:
            workers[i] = Worker(worker.step, worker.remaining_time - 1)

                

    print(f"\n{second}", end="\t")        
    for worker in workers:
        print(worker, end="\t")        

    second += 1
    all_workers_idle = True
    for worker in workers:
        if worker.step != None:
            all_workers_idle = False

    if not remaining_steps and all_workers_idle:
        finished = True


#while remaining_steps:
#    for step in remaining_steps:
#        if step not in requirements.keys():
#            order.append(step)
#            remaining_steps.remove(step)
#            to_delete = set()
#            for key, required_list in requirements.items():
#                if step in required_list:
#                    required_list.remove(step)
#                if not required_list:
#                    to_delete.add(key)
#            for key in to_delete:
#                del requirements[key]
#            break
    #print(remaining_steps)
    #print(requirements)

#print (''.join(order))
