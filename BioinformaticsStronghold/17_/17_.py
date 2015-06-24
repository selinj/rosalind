#given 2 dna strings s and t
#return collection of indices of s in which symbols of t appear in order


s = 'ACGTACGTGACG'
t = 'GTA'

symbols = []
for nt in t:
    symbols.append(nt)

indexlist = ""
index = 0
for symbol in symbols:
    for nt in s:
        if symbol == nt:
            indexlist += str(index) + " "
        index +=1
print indexlist
    
        
