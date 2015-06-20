'''

Problem: Finding a Motif in DNA
ID: SUBS
URL: http://rosalind.info/problems/hamm/

A motif = commonly shared stretch of DNA

Given 2 str s and t, t is a substring of s if it is
found as a contiguous sequence in s

Return all locations of the substring t in s

'''

f1 = open('rosalind_subs.txt', 'r')
f2 = open('05_SUBSoutput.txt', 'w')

s = f1.readline()
t = f1.readline()

for i in range(len(s)):   
    if s[i:i+len(t)-1] == t[0:len(t)-1]:
        f2.write(str(i+1)+' ')
    else:
        pass
                 
f2.close()

        
