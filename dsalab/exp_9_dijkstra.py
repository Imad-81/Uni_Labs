import heapq

class CityGraph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, city1, city2, distance):
        # Add an undirected edge between two cities with the given distance
        self.graph.setdefault(city1, []).append((city2, distance))
        self.graph.setdefault(city2, []).append((city1, distance))

    def shortest_path(self, start_city, end_city):
        # Dijkstra's algorithm for finding the shortest path between two cities
        priority_queue = [(0, start_city)]
        visited = set()

        while priority_queue:
            current_distance, current_city = heapq.heappop(priority_queue)

            if current_city in visited:
                continue

            visited.add(current_city)

            if current_city == end_city:
                return current_distance

            for neighbor, distance in self.graph.get(current_city, []):
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (current_distance + distance, neighbor))

        return float('inf')  # No path found


# Example usage:
if __name__ == "__main__":
    # Create a CityGraph instance
    city_graph = CityGraph()

    # Add cities and their connections with distances
    city_graph.add_edge("CityA", "CityB", 50)
    city_graph.add_edge("CityA", "CityC", 100)
    city_graph.add_edge("CityB", "CityD", 25)
    city_graph.add_edge("CityC", "CityD", 60)
    city_graph.add_edge("CityD", "CityE", 40)

    # Find the shortest path between two cities and calculate total distance
    start_city = "CityA"
    end_city = "CityE"

    shortest_distance = city_graph.shortest_path(start_city, end_city)

    if shortest_distance != float('inf'):
        print(f"Shortest distance between {start_city} and {end_city}: {shortest_distance} units")
    else:
        print(f"No path found between {start_city} and {end_city}")
