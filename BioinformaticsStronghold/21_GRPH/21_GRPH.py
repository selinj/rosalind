'''

If given a grap w/ labelled nodes,
can be represented by adjacency list
    -each row of list contains 2 node labels = unique edge


digraph = graph containing directed edges w/ orientation
    -represented by arrow (start node ----> end node)
    -represented by (start, end)

directed loop = edge of the form (start, start)

for collection of strings, and int > 0, k
overlap graph for strings = Ok
each string represented by node
strin s connected to string t w/ directed edge when s suffix length k
    matches t prefix length k (ie. overlap at end of first string
    and beginning of second of length k)
    **as long as s is not t

given: collection of DNA strings
return: adjacency list corresponding to Ok, in any order
'''

import math
import itertools
from Bio import SeqIO

#handle = open('rosalind_grph.txt','r')
#given = SeqIO.parse(handle,'fasta')
#handle.close()

strings = ['AAATAAA','AAATTTT','TTTTCCC','AAATCCC','GGGTGGG']
k=3

pairs = []
for p in itertools.permutations(strings,2):
    pairs.append(p)

print pairs

for p in pairs:
    if p[0][len(p[0])-k:len(p[0])] == p[1][0:k]:
        print "overlap: "+str(p[0])+", "+str(p[1])

'''
for every permutation of length 2:
    if substring perm[0] at (len(perm[0]-k,len(perm[0]) == same for perm[1] at (0,k)
                                 then return both ids
                                 else check next
'''
    
