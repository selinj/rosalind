
f1 = open('rosalind_fib.txt','r')
f2 = open('07_FIBoutput.txt', 'w')

n,k= f1.readline().split()
n = int(n)
k = int(k)

baby = 1
new = 0
adult = 0

for i in range(1,n+1):
    #print i
    if i ==1:
        new = 0
        baby = 1
        adult =0
    if i ==2:
        adult = 0
        baby = 0
        new = 1
    if i==3:
        adult =1
        baby = adult*k
        new = 0 
    elif i >=4:
        adult = adult + new
        new = baby
        baby = adult*k
        
rabbits = (adult + new + baby)
print str(rabbits)

f2.write(str(rabbits))
f2.close()

