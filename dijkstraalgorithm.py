import heapq

def dijkstra(graph, start, goal):
    # Priority queue for nodes to explore
    pq = []
    heapq.heappush(pq, (0, start))  # (distance, node)
    
    # Dictionary to store the shortest distance to each node
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    
    # Dictionary to store the shortest path tree (previous nodes)
    previous = {node: None for node in graph}
    
    while pq:
        # Get the node with the smallest distance
        current_distance, current_node = heapq.heappop(pq)
        
        # If we reached the goal, reconstruct the path
        if current_node == goal:
            path = []
            while previous[current_node] is not None:
                path.insert(0, current_node)
                current_node = previous[current_node]
            path.insert(0, start)
            return path, distances[goal]
        
        # Process each neighbor of the current node
        for neighbor, weight in graph[current_node]:
            tentative_distance = current_distance + weight
            
            # If a shorter path to the neighbor is found
            if tentative_distance < distances[neighbor]:
                distances[neighbor] = tentative_distance
                previous[neighbor] = current_node
                heapq.heappush(pq, (tentative_distance, neighbor))
    
    # If the goal is not reachable
    return "No solution"

# Define the graph
graph = {
    'start': [('1', 7)],
    '1': [('2', 6)],
    '2': [('3', 5)],
    '3': [('4', 4), ('5', 3)],
    '4': [('6', 3), ('7', 6)],
    '5': [('8', 2)],
    '6': [('8', 2)],
    '7': [('9', 5)],
    '8': [('10', 3)],
    '9': [('12', 4)],
    '10': [('11', 1)],
    '11': [('goal', 0)],
    '12': [('14', 3)],
    '13': [('goal', 2)],
    '14': [('15', 2)],
    '15': [],
    'goal': []
}

# Run Dijkstra's algorithm
start_node = 'start'
goal_node = 'goal'
path, distance = dijkstra(graph, start_node, goal_node)
print(f"Shortest path: {path} with total distance: {distance}")
