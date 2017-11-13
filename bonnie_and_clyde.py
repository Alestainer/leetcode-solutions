import queue

graph = dict()

# Read the data

n, m, q = input().strip().split(' ')
n, m, q = [int(n), int(m), int(q)]
for a0 in range(m):
    u, v = input().strip().split(' ')
    u, v = [int(u), int(v)]

    if u in graph:
        graph[u].add(v)
    else:
        graph[u] = set([v])

    if v in graph:
        graph[v].add(u)
    else:
        graph[v] = set([u])


# We look for the shortest path between two vertices, bonnie's and clyde's coordinates
# After that we check if the pizza place was visited
# Can optimize execution time if memoize all paths and check them upon request
def find_shortest(graph, start, goal, visit):

    pq = queue.PriorityQueue()
    prev = dict()
    pq.put((0, start))
    prev[start] = None

    while not pq.empty():

        length, vertex = pq.get()

        if vertex == goal:

            prev_vert = prev[vertex]

            while prev_vert is not None:

                if prev_vert == visit:
                    return True
                prev_vert = prev[prev_vert]
        else:

            for v in graph[vertex]:
                if v != prev[vertex]:
                    pq.put((length + 1, v))
                    prev[v] = vertex
    return False

  
# Process the cases

for a0 in range(q):

    u, v, w = input().strip().split(' ')
    u, v, w = [int(u), int(v), int(w)]

    if find_shortest(graph, start= v, goal= u, visit= w):
        print ("YES")
    else:
        print ("NO")