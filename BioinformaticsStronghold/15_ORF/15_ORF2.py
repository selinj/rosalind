from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna
from Bio.Alphabet import generic_rna

handle = open('rosalind_orf.txt','rU')
data = SeqIO.parse(handle,'fasta').next()
handle.close()

dna = data.seq
mrna1 = dna.transcribe()
revc = dna.reverse_complement()
mrna2 = revc.transcribe()

mrna1 = str(mrna1)
mrna2 = str(mrna2)

reading_frames = []

def trans_RF(start,strand):
    rf = Seq(strand[start:])

    if len(rf) % 3 == 2:
        rf = str(rf)
        rf = rf + 'N'
        rf = Seq(rf)
    elif len(rf) % 3 == 1:
        rf = str(rf)
        rf = rf + 'NN'
        rf = Seq(rf)
    
    rf = rf.translate()
    rf = str(rf)
    j = rf.find('*')
    
    if j!= -1 and rf[0:1] == 'M':
        reading_frames.append(rf[:j])

def find_RF(strand):
    i = 0
    while i < len(strand):
        i = strand.find('AUG',i)
        if i == -1:
            break
        trans_RF(i,strand)
        trans_RF(i+1,strand)
        trans_RF(i+2,strand)
        i +=1

find_RF(mrna1)
find_RF(mrna2)
set_of_frames = list(set(reading_frames))

out = open('15_ORF2out.txt','w')
for element in set_of_frames:
    out.write(element+'\n')

out.close()
