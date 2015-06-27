import itertools
import math

n = 2
nset = []

for i in range(1,n+1):
    nset.append(i)

print nset

perms = []

for p in itertools.permutations(nset,n):
    perms.append(p)

print perms
