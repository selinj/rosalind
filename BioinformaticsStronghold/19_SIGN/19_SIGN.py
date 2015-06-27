import itertools
import math

with open('rosalind_sign.txt','r') as handle:
    n = int(handle.readline())

nset = []
perms = []

for i in range(-n,n+1):
    if i == 0:
        continue
    else:
        nset.append(i)

for p in itertools.permutations(nset,n):
    perms.append(p)

#remove all permutations containing opposite numbers (eg (1,-2, 2)
count = 0
newperms = []
pop = False

for p in perms:
    pop = False
    for i in range(0,n-1):
        if -p[i] in p:
            pop = True
            break
    if not pop:
        newperms.append(p)
    count +=1

printformat = ''
for i in range(0,n):
    if i<n:
        printformat+='{} '
    elif i==n:
        printformat +='{}'

out = open('19_SIGNout.txt','w')
out.write(str(len(newperms))+'\n')
for p in newperms:
    out.write(str(printformat.format(*p)+'\n'))
out.close()

