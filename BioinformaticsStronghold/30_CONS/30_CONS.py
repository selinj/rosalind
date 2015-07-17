'''

m x n matrix has m rows, n colmns
matrix Aij --> value at intersection of row i, column n

-given several dna seqs of equal length n
-profile matrix: 4 x n matrix P
-P1j = # of times A occurs in the jth position of a string
- i  1 2 3 4
  nt A C G T
-consensus string c -- string of length n, formed from collection
-take most common symbol at each position
  (max val in jth column for each base)

'''

from Bio import SeqIO

handle = open('rosalind_cons.txt','rU')
data = SeqIO.parse(handle,'fasta')

sequences = []
for record in data:
    sequences.append(record.seq)

#test case from rosalind
#sequences = ['ATCCAGCT','GGGCAACT','ATGGATCT','AAGCAACC','TTGGAACT','ATGCCATT','ATGGCACT']

#print dna strings like a matrix
def matrix_printer(seqs):
    n = len(seqs[0])
    for seq in seqs:
        result = []
        for i in xrange(n):
            result.append(seq[i])
        print ' '.join(result)

#count the number of times a base appears at given index for set of strings
def column_count(nt, seqs, column):
    n = len(seqs[0])
    count = 0
    for seq in seqs:
        if seq[column] == nt:
                count += 1
    return count

#loop the prev. function to create a count list for every base
def count_all(nt, seqs):
    countlist = []
    for col in xrange(len(seqs[0])):
        countlist.append(column_count(nt, seqs, col))
    newlist = []
    for num in countlist:
        newlist.append(str(num))
    #print nt+ ': '+' '.join(newlist)
    toPrint = nt+ ': '+' '.join(newlist)
    return countlist, toPrint

#find consensus base at a particular position
def column_consensus(countlist,col):
    pos = 0
    num = 0
    symboldict = {1:'A',2:'C',3:'G',4:'T'}
    for basecount in countlist:
        pos += 1
        if basecount[col] > num:
            num = basecount[col]
            numpos = pos
    #print symboldict[numpos]
    return symboldict[numpos]

#find print consensus sequence for a set of strings
def find_consensus(countlist, seqs):
    consensus = []
    for col in xrange(len(seqs[0])):
        consensus.append(column_consensus(countlist,col))
    return consensus
        
#print "DNA sequences:"
#matrix_printer(sequences)

print "Base counts:"
Acount, Aprint = count_all('A', sequences)
Ccount, Cprint = count_all('C', sequences)
Gcount, Gprint = count_all('G', sequences)
Tcount, Tprint = count_all('T', sequences)
lists = [Acount, Ccount, Gcount, Tcount]

print "Consensus sequence:"
result = find_consensus(lists,sequences)
print ' '.join(result)

out = open('30_CONSout.txt','w')
out.write(''.join(result)+'\n')
out.write(Aprint + '\n' + Cprint + '\n' + Gprint + '\n' + Tprint)
out.close()

