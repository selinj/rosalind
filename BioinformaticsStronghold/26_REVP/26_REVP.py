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
#revc = data.seq.reverse_complement()
#revd = revc[::-1]

#dna = Seq('TCAATGCATGCGGGTCTATATGCAT')
#revc = dna.reverse_complement()
#print dna
#print revc
#print revc[::-1]
#revd = revc[::-1]
#print revd

#check every substring of length between 4 and 12, if it equals its reverse complement
def check_p(seq,start,n):
    #s is the start index, n is the length
    forward = seq[start:start+n]
    revc = seq.reverse_complement()
    revd = revc[::-1]
    candidate = revd[start:start+n]
    candidate = revd[::-1]
    print forward
    print candidate
    return forward == candidate

out = open('26_REVPout.txt','w')

for n in range(4,12):
    print n
    for i in range(len(dna)):
        if check_p(dna,i,n):
            print str(i) + ' ' + str(n)
            #print str(dna[i:i+n])
            #print str(revc[(i+n-1):(i-1):-1])
            #out.write(str(i+1) + ' ' + str(n)+'\n')
            #out.write(str(dna[i:i+n])+'\n')
            #out.write(str(revc[i+n-1:i-1:-1])+'\n\n')

out.close()
