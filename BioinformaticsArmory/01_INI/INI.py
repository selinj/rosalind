from Bio.Seq import Seq

with open('rosalind_ini.txt','r') as handle:
    dna = Seq(handle.readline())

with open('01_INIout.txt','w') as out:
    out.write(str(dna.count("A")) + " " + str(dna.count("C")) + " " + str(dna.count("G")) + " " + str(dna.count("T")))

out.close()
