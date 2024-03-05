def insert(v):
    if v in graph:
        print(v," is already exist")
    else:
        graph[v]=[]
def add_edge(v1,v2):
    if v1 not in graph:
        print(v1," is not exist")
    elif v2 not in graph:
        print(v2," is not exist")
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)

def DFS(node,graph):
    visited=set()
    if node not in graph:
        print(node," is not present")
        return
    stack=[]
    stack.append(node)
    
    while stack:
        current=stack.pop()
        if current not in visited:
            print(current)
            visited.add(current)
            for i in graph[current]:
                stack.append(i)
graph={}
insert("A")
insert("B")
insert("C")
insert("D")
add_edge("A","B")
add_edge("A","C")

print(graph)
DFS("B",graph)