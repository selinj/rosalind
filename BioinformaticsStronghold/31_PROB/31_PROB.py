'''

-quantify likelihood of finding a given motif randomly
-need a critical motif length at which we can discard chance and
conclude that the motif is conserved/present for a biological reason
-calculate probability of a given motif occurring randomly at a
fixed location in the genome
-for GC content (%) x, then symbol frequency of G or C = x/2
-symbol frequency of A/T = (1-x)/2
-small probabilities therefore "magnify" with log10(x) --> raise
10 to an exponent to obtain x

-given DNA string s length <= 100bp and array A w <= 20 numbers
between 0 and 1
-return array B w length = length(A), where B[k] represents the
common log of the probability that a random string w/ GC content
found in A[k] will match s exactly

'''

import math

handle = open('rosalind_prob.txt','rU')
s = handle.readline()
A = handle.readline().strip('\n')
A = A.split(' ')
A = [float(i) for i in A]

def find_probs(GCcont):
    pg = (GCcont/2)
    pa = (1-GCcont)/2
    return pg, pa

def calculate_probs(pGC,pAT):
    probability = 1
    for nt in s:
        if nt == 'A' or nt == 'T':
            probability *= pAT
        elif nt == 'G' or nt == 'C':
            probability *= pGC
    logprob = math.log10(probability)
    return logprob

B = []

for val in A:
    pGC,pAT = find_probs(val)
    B.append(calculate_probs(pGC,pAT))

print B

out = open('31_PROBout.txt','w')

for val in B:
    out.write(str(val) + ' ')
out.close()
    
