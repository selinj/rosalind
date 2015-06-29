from Bio import SeqIO

handle = open('rosalind_lcsm.txt','rU')
given = list(SeqIO.parse(handle,'fasta'))
handle.close()

def findsharedmotif(s1,s2):
    i = [[0] * (1+len(s2)) for j in xrange(1+len(s1))]
    longest, x_longest = 0, 0
    for x in xrange(1, 1 + len(s1)):
        for y in xrange(1, 1+ len(s2)):
            if s1[x-1] == s2[y-1]:
                i[x][y] = i[x-1][y-1] + 1
                if i[x][y] > longest:
                    longest = i[x][y]
                    x_longest = x

            else:
                i[x][y] = 0
    return s1[x_longest - longest: x_longest]

#print len(given)

found = ""

for k in range(len(given)-1):
    #print k
    found = str(findsharedmotif(given[k].seq,given[k+1].seq))
    for j in range(len(given)):
        dna = str(given[j].seq)
        if found not in dna:
            break
        else:
            toBreak = True
    if toBreak:
        break

print found

out = open('08_LCSM2out.txt','w')
out.write(str(found))
out.close()
