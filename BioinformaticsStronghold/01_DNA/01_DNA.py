f1 = open('rosalind_dna.txt', 'r')
f2 = open('01_DNAoutput.txt', 'w')

A = 0
C = 0
G = 0
T = 0

while True:
    letter = f1.read(1)
    if letter == 'A':
        A = A + 1;
    elif letter == 'C':
        C = C + 1;
    elif letter == 'G':
        G = G + 1;
    elif letter == 'T':
        T = T + 1;
    if not letter: break

str(A)
str(C)
str(G)
str(T)

f2.write(str(A) + " " + str(C) + " " + str(G) + " " + str(T))
f2.close()
        

