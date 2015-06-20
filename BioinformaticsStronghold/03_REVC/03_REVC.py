f1 = open('rosalind_revc.txt', 'r')
f2 = open('03_REVCoutput.txt', 'w')

slist = []

while True:
    letter = f1.read(1)
    if letter == 'A':
        slist.append('T')
    if letter == 'T':
        slist.append('A')
    if letter == 'C':
        slist.append('G')
    if letter =='G':
        slist.append('C')
    if not letter: break


scomp = ''.join(slist)
srevcomp = scomp[::-1]

f2.write(srevcomp)
f2.close()
