def insert(v):
    if v in graph:
        print(v," already in the graph")
    else:
        graph[v]=[]
def add_edge(v1,v2):
    if v1 not in graph:
        print(v1," not present")
    elif v2 not in graph:
        print(v2," not presnet")
    else:
        # list1=[v1,cost]
        # list2=[v2,cost]
        # graph[v1].append(list1)
        # graph[v2].append(list2)

        #in directed
        # list1=[v2,cost]
        # graph[v1].append(list1)

        # in the undirected and weight 
        graph[v1].append(v2)  
        graph[v2].append(v1)
def delete(v):
    if v not in graph:
        print(v," is not present")
    else:
        graph.pop(v)
        for i in graph:
            list1=graph[i]
            # if v in list1:
            #     list1.remove(v)
            for j in list1:
                if v==j[0]:
                    list1.remove(j)
                    break
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
insert('A')
insert('B')
insert('C')
insert('D')
insert('E')
add_edge('A','B')
add_edge('A','C')
add_edge('C','B')
print(graph)
# delete('A')
delete_edge('C','B')
print(graph)