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
import os
#import time

#f1 = open('rosalind_pper.txt','r')
#n,k = f1.readline().split()
#n,k=int(n),int(k)

n=86
k=9
#print n
#print k

count = 0
nset = [i for i in range(1,n+1)]
perms = sum(((count+1)) for p in itertools.permutations(nset,k)) % 1000000
print perms

#out = open('28_PPERout.txt','w')
#out.write(str(count))
#out.close()

os.system('say "your program has finished"')
