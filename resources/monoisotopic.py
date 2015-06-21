#store the monoisotopic mass table

import os
import pickle

f1 = open(os.path.expanduser('~/Documents/CS/CS_Bio_self/rosalind/resources/monoisotopiclist.txt'),'r')
table = {}
index = 0

while True:
    line = f1.readline()
    if not line: break
    key, value = line.split()
    table[key] = float(value)
    index += 1

#create a new file in the resources folder in my rosalind directory
with open(os.path.expanduser('~/Documents/CS/CS_Bio_self/rosalind/resources/monoisotopictable.txt'),'wb') as f2:
    pickle.dump(table,f2) #pickle the table to that file for future use
    
