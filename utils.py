def dfs(graph, node, visited, exwords):
    if node in exwords:
        return visited
    if node not in visited:
        visited.append(node)
        for k in graph[node]:
            dfs(graph, k, visited, exwords)
    return visited


def read_csv(filename):
    with open(filename) as fd:
        data = fd.readlines()
    data = [line.strip().split(';') for line in data]
    return {vertex: value for vertex, value in data}
