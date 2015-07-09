#proof of concept
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna

dna = Seq('TCAATGCATGCGGGTCTATATGCAT')
print "                   0123456789012345678901234"
print "                   1234567890123456789012345"
print "dna seq         5' " + dna + " 3'"
rev_comp = dna.reverse_complement()
print "rev comp        5' " + rev_comp + " 3'"
revd = rev_comp[::-1]
print "reversed r.c.   3' " + revd +  " 5'"
