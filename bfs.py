graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}
         
def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)      
    return visited

#print bfs(graph, 'A') # {'B', 'C', 'A', 'F', 'D', 'E'}


def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        print queue
        vertex, path = queue.pop(0)
        print "---"+str(graph[vertex])+'---'+str(set(path))
        non_visited_node=graph[vertex] - set(path)
        print "---"+str(non_visited_node)
        for next in non_visited_node:
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

print list(bfs_paths(graph, 'A', 'F')) # [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]

def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None

#   print shortest_path(graph, 'A', 'F') # ['A', 'C', 'F']



#http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/