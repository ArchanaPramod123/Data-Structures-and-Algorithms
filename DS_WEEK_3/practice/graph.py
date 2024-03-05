def insert(v):
    if v in graph:
        print(v," already exist")
    else:
        graph[v]=[]
def insert_edge(v1,v2):
    if v1 not in graph:
        print(v1," not present")
    elif v2 not in graph:
        print(v2," not present")
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)
def delete(v):
    if v not in graph:
        print(v ," is not present")
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
        print(v2," not present")
    else:
        if v2 in graph[v1]:
            graph[v1].remove(v2)
            graph[v2].remove(v1)


    




graph={}
insert("A")
insert("B")
insert("C")
insert("D")
insert_edge("A","B")
insert_edge("A","C")
print(graph)
print("\n===remove====")
delete("D")
delete_edge("A","C")
print(graph)

