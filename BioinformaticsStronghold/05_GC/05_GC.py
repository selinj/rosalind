'''

Quick method for language determination: analyze letter frequency
    *unique for diff languages
We can distinguish between species based on GC-content (ie. percentage
    of bases that are either C or G

Given <= 10 strings in FASTA format
Return ID w/ hightest GC content and then that string's GC content
'''

from Bio import SeqIO

handle = open('rosalind_gc.txt','rU')
dataset = list(SeqIO.parse(handle,'fasta'))
handle.close()

highestGC = 0.0
highestID = ""

for record in dataset:
    GCcount = 0.0
    s = str(record.seq)
    for base in s:
        if base in ['G','C']:
            GCcount +=1
    GCcontent = GCcount/len(s)*100
    #print GCcontent
    #print record.id
    if GCcontent > highestGC:
        highestGC = GCcontent
        highestID = record.id
 
#print highestID
#print highestGC

with open('05_GCout.txt','w') as out:
    out.write(str(highestID)+'\n')
    out.write(str(highestGC))
    out.close()
