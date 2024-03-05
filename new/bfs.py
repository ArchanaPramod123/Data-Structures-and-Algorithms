import collections
def BSF(node,graph):
    visited=set()
    if node not in graph:
        print(node," is not present")
        return
    queue=collections.deque([node])
    while queue:
        curent=queue.popleft()
        if curent not in visited:
            visited.add(curent)
            for i in graph[curent]:
                if i not in visited:
                    queue.append(i)
    sel


    




graph={}

    
