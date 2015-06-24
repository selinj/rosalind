
with open('rosalind_iev.txt','r') as f1:
    a,b,c,d,e,f=f1.readline().split()

a=float(a)
b=float(b)
c=float(c)
d=float(d)
e=float(e)

p = 2*a + 2*b + 2*c + 1.5*d + 1*e

with open('18_IEVout.txt','w') as f2:
    f2.write(str(p))
    f2.close()
