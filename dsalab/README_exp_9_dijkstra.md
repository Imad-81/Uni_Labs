# Experiment 9: Dijkstra's Shortest Path Algorithm

**Aim:** To implement Dijkstra's algorithm to find the shortest path between cities in a graph.

**Algorithm:**
1. **Graph Representation**: Use an adjacency list to represent cities and the distances between them.
2. **Priority Queue**: Use a min-heap (`heapq`) to always process the nearest unvisited city.
3. **Shortest Path Logic**:
   - Initialize distances to all cities as infinity, except the start city (0).
   - While the queue is not empty:
     - Pop the city with the smallest distance.
     - For each neighbor, calculate the potential new distance.
     - If the new distance is smaller than the recorded distance, update it and push to the queue.
4. Return the minimum distance to the target city.

**Key Features:**
- Efficient pathfinding using `heapq`.
- Supports undirected graphs with weighted edges.
- Handles scenarios with no possible path between nodes.
