'''

given string s
return every candidate protein string that can be translated from ORFs of S

'''

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna
from Bio.Alphabet import generic_rna
import pickle
import os

#handle = open('rosalind_orf.txt','rU')
#given = list(SeqIO.parse(handle,'fasta'))
#handle.close()

#s = str(given[0].seq)

#coding_dna = Seq(s,generic_dna)

##coding_dna = Seq('AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG',generic_dna)
###print coding_dna
##mRNA = coding_dna.transcribe()
##translated = mRNA.translate()
##print mRNA
##print translated
###mRNA2 = Seq('AUGGCCAUUGUAAUGGGCCGCUGAAAGGGUGCCCGAUAG',generic_rna)
###print mRNA2.translate()
##
##protein = ""
##for aa in translated:
##    if aa != '*':
##        protein += aa
##    elif aa == '*':
##        print protein
##        protein = ''
##
##rev = coding_dna.reverse_complement()
##mRNA2 = rev.transcribe()
##translated2 = mRNA2.translate()
##print mRNA
##print translated2
##protein2 = ""
##for aa in translated:
##    if aa != '*':
##        protein += aa
##    elif aa == '*':
##        print protein
##        protein = ''

#DNA to mRNA
def i_transcribe(dna):
    #str(s)
    mrna = dna.replace('T','U')
    return mrna

table = pickle.load(
    open(os.path.expanduser(
        '~/Documents/CS/CS_Bio_self/rosalind/resources/RNAcodontable.txt')))

#RNA to polypeptide
def i_translate(mRNA):
    length = 0
    p = ""

    if len(mRNA) % 3 != 0:
        if len(mRNA)% 3 == 1:
            length = len(mRNA) -1
        if len(mRNA)% 3 == 2:
            length = len(mRNA) -2
    else:
        length = len(mRNA)
        
    for i in range(0,length,3):
        aa = table[mRNA[i:i+3]]
        codon = mRNA[i:i+3]
        if aa != 'Stop':
            p += aa
        elif aa == 'Stop':
            break
    return p

#reverse complement
def rev_comp(dna):
    slist = []

    for nt in dna:
        if nt == 'A':
            slist.append('T')
        if nt == 'T':
            slist.append('A')
        if nt == 'C':
            slist.append('G')
        if nt =='G':
            slist.append('C')

    comp = ''.join(slist)
    revcomp = comp[::-1]
    return revcomp

s = 'AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG'
m = i_transcribe(s)
print m
p = i_translate(m)
print p

s2 = rev_comp(s)
m2 = i_transcribe(s2)
print m2
p2 = i_translate(m2)
print p2

