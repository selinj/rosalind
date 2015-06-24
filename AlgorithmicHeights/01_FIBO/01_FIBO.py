
with open('rosalind_fibo.txt','r') as handle:
    i = int(handle.readline())
    #print i

n = 6
def Fib(n):
    f = [0,1]
    a,b = 0,1
    for i in range(n):
        f.append(b)
        a,b = b,a+b
    #print f
    #print n
    print f
    print b
print Fib(n)

out = open('01_FIBOout.txt','w')
out.write(str(Fib(n)))
out.close()
