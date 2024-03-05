def insert(v):
    if v in graph:
        print(v," is alrady present")
    else:
        graph[v]=[]
def add_edge(v1,v2):
    if v1 not in  graph:
        print(v1," is not present in the graph")
    elif v2 not in graph:
        print(v2," is not presnt in the graph")
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)

def DFS(node,visited,graph):
    if node not in graph:
        print(node," not in the graph")
        return
    if node not in visited:
        print(node)
        visited.add(node)
        for i in graph[node]:
            DFS(i,visited,graph)



graph={}
visited=set()
insert("A")
insert("B")
insert("C")
insert("D")
add_edge("A","B")
add_edge("B","C")
print(graph)
DFS("A",visited,graph)
