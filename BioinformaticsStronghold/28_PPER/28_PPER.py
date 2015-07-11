'''

modifying the notion of permutation in order to include
the concept of partial gene orderings

pper = ordering of only k objects taken from a collection of n

eg set: 1,2,3,4,5,6,7,8
a pperm: 5,7,2

P(n,k) = total number of partial permutations of k objects from colleciton
of n objects

P(n,n) is simply the number of permutations of n objects

given n, k
return P(n,k) % 1 000 000


'''
import itertools
import math
from math import factorial
import os
#import time

#f1 = open('rosalind_pper.txt','r')
#n,k = f1.readline().split()
#n,k=int(n),int(k)

n=81
k=8
print n
print k

count = 0
nset = [i for i in range(1,n+1)]

#this works, but is too slow for Rosalind's 5-min answer windo
#perms = sum(((count+1)) for p in itertools.permutations(nset,k)) % 1000000

'''
number of k permutations for n set
= P(n,k) = n!/(n-k)!

In factorial = n(n-1)(n-2)...(n-k-1)
= 21,20,19...*13
13,14,15...19,20,21
'''

result = 1
for i in xrange(n-k-1,n+1):
    print i
    result *= i%1000000
print result




#print factorial(5)
first = factorial(n)
second = factorial(n-k)

print (factorial(n)/factorial(n-k))%1000000

#out = open('28_PPERout.txt','w')
#out.write(str(count))
#out.close()

#os.system('say "done!"')
