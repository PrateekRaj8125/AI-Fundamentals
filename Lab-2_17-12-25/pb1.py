#Breadth-first Search
# Breadth-First Search (BFS) using an array-based queue

def bfs(graph, start):
    visited = [False] * len(graph)
    queue = [0] * len(graph)
    front = 0
    rear = 0
    visited[start] = True
    queue[rear] = start
    rear += 1
    print("BFS traversal:", end=" ")
    while front < rear:
        current = queue[front]
        front += 1
        print(current, end=" ")
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue[rear] = neighbor
                rear += 1
graph = [
    [1, 2],
    [0, 3, 4],
    [0, 5],
    [1],
    [1],
    [2]
]
bfs(graph, 0)