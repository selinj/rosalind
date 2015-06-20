'''

Problem: Translating RNA into Protein
ID: PROT
URL: http://rosalind.info/problems/prot/

genetic string = incorporates protein strings along w/ DNA and RNA strings

given an RNA string s (corresponding to a strand of mRNA),
return the protein string encoded by s

'''

import pickle
import os

#make a new dictionary to store the RNA codon table
table = {'UUU':'F', 'UUC':'F', 'UUA':'L', 'UUG':'L', 'UCU':'S', 'UCC':'S',
         'UCA':'S', 'UCG':'S', 'UAU':'Y', 'UAC':'Y', 'UAA':'Stop',
         'UAG':'Stop', 'UGU':'C', 'UGC':'C', 'UGA':'Stop', 'UGG':'W',
         'CUU':'L', 'CUC':'L', 'CUA':'L', 'CUG':'L', 'CCU':'P', 'CCC':'P',
         'CCA':'P', 'CCG':'P', 'CAU':'H', 'CAC':'H', 'CAA':'Q', 'CAG':'Q',
         'CGU':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R', 'AUU':'I', 'AUC':'I',
         'AUA':'I', 'AUG':'M', 'ACU':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
         'AAU':'N', 'AAC':'N', 'AAA':'K', 'AAG':'K', 'AGU':'S', 'AGC':'S',
         'AGA':'R', 'AGG':'R', 'GUU':'V', 'GUC':'V', 'GUA':'V', 'GUG':'V',
         'GCU':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A', 'GAU':'D', 'GAC':'D',
         'GAA':'E', 'GAG':'E', 'GGU':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G'}

#create a new file in the resources folder in my rosalind directory
with open(os.path.expanduser('~/Documents/CS/CS_Bio_self/rosalind/resources/RNAcodontable.txt'),'wb') as f:
    pickle.dump(table,f) #pickle the table to that file for future use

#reloading the file from the pickle, to practice
table2 = pickle.load(
    open(os.path.expanduser(
        '~/Documents/CS/CS_Bio_self/rosalind/resources/RNAcodontable.txt')))

f1 = open('rosalind_prot.txt','r')
f2 = open('07_PROToutput.txt','w')

s = f1.readline()

print len(s)

length = 0

if len(s) % 3 != 0:
    if len(s)% 3 == 1:
        length = len(s) -1
    if len(s)% 3 == 2:
        length = len(s) -2
else:
    length = len(s)

print length
    
for i in range(0,length,3):
    aa = table2[s[i:i+3]]
    codon = s[i:i+3]
    if aa != 'Stop':
        f2.write(aa)
    elif aa == 'Stop':
        break

f2.close()
    
