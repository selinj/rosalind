
'''
given collection of k DNA strings in FASTA format
return longest common substring - multiple, if that's the case

'''

#SeqRecord object in Biopython holds sequence w/ identifiers

from Bio import SeqIO
from Bio import AlignIO

handle = open('rosalind_lcsm.txt','rU')
given = list(SeqIO.parse(handle, 'fasta'))
handle.close()

s = given[0].seq

#s = 'ABCD'

print s

def generate_substrings(s):
    for i in xrange(1,len(s)+1):
        for j in xrange(len(s)-i+1):
            yield s[j:j+i]

def compare(a,b):
    result = 0
    if len(a) < len(b):
        result = 1 #not in decreasing order

def order(collection):
    for i in range(len(collection)-1):
        if compare(collection[i], collection[i+1]) == 1:
            collection[i],collection[i+1]=collection[i+1],collection[i]

subs = list(generate_substrings(s))
subs = list(reversed(subs))
#print subs

longestsub = ''
for sub in subs:
    for i in range(1,len(given)):
        instring = False
        if str(given[i].seq).find(sub)> 0:
            instring = True
        else:
            instring = False
        if instring:
            longestsub=sub
        else: break
        
print longestsub
