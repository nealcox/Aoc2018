from collections import defaultdict
from collections import namedtuple

INPUT = "8-input.test"
INPUT = "8-input.txt"

Header = namedtuple('Header',['num_children', 'num_metadata'])

class node:
    def __init__(self, header, children, metadata):
        self.header = header
        self.children = children
        self.metadata = metadata
#
#    def __str__(self):
#        me =  f"\nHeader: {self.header}\tMetadata: {self.metadata}\nChildren:\n {self.children}\nLength: {self.length()}\n"
#        for child in self.children:
#            me += str(child)
#        return me
#
    def length(self):
        length = 2 # header
        length += self.header.num_metadata # metadata
        for child in self.children:
            length += child.length()
        return length

    def complete_metadata_sum(self):
        #print(self)
        metadata_sum = sum(self.metadata)
        if self.header.num_children >0:
            for child in self.children:
                metadata_sum += child.complete_metadata_sum()
        return metadata_sum

    def value(self):
        if self.header.num_children  == 0:
            return sum(self.metadata)
        else:
            value = 0
            for datum in self.metadata:
                if datum > 0 and datum <= self.header.num_children:
                    value += self.children[datum -1].value()
            return value

with open(INPUT, 'r') as infile:
    text = infile.read().replace('\n', '')
    tree_definition = [int(n) for n in  text.split(' ')]


def analyse_tree(tree_definition):
#    print(f"analysing {tree_definition}")
    header = Header(tree_definition[0], tree_definition[1])
    if header.num_children == 0:
        children = []
        metadata = tree_definition[2:2+header.num_metadata]
#    elif num_children == 1:
#        child_node = analyse_tree(tree_definition[2:-header.num_metadata])
#        children = list(child_node)
#        metadata = tree_definition[-header.num_metadata:]
    else:
        find_children_in = tree_definition[2:]
        children = []
        length_of_children = 0
        while len(children) < header.num_children:
            child = analyse_tree(find_children_in)
            children.append(child)
            find_children_in = find_children_in[child.length():]
            length_of_children += child.length()
        metadata = tree_definition[2 + length_of_children :2 + length_of_children + header.num_metadata]
    return node(header, children, metadata)

root = analyse_tree(tree_definition)
#print(root)
print(root.value())
