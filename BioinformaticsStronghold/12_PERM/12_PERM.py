'''

Synteny block = similar DNA interval across pecies
Not strictly identical, but considered equivalent
We assign each block an integer
Then for a given genome, can determine the order of synteny blocks

Permutation of length n = ordering of positive integers

'''

import itertools
import math

n=0

given = open('rosalind_perm.txt','r')
n = int(given.readline())

nset = []
perms = []

#create a list
for i in range(1,n+1):
    nset.append(i)

print nset

for p in itertools.permutations(nset):
    perms.append(p)

#generalizing a format
printformat = ''
for i in range(0,n):
    if i<n:
        printformat += '{} '
    elif i==n:
        printformat += '{}'

out = open('12_PERMout.txt','w')
out.write(str(math.factorial(n))+'\n')


for p in perms:
    out.write(str(printformat.format(*p))+'\n')

out.close()
