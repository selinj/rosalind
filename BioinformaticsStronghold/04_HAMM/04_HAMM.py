'''

Problem: Counting Point mutations
No. 06, ID: HAMMM
URL: http://rosalind.info/problems/hamm/

Given two strings s and t of equal length
the Hamming distance between s and t (dH(s,t))
is the no. of corresponding symbols that differ across the two

'''


fIN = open('rosalind_hamm.txt', 'r')
fOUT = open('06_HAMMoutput.txt', 'w')

s1 = fIN.readline()
s2 = fIN.readline()

dH = 0

for i in range(len(s1)):
    if s1[i] is not s2[i]:
        dH += 1

fOUT.write(str(dH))
fOUT.close()
