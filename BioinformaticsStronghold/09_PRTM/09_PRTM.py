import pickle
import os


monoisotopic = pickle.load(
    open(os.path.expanduser(
        '~/Documents/CS/CS_Bio_self/rosalind/resources/monoisotopictable.txt')))

monoisotopic['\n'] = 0
f1 = open('rosalind_prtm.txt','r')
f2 = open('09_PRTMout.txt','w')
P = f1.readline()

def weigh(P):
    mass = 0
    for aa in P:
        mass = mass + float(monoisotopic[aa])
        if aa == '\n':
            continue
    return mass

print weigh(P)
f2.write(str(weigh(P)))
f2.close()
