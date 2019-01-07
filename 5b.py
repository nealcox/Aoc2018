#INPUT = "5-input.test"
INPUT = "5-input.txt"

polymer = []
with open(INPUT, 'r') as infile:
    for line in infile:
        for character in line:
            polymer.append(ord(character))
    del polymer[-1]

def len_reduced_polymer(polymer):
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

    #print(''.join(chr (c) for c in polymer))
    return(len(polymer))

def improve_reduce(char, polymer):
    ord_lower = ord(char.lower())
    ord_upper = ord(char.upper())

    improved_polymer = []
    for i in polymer:
        if (i != ord_lower  and i != ord_upper):
            improved_polymer.append(i)

    #print(char, ''.join(chr (c) for c in improved_polymer))
    length = len_reduced_polymer(improved_polymer)
    return length


#print(len_reduced_polymer(polymer))

chars = set(chr(s).lower() for s in polymer)
shortest = len(polymer) +1
best_letter = ""

for char in chars:
    l = improve_reduce(char, polymer)
    #print(char, l)
    if l < shortest:
        shortest = l
        best_letter = char
     #   print("new best!")
    #else:
     #   print("X")


print(best_letter, shortest)
        
        


