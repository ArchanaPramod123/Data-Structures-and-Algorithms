def insert(v):
    if v in graph:
        print(v," already")
    else:
        graph[v]=[]
def insert_edge(v1,v2):
    if v1 not in graph:
        print(v1," not prest")
    elif v2 not in graph:
        print(v2," not prest")
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)
def delete(v):
    if v not in graph:
        print("not in the graph")
    else:
        graph.pop(v)
        for i in graph:
            list1=graph[i]
            if v in list1:
                list1.remove(v)
def delete_edge(v1,v2):
    if v1 not in graph:
        print(v1," not present")
    elif v2 not in graph:
        print(v2," not presnt")
    else:
        if v2 in graph[v1]:
            graph[v1].remove(v2)
            graph[v2].remove(v1)
def DFS(node,visited,graph):
    if node not in graph:
        print(node," not prest")
        return
    if node not in visited:
        print(node,end=" ")
        visited.add(node)
        for i in graph[node]:
            DFS(i,visited,graph)
import collections
def BFS(node,graph):
    visited=set()
    orginal=[]
    if node not in graph:
        print(node," not pressent")
        return
    queue=collections.deque([node])
    while queue:
        current=queue.popleft()
        if current not in visited:
            visited.add(current)
            orginal.append(current)

            for i in graph[current]:
                if i not in visited:
                    queue.append(i)
    return orginal


graph={}
visited=set()
insert("A")
insert("B")
insert("C")
insert("D")
insert("E")
insert_edge("A", "B")
insert_edge("A", "C")
insert_edge("B", "E")
insert_edge("C", "D")
insert_edge("D", "E")
print(graph)
delete("C")
print(graph)
# delete_edge("A","B")
print(graph)
DFS("A",visited,graph)
print(BFS("A",graph))
