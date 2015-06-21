'''

Given file w/ FASTA formats of seqs
seq 1: string s
seq 2 onwards: collection of substrings acting as introns

Transcribe: splice out the introns, concatenate the exons into RNA

return/Translate: protein string resulting from translating the RNA string
    (= the exons of s)

'''

from Bio import SeqIO
import pickle
import os

handle = open('rosalind_splc.txt','rU')
given = list(SeqIO.parse(handle,'fasta'))
handle.close()

s = str(given[0].seq)

#function to splice
def splice(intron, s):
    index = 0
    length = len(intron)
    while s.find(intron) != -1:
        index = s.find(intron)
        s = s[0:index] + s[index+length:]

    return s
    
#splice introns, concatenate exons
for record in given:
    if record == given[0]:
        continue
    else:
        i = str(record.seq)
        s = splice(i,s)

#transcribe: DNA > RNA > mRNA
s = s.replace('T','U')
#print s

#translate
table = pickle.load(
    open(os.path.expanduser(
        '~/Documents/CS/CS_Bio_self/rosalind/resources/RNAcodontable.txt')))

output = open('10_SPLCout.txt','w')

length = 0

#correct length of s
if len(s) % 3 != 0:
    if len(s)% 3 == 1:
        length = len(s) -1
    if len(s)% 3 == 2:
        length = len(s) -2
else:
    length = len(s)
    
#sub codon for aa and write to file
for nt in range(0,length,3):
    aa = table[s[nt:nt+3]]
    codon = s[nt:nt+3]
    if aa != 'Stop':
        output.write(aa)
    elif aa == 'Stop':
        break

output.close()
    
