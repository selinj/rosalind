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

perms = []
alphstring = ''

for letter in alphabet:
    alphstring += letter

print alphstring

for i in range(n+1):
    #print i
    for p in itertools.product(alphabet,repeat=i):
        perms.append(p)

#a function to compare two variables by letter then length    
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

#a sorting function which makes use of the compare function, and swaps
#if two permutations are found to be unsorted
def combsort(listtosort):
    gap = len(listtosort)
    shrink = 1.3
    swapped = True
    counter = 0

    while swapped or gap != 1:
        gap = gap/shrink
        if gap <1:
            gap = 1
        i = 0
        swapped = False

        #compare 2 elements, swap if not sorted
        while (i+gap) < len(listtosort):
            counter += 1
            if compare(listtosort[i],listtosort[i+1],alphstring) == 1:
                listtosort[i],listtosort[i+1]=listtosort[i+1],listtosort[i]
                swapped = True
            i += 1
    
combsort(perms)
perms.pop(0)

out = open('14_LEXVout.txt','w')

for p in perms:
    out.write(''.join(p)+'\n')
out.close()

print "written"
