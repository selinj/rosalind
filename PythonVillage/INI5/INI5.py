#given a file w <= 1000 lines
#return a file containing all even-no'd lines from original file

inputfile = open('rosalind_ini5.txt', 'r')
outputfile = open('INI5output.txt', 'w')

listofstr = []
evens = 0
index = 0

for line in inputfile:
    if index % 2 == 1: #even
        listofstr.append(line)
#        evens = evens + 1
    else:
        pass
    index = index + 1

secondindex = 0

for i in listofstr:
    outputfile.write(listofstr[secondindex] + '\n')
    secondindex = secondindex + 1
    #print listofstr[secondindex]

outputfile.close()

#print 'done'
