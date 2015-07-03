'''

given int 0<n<10000, and permutation p of length n
return longest increasing subsequence of p, and longest decreasing subsequence

'''
from itertools import groupby

n = 5
p = ['5','1','4','2','3']

#longest increasing subsequence]

setoflis = []*n
last = 0

for symbol in p:
    lis = []
    lis.append(symbol)
    found = []
    found.append(symbol)
    last = symbol
    print "found "+('').join(found)
    print "lis "+('').join(lis)
    for i in range(int(symbol),len(p)-1):
        print i
        if i>last:
            #found.append(i)
            print found
            last = i
        else:
            continue
        print "found list: "+found
    if len(found)>len(lis):
        lis = found
    setoflis.append(lis)

print setoflis

#print current


'''

set of longests = []*n

for every symbol in the sequence
start at symbol
    5 1 4 2 3
    longest = 5
    found =5
    last = symbol
    if i>last, found.append(i)
    last = i
    else continue
    if length of found > length longest
    longest = found

go through set of longests, return highest.
longest decreasing: reverse sequence. find lis. reverse lis.
'''
