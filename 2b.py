from collections import defaultdict

def check(pos, boxIDs):
    common = defaultdict(int)
    for boxID in boxIDs:
        common_letters = boxID[:pos] + boxID[pos+1:]
        common[common_letters] += 1

    for key, value in common.items():
        if value > 1:
            print("position:{}, key: {}, value {}".format(pos, key, value))
            return True
    #print("pos: {}, common: {}".format(pos, common))
    return False


INPUT = "2a-input.txt"
boxIDs = []


with open(INPUT, 'r') as infile:
    for boxID in infile:
        boxIDs.append(boxID)

IDlen = len(boxIDs[0])
found = False

for pos in range(IDlen):
    found = check(pos, boxIDs)
    if found:
        break
