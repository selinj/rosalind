'''

RNA nt's bind to one another like in DNA, defining the secondary
structure of RNA.

Here, consier a simpler/impractical case: every nt bonds in
a base pair in the RNA molecule


A matching for graph G is the edges of G for which no node
belongs to more than 1 edge.

G w/ even number of nodes, 2n
then G is perfect if n edges.

Kn = complete graph of 2n labeled nodes.
Every node is connected to every other node w/ an edge.
Pn = total number of perfect matchings
for a node x, there are 2n - 1 ways to join x to the other nodes
Pn = (2n-1) * Pn-1
p1 = 1
so
Pn = (2n-1)(2n-3)(2n-5)...(3)(1)

'''

s = 'AGCUAGUCAU'

s = 'ABCDEFGH'

au = 'AUAUAU'
gc = 'GCGC'

n = len(s)


Pn = (2*n-1)*(2*n-2)*(2*n-3)
print Pn
