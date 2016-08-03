graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}


def bfs_path(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        vertex, path = queue.pop(0)
        node_unvisited = graph[vertex] - set(path)
        for next in node_unvisited:
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))


print list(bfs_path(graph, 'A', 'F'))