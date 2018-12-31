from collections import defaultdict

INPUT = "2a-input.txt"

twos_and_threes = defaultdict(int)

def do_boxID_freqs(boxID):
    global twos_and_threes
    frequency = defaultdict(int)
    for letter in boxID:
        frequency[letter] += 1

    if 2 in frequency.values():
        twos_and_threes['2'] += 1

    if 3 in frequency.values():
        twos_and_threes['3'] += 1


with open(INPUT, 'r') as infile:
    for boxID in infile:
        do_boxID_freqs(boxID)

print("Twos: {}, Threes: {}, checksum: {}".format(twos_and_threes['2'],
       twos_and_threes['3'], twos_and_threes['2'] * twos_and_threes['3']))
