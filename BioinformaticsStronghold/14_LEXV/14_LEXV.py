'''

we organize genetic strings lexographically


given a collection of <= 10 symbols defining an ordered alphabet, and int n
return all strings of length n, ordered lexographically

'''

import itertools

given = open('rosalind_lexv.txt','r')
alphraw = str(given.readline().rstrip())
alphabet = alphraw.split(' ')
n = int(given.readline())

alphabet = ['D','N','A']
#n=3

perms = []
count = 0
alphstring = ''

for letter in alphabet:
    alphstring += letter

print alphstring

for i in range(n+1):
    #print i
    for p in itertools.product(alphabet,repeat=i):
        perms.append(p)
        count +=1

#print perms
#print count

#perms = [('D','A'),('A','A','A'),('N'),('D','D','D'),('N','A','D'),('N','D','A')]

#print perms

#a function to compare two variables by letter
    
def compare(p1,p2,orderedsymbols):
    result = 0
    length = 0
    if len(p1) > len(p2) or len(p1) == len(p2):
        length = len(p2)
    elif len(p1) < len(p2):
        length = len(p1)
        
    for j in range(length):
        index1 = orderedsymbols.find(p1[j])
        index2 = orderedsymbols.find(p2[j])        
        if index1 == index2:
            continue #check next letter
        elif index1 < index2:
            result = -1 #sorted
            return result
        elif index1 > index2:
            result = 1 #not sorted
            return result
    if result == 0:
        if len(p2) > len(p1):
                result = -1 #second longer than first = sorted correctly
        elif len(p1) > len(p2):
                result = 1 #not sorted if second shorter than first
        return result           

def bubblesort(listtosort):
    for i in range(1,len(listtosort)):
        for j in range(i+1,len(listtosort)):
            #print perms[i]
            if compare(listtosort[i],listtosort[i+1],alphstring) == 1:
                #then swap
                listtosort[i],listtosort[i+1]=listtosort[i+1],listtosort[i]
    return listtosort

for i in range(len(perms)):
    bubblesort(perms)
#print perms
perms.pop(0)

printformat = ''

out = open('14_LEXVout.txt','w')

for p in perms:
    print p
    for i in range(1,len(p)):
        printformat += '{}'
    print printformat.format(*p)
out.close()
