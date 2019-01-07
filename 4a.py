from collections import defaultdict
import re


#INPUT = "4-input.test"
INPUT = "4-input.txt"
total_hours_by_guard = defaultdict(int)
most_common_asleep = defaultdict(int)
    
        
shifts = []
events = []
def process_shift(shift_start, shift_end):
    guard_num = events[shift_start][4]
    #print(guard_num)
    awake = True
    state_start = 1
    event_num = shift_start + 1
    shift = ''
    while event_num < shift_end:
        state_end = int(events[event_num][2])
        if awake:
            state = '.' * (state_end - state_start + 1)
        else:
            state = '#' * (state_end - state_start + 1)
        shift = shift + state
        awake = not(awake)
        #print(awake, state_start, state_end)
        state_start = state_end + 1
        event_num += 1
    if awake:
        shift = shift + '.' * (61 - state_start)
    else:
        shift = shift + '#' * (61 - state_start)
    shifts.append((guard_num, shift))


with open(INPUT, 'r') as infile:
    for event in infile:

        this_event = re.split('\[|\] | #| begins shift|:|\n',event)
        events.append(this_event)

#for event in events:
    #print(event)

num_events = len(events)

shift_end = num_events
shift_start = num_events - 1

while shift_start > 0:
    while events[shift_start][3] != 'Guard':
        shift_start -= 1
    process_shift(shift_start, shift_end)
    shift_end = shift_start
    shift_start -= 1
for shift in shifts:
    print(shift)
    guard_num = shift[0]
    total_hours_by_guard[guard_num] += shift[1].count('#')

max_hours = max(total_hours_by_guard.values())
print("max hours: {}".format(max_hours))

for guard_num , hours in total_hours_by_guard.items():
    if hours == max_hours:
        sleepiest_guard_num = guard_num
        print (sleepiest_guard_num, hours)

for shift in shifts:
    guard_num = shift[0]
    if guard_num == sleepiest_guard_num:
        print(shift)
        minute_state = list(shift[1])
        for minute, state in enumerate(minute_state):
            if state == '#':
                most_common_asleep[minute] += 1
            elif state != '.':
                print("WTF: {}".format(state))

most_common_asleep_how_common = max(most_common_asleep.values())

for minute , how_common in most_common_asleep.items():
    if how_common == most_common_asleep_how_common:
        sleepiest_minute = minute
        print (sleepiest_guard_num, sleepiest_minute)

#
#    multiple_claims = defaultdict(int)
#    for key, value in cloth.items():
#        if len(value) > 1:
#            for claim_no in value:
#                multiple_claims[claim_no] += 1
#    for claim in claims:
#        claim_no = int(claim[1])
#        if multiple_claims[claim_no] < 1:
#            print(claim_no)
