'''
Given: 3 positive integers
k: homozygous dominant AA
m: heterozygous Aa
n: homozygous recessive aa

Return: probabiliy that 2 random organisms will produce an individual
w/ dominant phenotype, ie. genotype Aa or AA
'''

f1 = open('rosalind_iprb.txt','r')
f2 = open('16_IRPBout.txt','w')

a,b,c = f1.readline().split()
a = float(a)
b = float(b)
c = float(c)

total = a+b+c

p1 = (a/total)*(((a-1)/(total-1))+b/(total-1)+c/(total-1))
p2 = (b/total)*(a/(total-1)+ ((b-1)/(total-1))*0.75 + (c/(total-1))*0.5)
p3 = (c/total)*(a/(total-1) + (b/(total-1))*0.5)

p_of_A = p1 + p2 + p3 

print p_of_A
f2.write(str(p_of_A))
f2.close()
