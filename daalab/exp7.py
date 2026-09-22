# Experiment 7: Minimum Spanning Tree (MST)
# 7(a) - Prim's Algorithm
# 7(b) - Kruskal's Algorithm


# ==========================================================
# 7(a) - Prim's Algorithm
# ==========================================================
def prims_algorithm(vertices, edges):
    n = len(vertices)

    # Start with the first vertex
    selected = [vertices[0]]

    # Create empty list for MST
    mst = []

    # Set total cost to 0
    total = 0

    # Repeat until all vertices are selected
    while len(selected) < n:

        # Set minimum weight to a large number
        minimum = 999999

        # Set best edge as empty
        best = None

        # Check all edges
        for u, v, weight in edges:

            # Check if u is selected and v is not selected
            if u in selected and v not in selected:

                # Check for minimum weight
                if weight < minimum:
                    minimum = weight
                    best = (u, v, weight)

            # Check if v is selected and u is not selected
            elif v in selected and u not in selected:

                # Check for minimum weight
                if weight < minimum:
                    minimum = weight
                    best = (v, u, weight)

        # If no edge is found
        if best is None:
            print("Graph is not connected")
            break

        # Get the selected edge
        u, v, weight = best

        # Add the new vertex
        selected.append(v)

        # Add edge to MST
        mst.append((u, v, weight))

        # Add weight to total
        total = total + weight

    return mst, total


def run_prims():
    # Enter number of vertices
    n = int(input("Enter number of vertices: "))

    # Enter vertex names
    vertices = input("Enter vertex names: ").split()

    # Enter number of edges
    e = int(input("Enter number of edges: "))

    # Create empty list for edges
    edges = []

    # Enter all edges
    for i in range(e):

        # Enter edge like A-B
        edge = input("Enter edge: ")

        # Remove spaces
        edge = edge.replace(" ", "")

        # Enter weight
        weight = int(input("Enter weight: "))

        # Separate the two vertices
        u, v = edge.split("-")

        # Store edge and weight
        edges.append((u, v, weight))

    mst, total = prims_algorithm(vertices, edges)

    # Display the result
    print("\nMinimum Spanning Tree:")

    # Print MST edges
    for u, v, weight in mst:
        print(u, "-", v, "=", weight)

    # Print total cost
    print("Minimum cost =", total)


# ==========================================================
# 7(b) - Kruskal's Algorithm
# ==========================================================
def kruskals_algorithm(vertices, edges):
    n = len(vertices)

    # Sort all edges according to weight
    edges_sorted = sorted(edges, key=lambda x: x[2])

    # Create a parent dictionary
    parent = {}

    # Make every vertex its own parent
    for vertex in vertices:
        parent[vertex] = vertex

    # Function to find the parent of a vertex
    def find(vertex):

        # Continue until the vertex is its own parent
        while parent[vertex] != vertex:
            vertex = parent[vertex]

        # Return the parent
        return vertex

    # Create an empty list for MST
    mst = []

    # Set total cost to 0
    total = 0

    # Check edges one by one
    for u, v, weight in edges_sorted:

        # Find parent of first vertex
        parent_u = find(u)

        # Find parent of second vertex
        parent_v = find(v)

        # Check if adding edge creates a cycle
        if parent_u != parent_v:

            # Add edge to MST
            mst.append((u, v, weight))

            # Add weight to total
            total = total + weight

            # Join the two sets
            parent[parent_u] = parent_v

        # Stop when MST has n-1 edges
        if len(mst) == n - 1:
            break

    return mst, total


def run_kruskals():
    # Enter number of vertices
    n = int(input("Enter number of vertices: "))

    # Enter vertex names
    vertices = input("Enter vertex names: ").split()

    # Enter number of edges
    e = int(input("Enter number of edges: "))

    # Create an empty list to store edges
    edges = []

    # Enter all edges
    for i in range(e):

        # Enter edge like A-B
        edge = input("Enter edge: ")

        # Remove spaces
        edge = edge.replace(" ", "")

        # Enter weight
        weight = int(input("Enter weight: "))

        # Separate the two vertices
        u, v = edge.split("-")

        # Store edge and weight
        edges.append((u, v, weight))

    mst, total = kruskals_algorithm(vertices, edges)

    # Display the MST
    print("\nMinimum Spanning Tree:")

    # Print all MST edges
    for u, v, weight in mst:
        print(u, "-", v, "=", weight)

    # Print total cost
    print("Minimum cost =", total)


# ==========================================================
# Main Interactive Runner
# ==========================================================
def main():
    print("==========================================================")
    print("  EXPERIMENT 7: DAA LAB - MINIMUM SPANNING TREE (MST)")
    print("==========================================================")
    print("1. 7(a) - Prim's Algorithm")
    print("2. 7(b) - Kruskal's Algorithm")
    print("3. Run Both Experiments (Interactive)")
    print("==========================================================")

    choice = input("Enter choice (1-3) [default: 3]: ").strip()
    if not choice:
        choice = "3"

    if choice in ["1", "3"]:
        print("\n--- 7(a) Prim's Algorithm ---")
        run_prims()

    if choice in ["2", "3"]:
        print("\n--- 7(b) Kruskal's Algorithm ---")
        run_kruskals()


if __name__ == "__main__":
    main()
