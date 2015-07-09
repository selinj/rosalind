
'''using the first example in the problem, the protein with
uniprot id B5ZC00'''

import urllib2
from Bio import SeqIO

f1 = open('rosalind_mprt.txt','r')

#make array of id's
protList = []
protList = [line.rstrip('\n') for line in f1]

print "The list of IDs from Rosalind:"
print protList

def getUniprotFile(protID):
    output = urllib2.urlopen(("http://www.uniprot.org/uniprot/%s.fasta" % protID))
    return output

protDict = {}
for protID in protList:
    try:
        output = getUniprotFile(protID)
        protrecord = list(SeqIO.parse(output,'fasta'))
        seq = (protrecord[0]).seq
        protDict.update({protID:seq})
    except:
        print "This didn't work."

print "The Dictionary of IDs/UniProt sequences:"
print protDict

#N-glycosylation motif: N{P}[ST]{P}
listofindexes = []
index = 0

def find_indexes(protID,seq):
    print "Now checking protein "+protID
    print "With sequence starting " +seq
    del listofindexes[:]
    for i in range(len(seq)-5):
        if seq[i] == 'N':
            index = i
            if seq[i+1] != 'P':
                if seq[i+2] == 'S' or seq[i+2] == 'T':
                    if seq[i+3] != 'P':
                        listofindexes.append(i+1)
    print "Found N-glycosylation motif at "
    print listofindexes
    return listofindexes

out = open('25_MPRTout.txt','w')
    
for uniprotid,seq in protDict.items():
    s_list = find_indexes(uniprotid,seq)
    if not s_list:
        continue
    out.write(uniprotid+'\n')
    for i in s_list:
        out.write(str(i)+' ')
    out.write('\n')

out.close()
