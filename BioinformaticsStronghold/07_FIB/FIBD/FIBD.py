f1 = open('rosalind_fibd.txt','r')
f2 = open('FIBDoutput.txt', 'w')

n,m= f1.readline().split()
n = int(n) #how many months
m = int(m) #lifetime, in months

pairs = [0]*(n+1)
pairs[0] = 1
for month in range(2,n+1):
    pairs[month] = pairs[month-2] + pairs[month-1] - pairs[month- m -1]
    
print pairs[n] + pairs[n-1]
rabbits = pairs[n] + pairs[n-1]

f2.write(str(rabbits))
f2.close()
