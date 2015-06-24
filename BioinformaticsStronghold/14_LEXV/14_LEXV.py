'''

we organize genetic strings lexographically


given a collection of <= 10 symbols defining an ordered alphabet, and int n
return all strings of length n, ordered lexographically

'''

import itertools

#given = open('rosalind_lexv.txt','r')
#alphraw = str(given.readline().rstrip())
#alphabet = alphraw.split(' ')
#n = int(given.readline())

alphabet = ['D','N','A']
n=3

perms = []
count = 0

for i in range(n+1):
    print i
    for p in itertools.product(alphabet,repeat=i):
        perms.append(p)
        count +=1

print perms
print count

##for i in perms:
##    for nt in i:
##        
def swap(a,b):
    temp = ""
    temp = a
    a = b
    b = temp


#generalizing a format
#printformat1 = '{}'

#out = open('14_LEXVout.txt','w')

#for p in perms:
#    if len(p)<n:
        #perms[p].append(
    #out.write(str(printformat.format(*p))+'\n')
#        print printformat.format(*p)+'\n'

#out.close()
