# 📂 Algorithm Implementations in Python

This repository contains implementations of key algorithms in Python for solving specific optimization problems. Each script focuses on a unique problem, including Huffman Coding, Job Scheduling with Deadlines, Minimum Jumps to reach the end of an array, and finding the shortest path in a graph using Dijkstra's algorithm.

## 📜 Contents

1. **Huffman Coding (huffmancoding.py)** - A data compression algorithm based on character frequencies.
2. **Job Scheduling with Deadlines (jobschedulingwithdeadlines.py)** - A greedy algorithm to maximize profit by scheduling jobs within their deadlines.
3. **Minimum Jumps (MinJumps.py)** - An algorithm to find the minimum number of jumps to reach the end of an array.
4. **Dijkstra's Algorithm (dijkstra.py)** - An algorithm to find the shortest path between two nodes in a weighted graph.

---

### 🗜️ 1. Huffman Coding (`huffmancoding.py`)

**Description**: This script implements the Huffman Coding algorithm, a greedy technique for compressing data by minimizing the total length of the encoded message. Given character frequencies, the script generates a prefix-free binary code for each character based on its frequency.

**Example Usage**:
```python
# Define character frequencies
char_freqs = {'A': 10, 'B': 15, 'C': 30, 'D': 40, 'E': 5}
# Run the Huffman coding function
result = huffman_coding(char_freqs)
print(result)

Key Features:

    Creates a binary tree where frequently used characters have shorter codes.
    Efficiently encodes characters to minimize overall message size.

📅 2. Job Scheduling with Deadlines (jobschedulingwithdeadlines.py)

Description: This script uses a greedy algorithm to maximize the profit from scheduling jobs, each with a specific profit and deadline. Jobs are scheduled in descending order of profit to ensure maximum gain within the provided deadlines.

Example Usage:

python

jobs = [Job(100, 2), Job(19, 1), Job(27, 2), Job(25, 1), Job(15, 3)]
max_profit = job_scheduling(jobs)
print(f"Max profit = {max_profit}")  # Expected output: Max profit = 142

Key Features:

    Schedules jobs to maximize total profit.
    Considers each job’s deadline and avoids overlap using a slot allocation array.

🚀 3. Minimum Jumps (MinJumps.py)

Description: This script calculates the minimum number of jumps required to reach the end of an array, where each element indicates the maximum number of steps that can be jumped from that position. The algorithm uses a greedy approach to efficiently find the shortest path to the last index.

Example Usage:

python

input_array = [2, 3, 1, 1, 4]
result = min_jumps(input_array)
print(f"Minimum number of jumps to reach the end: {result}")  # Expected output: 2

Key Features:

    Utilizes a greedy approach to calculate the fewest number of jumps.
    Maintains optimal time complexity for large inputs.

📍 4. Dijkstra's Algorithm (dijkstra.py)

Description: This script implements Dijkstra's algorithm to find the shortest path between two nodes in a weighted graph. It uses a priority queue to explore nodes in order of distance, ensuring an efficient path discovery from the start to the goal node.

Example Usage:

python

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
print(f"Shortest path: {path} with total distance: {distance}")  # Expected output: Shortest path and distance

Key Features:

    Finds the shortest path between nodes in a weighted graph.
    Efficiently processes paths using a priority queue to minimize computational complexity.

🔧 Requirements

Each script requires Python 3.x and no additional libraries except for Dijkstra's algorithm, which uses the heapq library (a built-in Python library for priority queues).
