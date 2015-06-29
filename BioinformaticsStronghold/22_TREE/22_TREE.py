'''

undirected graph is connected if a path connects any 2 nodes
tree = connected, undirected graph w/ no cycles
.: tree has a branching structure around core of nodes


given int n and adjacency list --> describes graph
    of n nodes w/ no cycles
return min no. edges that can be added to graph to produce tree

1. use adjacency list to generate graph
2. count the n. separate graphs?
3. # edges to make tree = # separate graphs - 1
'''

n = 10 #number of nodes in graph

adjlist =[(1,2),(2,8),(4,10),(5,9),(6,10),(7,9)]

groups = []
for edge in adjlist:
    attached = []
    for i in edge:
        for e in adjlist:
            if i in e:
                attached.append(e)
    groups.append(attached)
    #print attached

print groups

for grp in groups:
    index = 0
    for edge in grp:
        if edge in grp:
            grp.pop(index)
            break
        index +=1

print groups
