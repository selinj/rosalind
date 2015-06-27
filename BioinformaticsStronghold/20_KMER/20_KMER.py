'''

Given fixed int > 0, k
Order all possible k-mers taken from an underlying alphabet lexicographically

Then, k-mer composition of string s can be represed by
Array A, where A[m] is the # of times that the m-th k-mer
(lexicographically) appears in s

Return the 4-mer composition of s

'''

import math
import itertools
from Bio import SeqIO

handle = open('rosalind_kmer.txt','rU')
given = list(SeqIO.parse(handle,'fasta'))
handle.close()

s = given[0].seq

alphabet = ['A','C','G','T']
merset = []

for mer in itertools.product(alphabet,repeat=4):
    merset.append(mer)

print merset

newmerset = []
for mer in merset:
 newmerset.append(str(''.join(mer)))

A = []
def countmers(s,substring):
    count = index = 0
    while True:
        index = s.find(substring,index) +1
        if index >0:
            count+=1
        else:
            return count

for mer in newmerset:
    A.append(countmers(s,mer))

out = open('20_KMERout.txt','w')

for a in A:
    out.write(str(a)+' ')
out.close()
