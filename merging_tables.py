# python3

import sys
import collections
n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))
rank = [1] * n
parent = list(range(0, n))
ans = max(lines)

def getParent(table):
    if table != parent[table]:
        parent[table] = getParent(parent[table])
    return parent[table]

def merge(destination, source):
    realDestination, realSource = getParent(destination), getParent(source)
    
    if realDestination == realSource:
        return 1
    
    if rank[realDestination]> rank[realSource]:
        parent[realSource] = realDestination
    else:
        parent[realDestination] = realSource
        if rank[realDestination] == rank[realSource]:
            rank[realSource] = rank[realDestination]+1
    # merge two components
    # use union by rank heuristic 
    # update ans with the new maximum table size
    
    return 1

for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    merge(destination - 1, source - 1)
    counter = collections.Counter(parent)
    x, ans = counter.most_common(1)[0]
    print(ans)
    #print (" this is rank" ,rank)
    #print (" this is parent", parent)
