'''

Point mutations in DNA:
    *transition = purine sub (A <-> G) or pyrimidine sub (C <-> T)
    *transversion = purine <-> pyrimidine

Transversions less common than transition
Across genome, transitions:transversions = ~2

Given 2 DNA strings s1 and s2 of same length, find transition/transversion ratio
R(s1, s2)

'''

from Bio import SeqIO

handle = open('rosalind_tran.txt','rU')
given = list(SeqIO.parse(handle,'fasta'))
handle.close()

s1 = str(given[0].seq)
s2 = str(given[1].seq)

transitions = 0.0
transversions = 0.0

purines = ['A','G']
pyrimidines = ['C','T']

for i in range(len(s1)):
    if s1[i] != s2[i]:
        if s1[i] in purines:
            if s2[i] in purines:
                transitions += 1
            else:
                transversions +=1
        elif s1[i] in pyrimidines:
            if s2[i] in pyrimidines:
                transitions += 1
            else:
                transversions +=1
        
R=transitions/transversions

with open('11_TRANout.txt','w') as f:
    f.write(str(R))
    f.close()
