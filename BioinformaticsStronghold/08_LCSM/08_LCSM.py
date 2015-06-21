
'''
given collection of k DNA strings in FASTA format
return longest common substring - multiple, if that's the case

'''

#SeqRecord object in Biopython holds sequence w/ identifiers

from Bio import SeqIO

handle = open('rosalind_lcsm.txt','rU')
records = list(SeqIO.parse(handle, 'fasta'))
handle.close()

#print records[0].id
#print records[0].seq

