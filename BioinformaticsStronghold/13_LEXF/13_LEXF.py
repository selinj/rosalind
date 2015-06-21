'''

we organize genetic strings lexographically


given a collection of <= 10 symbols defining an ordered alphabet, and int n
return all strings of length n, ordered lexographically

'''

import itertools

given = open('rosalind_lexf.txt','r')
alphraw = str(given.readline().rstrip())
alphabet = alphraw.split(' ')
n = int(given.readline())
perms = []

for p in itertools.produßct(alphabet,repeat=n):
    perms.append(p)

#generalizing a format
printformat = ''
for i in range(0,n):
    printformat += '{}'

out = open('13_LEXFout.txt','w')

for p in perms:
    out.write(str(printformat.format(*p))+'\n')

out.close()
