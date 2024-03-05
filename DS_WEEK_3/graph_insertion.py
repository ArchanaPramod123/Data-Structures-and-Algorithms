def insertion(v):
    global node_counts
    if v in nodes:
        print(v," is already existing in the graph")
    else:
        node_counts=node_counts+1
        nodes.append(v)
        for i in graph:
            i.append(0)
        temp=[]
        for i in range(node_counts):
            temp.append(0)
        graph.append(temp)
def print_f():
    for i in range(node_counts):
        for j in range(node_counts):
            print(format(graph[i][j],'<3'),end=" ")
        print()
def add_edge(v1,v2,cost):
    if v1 not in nodes:
        print(v1,' is not present in the graph')
    elif v2 not in nodes:
        print(v2,' is not present in the graph')
    else:
        index1=nodes.index(v1)
        index2=nodes.index(v2)
        graph[index1][index2]=cost
        graph[index2][index1]=cost
def delete(v):
    global node_counts
    if v not in nodes:
        print(v," is not present in the graph")
    else:
        index1=nodes.index(v)
        node_counts=node_counts-1
        nodes.remove(v)
        graph.pop(index1)
        for i in graph:
            i.pop(index1)
def delete_edge(v1,v2):
    if v1 not in nodes:
        print(v1," not present")
    elif v2 not in nodes:
        print(v2," not present")
    else:
        index1=nodes.index(v1)
        index2=nodes.index(v2)
        graph[index1][index2]=0
        graph[index2][index1]=0

    

nodes=[]
graph=[]
node_counts=0
print("before add")
print(nodes)
print(graph)
insertion('A')
insertion('B')
insertion('C')
insertion('D')
add_edge('A','B',10)
add_edge('A','C',8)

print("after add")
print(nodes)
print(graph)
print_f()
# delete('C')
print("after delete")
print(nodes)
print(graph)
print_f()
delete_edge('A','C')
print("after deleting edge")

print_f()