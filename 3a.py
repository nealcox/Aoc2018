from collections import defaultdict
import re


INPUT = "3-input.txt"
cloth = defaultdict(int)

def place(claims):
    global cloth
    for claim in claims:
        left = int(claim[2])
        top = int(claim[3])
        width = int(claim[4])
        depth = int(claim[5])
        for i in range(width):
            for j in range(depth):
                cloth[(left+i, top + j)] += 1
    
        

claims = []


with open(INPUT, 'r') as infile:
    for claim in infile:

        this_claim = re.split('#| @|,|:|x|\n',claim)
        claims.append(this_claim)

place(claims)

multiple_claims = 0
for key, value in cloth.items():
    if value > 1:
        multiple_claims += 1

print("Multiply claimed squares: {}".format(multiple_claims))

