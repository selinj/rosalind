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

handle = open('rosalind_grph.txt','r')
given = list(SeqIO.parse(handle,'fasta'))
handle.close()
k=3

pairs = []
for p in itertools.permutations(given,2):
    pairs.append(p)

with open('21_GRPHout.txt','w') as out:       
    for p in pairs:
        if (p[0].seq)[len(p[0])-k:len(p[0])] == (p[1].seq)[0:k]:
            out.write(str(p[0].id)+" "+str(p[1].id)+'\n')
    out.close()
