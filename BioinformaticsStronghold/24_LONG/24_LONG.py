
import math
import itertools
from Bio import SeqIO

handle = open('rosalind_long.txt','r')
given = list(SeqIO.parse(handle,'fasta'))
handle.close()

##pairs = []
##for p in itertools.permutations(given,2):
##    pairs.append(p)
##
##with open('21_GRPHout.txt','w') as out:       
##    for p in pairs:
##        if (p[0].seq)[len(p[0])-k:len(p[0])] == (p[1].seq)[0:k]:
##            out.write(str(p[0].id)+" "+str(p[1].id)+'\n')
##    out.close()
##

