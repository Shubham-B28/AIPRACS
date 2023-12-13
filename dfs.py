graph = {
    1: [2, 3, 4, 5],
    2: [],
    3: [6, 7],
    4: [],
    5: [8, 9],
    6: [],
    7: [10],
    8: [11],
    9: [],
    10: [],
    11: []
}



def dfs(node):
    visited = set()
    if node not in visited:
        print(node,end = " ")
        visited.add(node)
        for i in graph[node]:
            dfs(i)


dfs(1)

def dfs_stack(start,graph):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            print(node,end = " ")
            visited.add(node)
            stack.extend(neighbour for neighbour in graph[node] if neighbour not in visited)

print("\n Using Stack")
dfs_stack(1,graph)
