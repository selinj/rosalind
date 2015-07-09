
'''using the first example in the problem, the protein with
uniprot id B5ZC00'''

import urllib2

#proteinseqs='MKNKFKTQEELVNHLKTVGFVFANSEIYNGLANAWDYGPLGVLLKNNLKNLWWKEFVTKQKDVVGLDSAIILNPLVWKASGHLDNFSDPLIDCKNCKARYRADKLIESFDENIHIAENSSNEEFAKVLNDYEISCPTCKQFNWTEIRHFNLMFKTYQGVIEDAKNVVYLRPETAQGIFVNFKNVQRSMRLHLPFGIAQIGKSFRNEITPGNFIFRTREFEQMEIEFFLKEESAYDIFDKYLNQIENWLVSACGLSLNNLRKHEHPKEELSHYSKKTIDFEYNFLHGFSELYGIAYRTNYDLSVHMNLSKKDLTYFDEQTKEKYVPHVIEPSVGVERLLYAILTEATFIEKLENDDERILMDLKYDLAPYKIAVMPLVNKLKDKAEEIYGKILDLNISATFDNSGSIGKRYRRQDAIGTIYCLTIDFDSLDDQQDPSFTIRERNSMAQKRIKLSELPLYLNQKAHEDFQRQCQK',

f1 = open('rosalind_mprt.txt','r')

#make array of id's
protList = []
protList = [line.rstrip('\n') for line in f1]

print "The list of IDs from Rosalind:"
print protList

def getUniprotFile(protID):
    output = urllib2.urlopen(("http://www.uniprot.org/uniprot/%s.fasta" % protID))
    return output

#print getUniprotFile('P10493')

protDict = {}
for protID in protList:
    output = getUniprotFile(protID)
    output.readline()
    seq = output.readline()
    protDict.update({protID:seq})
        
#prompt user w/ id, get seq input to make a dictionary with the UniProt id's + seqs
##protDict = {}
##for prot in protList:
##    print prot
##    seq = raw_input()
##    seq = seq.replace(' ','')
##    protDict.update({prot:seq})

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
            #go on
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
    out.write(uniprotid+'\n')
    for i in s_list:
        out.write(str(i))
    out.write('\n')

out.close()
