'''
a DNA string is a reverse palindrome if it is equal
to its reverse complement

given a DNA string in fasta
return position and length of every reverse palindrome in the string
 w/ 4 <= length <= 12, in any order
'''

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna

handle = open('rosalind_revp.txt','rU')
data = SeqIO.parse(handle,'fasta').next()
handle.close()

dna = data.seq
rev_comp = dna.reverse_complement()
revd = rev_comp[::-1]

def check(i,n):
    fwd, opp = dna[i:i+n], revd[i:i+n]
    opp = opp[::-1]
    return fwd == opp

length = len(str(dna))
print length
out = open('26_REVPout.txt','w')

for n in range(4,13):
    for i in range(length-n+1):
        if check(i,n):
            if len(str(dna[i:i+n])) >= n:
                print str(i+1) + ' ' + str(n) #print i + 1 because rosalind uses 1-based numbering
                out.write(str(i+1) + ' ' + str(n)+'\n')
out.close()
