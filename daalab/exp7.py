# Experiment 7: Minimum Spanning Tree (MST)
# 7(a) - Prim's Algorithm
# 7(b) - Kruskal's Algorithm


# ==========================================================
# 7(a) - Prim's Algorithm
# ==========================================================
def prims_algorithm(vertices, edges):
    if not vertices:
        return [], 0
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
        minimum = float('inf')

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


def _read_edge(i):
    while True:
        try:
            raw = input(f"Enter edge {i + 1} (e.g. A-B or A B): ").strip()
            if not raw:
                continue
            # Support formats: "A-B 5", "A B 5", "A-B", "A B"
            cleaned = raw.replace("-", " ").replace(",", " ")
            parts = cleaned.split()
            if len(parts) >= 3:
                return parts[0], parts[1], int(parts[2])
            elif len(parts) == 2:
                w_str = input("Enter weight: ").strip()
                return parts[0], parts[1], int(w_str)
            elif len(parts) == 1 and "-" in raw:
                u, v = raw.replace(" ", "").split("-")
                w_str = input("Enter weight: ").strip()
                return u, v, int(w_str)
            else:
                print("Format not recognized. Please enter edge like 'A-B' or 'A B'.")
        except ValueError:
            print("Invalid weight! Please enter an integer weight.")


def run_prims():
    while True:
        try:
            n_str = input("Enter number of vertices: ").strip()
            if not n_str:
                continue
            n = int(n_str)
            if n < 1:
                print("Number of vertices must be at least 1.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")

    vertices = input("Enter vertex names: ").split()
    while len(vertices) < n:
        more = input(f"Please enter remaining {n - len(vertices)} vertex names: ").split()
        vertices.extend(more)
    vertices = vertices[:n]

    while True:
        try:
            e_str = input("Enter number of edges: ").strip()
            if not e_str:
                continue
            e = int(e_str)
            if e < 0:
                print("Number of edges cannot be negative.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")

    edges = []
    for i in range(e):
        u, v, weight = _read_edge(i)
        edges.append((u, v, weight))

    mst, total = prims_algorithm(vertices, edges)

    # Display the result
    print("\nMinimum Spanning Tree:")
    for u, v, weight in mst:
        print(u, "-", v, "=", weight)

    print("Minimum cost =", total)


# ==========================================================
# 7(b) - Kruskal's Algorithm
# ==========================================================
def kruskals_algorithm(vertices, edges):
    n = len(vertices)
    if n == 0:
        return [], 0

    # Sort all edges according to weight
    edges_sorted = sorted(edges, key=lambda x: x[2])

    # Create a parent dictionary
    parent = {}

    # Make every vertex its own parent
    for vertex in vertices:
        parent[vertex] = vertex

    # Function to find the parent of a vertex
    def find(vertex):
        if vertex not in parent:
            parent[vertex] = vertex

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

    if len(mst) < n - 1 and n > 1:
        print("Graph is not connected")

    return mst, total


def run_kruskals():
    while True:
        try:
            n_str = input("Enter number of vertices: ").strip()
            if not n_str:
                continue
            n = int(n_str)
            if n < 1:
                print("Number of vertices must be at least 1.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")

    vertices = input("Enter vertex names: ").split()
    while len(vertices) < n:
        more = input(f"Please enter remaining {n - len(vertices)} vertex names: ").split()
        vertices.extend(more)
    vertices = vertices[:n]

    while True:
        try:
            e_str = input("Enter number of edges: ").strip()
            if not e_str:
                continue
            e = int(e_str)
            if e < 0:
                print("Number of edges cannot be negative.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")

    edges = []
    for i in range(e):
        u, v, weight = _read_edge(i)
        edges.append((u, v, weight))

    mst, total = kruskals_algorithm(vertices, edges)

    # Display the MST
    print("\nMinimum Spanning Tree:")
    for u, v, weight in mst:
        print(u, "-", v, "=", weight)

    print("Minimum cost =", total)


# ==========================================================
# Built-in Demos
# ==========================================================
def demo_prims():
    print("Demo Prim's Algorithm:")
    vertices = ["A", "B", "C", "D"]
    edges = [
        ("A", "B", 5),
        ("A", "C", 4),
        ("B", "C", 10),
        ("B", "D", 6),
        ("C", "D", 8)
    ]
    print("Vertices:", vertices)
    print("Edges:", edges)
    mst, total = prims_algorithm(vertices, edges)
    print("\nMinimum Spanning Tree:")
    for u, v, weight in mst:
        print(u, "-", v, "=", weight)
    print("Minimum cost =", total)


def demo_kruskals():
    print("Demo Kruskal's Algorithm:")
    vertices = ["A", "B", "C", "D"]
    edges = [
        ("C", "D", 1),
        ("A", "D", 2),
        ("B", "D", 4),
        ("A", "B", 5),
        ("B", "C", 6)
    ]
    print("Vertices:", vertices)
    print("Edges:", edges)
    mst, total = kruskals_algorithm(vertices, edges)
    print("\nMinimum Spanning Tree:")
    for u, v, weight in mst:
        print(u, "-", v, "=", weight)
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
    print("4. Run Example / Demo Data")
    print("==========================================================")

    try:
        choice = input("Enter choice (1-4) [default: 3]: ").strip()
    except (KeyboardInterrupt, EOFError):
        print("\nExiting.")
        return

    if not choice:
        choice = "3"

    if choice == "1":
        print("\n--- 7(a) Prim's Algorithm ---")
        run_prims()
    elif choice == "2":
        print("\n--- 7(b) Kruskal's Algorithm ---")
        run_kruskals()
    elif choice == "3":
        print("\n--- 7(a) Prim's Algorithm ---")
        run_prims()
        print("\n--- 7(b) Kruskal's Algorithm ---")
        run_kruskals()
    elif choice == "4":
        print("\n--- 7(a) Prim's Algorithm (Demo) ---")
        demo_prims()
        print("\n--- 7(b) Kruskal's Algorithm (Demo) ---")
        demo_kruskals()
    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()
