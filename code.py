from operator import mul
from functools import reduce

def beadOrnaments(b):
    return int((reduce(mul, map(lambda x: x ** (x - 1), b), 1) * (sum(b) ** (len(b) - 2))) % (7 + 10 ** 9))

'''
All beads are distinct, even if they have the same color. Two ornaments are considered different if two beads are joined by a thread in one configuration, but not in the other.
How many different ornaments can be formed using this algorithm? Return the answer modulo 10 to power 9 plus 7
'''
