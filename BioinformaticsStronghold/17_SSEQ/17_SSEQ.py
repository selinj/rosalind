#given 2 dna strings s and t
#return collection of indices of s in which symbols of t appear in order

from Bio import SeqIO

handle = open('rosalind_sseq.txt','rU')
given = list(SeqIO.parse(handle,'fasta'))
handle.close()

s = str(given[0].seq)
t = str(given[1].seq)

indexes = []
n=0

for i in range(len(t)):
    index = s.find(t[i],n+1,len(s))
    n = index
    indexes.append(str(index+1))
    
with open('17_SSEQout.txt','w') as out:
    out.write(' '.join(indexes))
    out.close()
