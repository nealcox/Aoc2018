from collections import defaultdict
import re


INPUT = "3-input.txt"
cloth = defaultdict(set)

def place(claims):
    global cloth
    for claim in claims:
        claim_no = int(claim[1])
        left = int(claim[2])
        top = int(claim[3])
        width = int(claim[4])
        depth = int(claim[5])
        for i in range(width):
            for j in range(depth):
                cloth[(left+i, top + j)].add(claim_no)
    
        

claims = []


with open(INPUT, 'r') as infile:
    for claim in infile:

        this_claim = re.split('#| @|,|:|x|\n',claim)
        claims.append(this_claim)

place(claims)

multiple_claims = defaultdict(int)
for key, value in cloth.items():
    if len(value) > 1:
        for claim_no in value:
            multiple_claims[claim_no] += 1
for claim in claims:
    claim_no = int(claim[1])
    if multiple_claims[claim_no] < 1:
        print(claim_no)
