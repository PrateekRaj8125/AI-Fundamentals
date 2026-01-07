import heapq
def uniform_cost_search(graph, start, goal):
    # Priority queue entries: (total_cost, current_node, path)
    frontier = [(0, start, [start])]
    visited_costs = {start: 0}
    while frontier:
        cost, node, path = heapq.heappop(frontier)
        if node == goal:
            return cost, path
        for neighbor, edge_cost in graph.get(node, []):
            new_cost = cost + edge_cost
            if neighbor not in visited_costs or new_cost < visited_costs[neighbor]:
                visited_costs[neighbor] = new_cost
                heapq.heappush(
                    frontier,
                    (new_cost, neighbor, path + [neighbor])
                )
    return float("inf"), []


from collections import deque
def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    visited = {start}
    while queue:
        node, path = queue.popleft()
        if node == goal:
            return path
        for neighbor, _ in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return []


# Define the graph as an adjacency list with weights
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': []
}
cost, path = uniform_cost_search(graph, 'A', 'D')
print(cost, path)

path = bfs(graph, 'A', 'D')
print(path)