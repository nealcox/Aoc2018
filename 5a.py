#INPUT = "5-input.test"
INPUT = "5-input.txt"

polymer = []
with open(INPUT, 'r') as infile:
    for line in infile:
        for character in line:
            polymer.append(ord(character))
    del polymer[-1]

search_from = 0
change_made = True

while change_made:
    change_made = False
    polymer_length = len(polymer)
    #print(''.join(chr (c) for c in polymer))
    while search_from < polymer_length - 1:
        if abs(polymer[search_from] - polymer[search_from + 1]) == 32:
            del polymer[search_from:search_from + 2]
            change_made = True
            if search_from > 0:
                search_from -= 1
            break
        else:
            search_from += 1

print(''.join(chr (c) for c in polymer))
print(len(polymer))




