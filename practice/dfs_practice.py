graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}


def dfs_path(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        vertex, path = stack.pop()
        non_visistednode = graph[vertex] - set(path)
        for next in non_visistednode:
            if next == goal:
                yield path + [next]
            else:
                stack.append((next,path + [next]))


print list(dfs_path(graph, 'A', 'F'))
