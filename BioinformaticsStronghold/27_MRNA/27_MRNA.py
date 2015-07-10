'''
eg.
M: 1 possibility
A: 4 possibilities
Stop: 3
:. 1 *4 *3 % 100000 = 12
'''

f1 = open('rosalind_mrna.txt','r')
protein = str(f1.readline().strip('\n'))

count = {'F':2, 'L':6, 'S':6, 'Y':2, '*':3, 'P':4, 'H':2,
                     'Q':2, 'R':6, 'I':3, 'M':1, 'T':4, 'N':2, 'K':2,
                     'V':4, 'A':4, 'D':2, 'E':2, 'G':4, 'C':2, 'W':1}
poss = count['*']

for aa in protein:
    poss = poss * count[aa] % 1000000

f2 = open('27_MRNAout.txt','w')
f2.write(str(poss))
f2.close()

print poss
