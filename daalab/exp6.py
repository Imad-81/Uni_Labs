# Experiment 6:
# 6(a) - Task Scheduling Problem (Greedy Approach)
# 6(b) - Bellman-Ford Algorithm (Shortest Path)


# ==========================================================
# 6(a) - Task Scheduling Problem
# ==========================================================
def task_scheduling(tasks):
    print("\nTASK SCHEDULE PROBLEM")
    print("-----------------------")

    previous_finish = 0

    for task in tasks:
        task_number = task[0]
        start_time = task[1]
        finish_time = task[2]

        if start_time >= previous_finish:
            print("Task", task_number, "is scheduled.")
            print("Start Time:", start_time)
            print("Finish Time:", finish_time)

            previous_finish = finish_time

        else:
            print("Task", task_number, "is not scheduled.")
            print("Reason: It overlaps with the previous task.")

        print()


def run_task_scheduling():
    # Take input from user
    n = int(input("Enter the number of tasks: "))

    tasks = []

    for i in range(n):
        print("\nEnter details of Task", i + 1)

        start_time = int(input("Enter the start time: "))
        finish_time = int(input("Enter the finish time: "))

        tasks.append((i + 1, start_time, finish_time))

    # Sort tasks according to finish time
    tasks.sort(key=lambda x: x[2])

    # Call the function
    task_scheduling(tasks)


# ==========================================================
# 6(b) - Bellman-Ford Algorithm
# ==========================================================
def run_bellman_ford():
    # Display the vertices.
    print("Vertices: A, B, C, D")

    # Ask the student to enter the number of edges.
    number_of_edges = int(input("Enter number of edges: "))

    # Ask the student to enter the starting vertex.
    source = input("Enter starting vertex: ").strip().upper()

    # Ask the student to enter the ending vertex.
    destination = input("Enter ending vertex: ").strip().upper()

    # Display the possible paths from A to D.
    print("\nTwo possible paths are:")

    # Display the first possible path.
    print("Path 1:", source, "- B -", destination)

    # Display the second possible path.
    print("Path 2:", source, "- C -", destination)

    # Ask the student to enter the weight of the first edge of Path 1.
    weight_ab = int(input("\nEnter the weight of " + source + "-B: "))

    # Ask the student to enter the weight of the second edge of Path 1.
    weight_bd = int(input("Enter the weight of B-" + destination + ": "))

    # Calculate the total weight of Path 1.
    path1_distance = weight_ab + weight_bd

    # Ask the student to enter the weight of the first edge of Path 2.
    weight_ac = int(input("\nEnter the weight of " + source + "-C: "))

    # Ask the student to enter the weight of the second edge of Path 2.
    weight_cd = int(input("Enter the weight of C-" + destination + ": "))

    # Calculate the total weight of Path 2.
    path2_distance = weight_ac + weight_cd

    # Compare the two path distances.
    if path1_distance < path2_distance:

        # Store Path 1 as the shortest path.
        shortest_path = source + " -> B -> " + destination

        # Store the distance of Path 1.
        shortest_distance = path1_distance

    # Check if Path 2 is shorter.
    elif path2_distance < path1_distance:

        # Store Path 2 as the shortest path.
        shortest_path = source + " -> C -> " + destination

        # Store the distance of Path 2.
        shortest_distance = path2_distance

    # If both paths have the same distance.
    else:

        # Store both paths as shortest paths.
        shortest_path = source + " -> B -> " + destination + " and " + source + " -> C -> " + destination

        # Store the common shortest distance.
        shortest_distance = path1_distance

    # Display the Bellman-Ford heading.
    print("\nBELLMAN-FORD ALGORITHM")

    # Display a separator line.
    print("----------------------")

    # Display the starting vertex.
    print("Starting Vertex  :", source)

    # Display the ending vertex.
    print("Ending Vertex    :", destination)

    # Display the shortest path.
    print("Shortest Path    :", shortest_path)

    # Display the shortest distance.
    print("Shortest Distance:", shortest_distance)


# ==========================================================
# Main Interactive Runner
# ==========================================================
def main():
    print("==========================================================")
    print("  EXPERIMENT 6: DAA LAB")
    print("==========================================================")
    print("1. 6(a) - Task Scheduling Problem (Greedy Approach)")
    print("2. 6(b) - Bellman-Ford Algorithm")
    print("3. Run Both Experiments (Interactive)")
    print("==========================================================")

    choice = input("Enter choice (1-3) [default: 3]: ").strip()
    if not choice:
        choice = "3"

    if choice in ["1", "3"]:
        print("\n--- 6(a) Task Scheduling Problem ---")
        run_task_scheduling()

    if choice in ["2", "3"]:
        print("\n--- 6(b) Bellman-Ford Algorithm ---")
        run_bellman_ford()


if __name__ == "__main__":
    main()