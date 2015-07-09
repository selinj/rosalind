'''
given a DNA string in fasta
return position and length of every reverse palindrome in the string
 w/ 4 <= length <= 12, in any order
'''

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna

tester = '1234556789'
print tester[0:10]
print len(tester)
print tester[::-1]

'''
then for a string s of length n
the reverse of the string is s[::-1]
and if s is equal to its reverse, then s is a palindrome
'''

test2 = 'noon'
print test2
print test2[0:2]
test3 = test2[::-1]
print test2 == test3


def check_palindrome(s):
    forward = s
    reverse = s[::-1]
    return forward == reverse

print check_palindrome(test2)

'''
a DNA string is a reverse palindrome if it is equal
to its reverse complement
'''

handle = open('rosalind_revp.txt','rU')
data = SeqIO.parse(handle,'fasta').next()
handle.close()

dna = data.seq
revc = data.seq.reverse_complement()

#check every substring of length between 4 and 12, if it equals its reverse complement

def check_p(start,n):
    #s is the start index, n is the length
    if dna[start:start+n] == revc[(start+n-1):(start-1):-1]:
        print dna[start:start+n]
        print revc[start+n-1:start-1:-1]
        return True
    else:
        return False

out = open('26_REVPout.txt','w')

for n in range(4,12):
    print n
    for i in range(len(dna)):
        if check_p(i,n):
            print str(i) + ' ' + str(n)
            print str(dna[i:i+n])
            print str(revc[(i+n-1):(i-1):-1])
            #out.write(str(i+1) + ' ' + str(n)+'\n')
            #out.write(str(dna[i:i+n])+'\n')
            #out.write(str(revc[i+n-1:i-1:-1])+'\n\n')

out.close()
