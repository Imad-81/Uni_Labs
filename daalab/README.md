# DAA Lab — Advanced Data Structures & Algorithms

Comprehensive Python implementations, algorithmic explanations, step-by-step operation breakdowns, complexity analysis, and viva questions for the Design and Analysis of Algorithms (DAA) Laboratory repository (`daalab`).

---

## Table of Contents

- [Directory Structure & Quick Reference](#directory-structure--quick-reference)
- [Experiment 1: B-Tree Operations & Implementation](#experiment-1-b-tree-operations--implementation)
- [Experiment 2: Binomial Heap Implementation](#experiment-2-binomial-heap-implementation)
- [Experiment 3: Fibonacci Heap Implementation](#experiment-3-fibonacci-heap-implementation)
- [Experiment 4: Red-Black Tree Implementation](#experiment-4-red-black-tree-implementation)
- [Experiment 5: Greedy Algorithms](#experiment-5-greedy-algorithms)
- [Experiment 6: Task Scheduling & Bellman-Ford Algorithm](#experiment-6-task-scheduling--bellman-ford-algorithm)
- [Experiment 7: Minimum Spanning Tree (MST) Algorithms](#experiment-7-minimum-spanning-tree-mst-algorithms)
- [Comprehensive Time & Space Complexity Matrix](#comprehensive-time--space-complexity-matrix)
- [Viva Questions & Answers](#viva-questions--answers)

---

## Directory Structure & Quick Reference

| File | Structure / Topic | Primary Operations Covered | Time Complexity (Primary) |
|---|---|---|---|
| [`exp1.py`](file:///Users/imadmac/school/code/Uni_Labs/daalab/exp1.py) | **B-Tree** | Linear Search, Node Insert, Node Delete, Splitting & Insertion | $O(\log_t n)$ search / insert |
| [`exp2.py`](file:///Users/imadmac/school/code/Uni_Labs/daalab/exp2.py) | **Binomial Heap** | `insert`, `get_min`, `extract_min`, `union`, `merge_trees` | $O(\log n)$ insert / extract-min |
| [`exp3.py`](file:///Users/imadmac/school/code/Uni_Labs/daalab/exp3.py) | **Fibonacci Heap** | `insert`, `find_min`, `extract_min`, `consolidate`, `decrease_key`, `cut` | $O(1)$ amortized insert & decrease-key |
| [`exp4.py`](file:///Users/imadmac/school/code/Uni_Labs/daalab/exp4.py) | **Red-Black Tree** | `insert`, `fix_insert`, `left_rotate`, `right_rotate`, `search`, `inorder` | $O(\log n)$ search / insert |
| [`exp5.py`](file:///Users/imadmac/school/code/Uni_Labs/daalab/exp5.py) | **Greedy Algorithms** | Fractional Knapsack, Activity Selection, Huffman Coding | $O(n \log n)$ sorting / heap building |
| [`exp6.py`](file:///Users/imadmac/school/code/Uni_Labs/daalab/exp6.py) | **Task Scheduling & Bellman-Ford** | 6(a) Greedy task scheduling (`task_scheduling`), 6(b) Shortest path relaxation & comparison (`run_bellman_ford`) | $O(n \log n)$ scheduling / $O(1)$ path relaxation demo |
| [`exp7.py`](file:///Users/imadmac/school/code/Uni_Labs/daalab/exp7.py) | **Minimum Spanning Tree (MST)** | 7(a) Prim's Algorithm (`prims_algorithm`), 7(b) Kruskal's Algorithm (`kruskals_algorithm`) | $O(V \cdot E)$ lab / $O(E \log E)$ |

---

## Experiment 1: B-Tree Operations & Implementation

**Source File:** [`exp1.py`](file:///Users/imadmac/school/code/Uni_Labs/daalab/exp1.py)

### Overview
A **B-Tree** is a self-balancing search tree designed to work efficiently on secondary storage (disks). Unlike binary search trees, B-Tree nodes can store multiple keys and have more than two child pointers.

### Parts Breakdown

#### Part 1: B-Tree Node Search (`b_tree_node = [10, 20, 30, 40, 50]`)
- Performs a linear lookup of a key within a simulated single node.
- Complexity: $O(n)$ where $n$ is the number of keys in the node.

#### Part 2: B-Tree Node Insertion
- Finds the first position where `key < node[i]` and inserts the key using `list.insert(i, key)`, maintaining sorted order.
- If key is greater than all existing elements, it appends to the end.

#### Part 3: B-Tree Node Deletion
- Locates the key within the array and removes it using `list.pop(i)`, shifting trailing keys to keep the node compact and sorted.

#### Part 4: Full B-Tree Class Implementation (`BTree`, `BTreeNode`)
- **Node Structure (`BTreeNode`)**: `key` array, `child` array of node references, `leaf` boolean flag.
- **Minimum Degree ($t$)**: Every non-root node must contain at least $t-1$ keys and at most $2t-1$ keys.
- **Child Splitting (`split_child`)**: When a child node overflows ($2t-1$ keys), it is split around its median key (index $t-1$), promoting the median to the parent.
- **Recursive Non-Full Insertion (`insert_non_full`)**: Descends the tree, preemptively splitting full nodes along the path to ensure insertion always succeeds at the leaf level.

```
Example B-Tree Structure (t=3):
               [3]
             /     \
      [0, 1]         [4, 5]   [7, 8]
```

---

## Experiment 2: Binomial Heap Implementation

**Source File:** [`exp2.py`](file:///Users/imadmac/school/code/Uni_Labs/daalab/exp2.py)

### Overview
A **Binomial Heap** is a collection of **Binomial Trees** $B_0, B_1, B_2, \dots, B_k$ satisfying:
1. Every binomial tree in the heap obeys the **min-heap property**.
2. There is at most **one** binomial tree of any given degree.

### Key Operations & Algorithms

1. **Tree Link / Merge (`merge_trees(tree1, tree2)`)**:
   - Given two trees of degree $k$, the tree with the smaller root becomes the parent of the other tree, forming a tree of degree $k+1$ in $O(1)$ time.
2. **Heap Union (`union(other_head)`)**:
   - Merges root lists sorted by degree (`merge_heap`), then iterates through to combine trees of duplicate degree.
3. **Insertion (`insert(key)`)**:
   - Constructs a single-node binomial heap $B_0$ and unions it with the current heap in $O(\log n)$ time.
4. **Extract Minimum (`extract_min()`)**:
   - Finds the minimum root node, removes it from the root list, reverses its children to form a valid root list, and performs `union()` with the remaining heap.

```
Binomial Tree Degrees:
B0: (1 node)    B1: (2 nodes)     B2: (4 nodes)
   o               o                 o
                  /                 / \
                 o                 o   o
                                  /
                                 o
```

---

## Experiment 3: Fibonacci Heap Implementation

**Source File:** [`exp3.py`](file:///Users/imadmac/school/code/Uni_Labs/daalab/exp3.py)

### Overview
A **Fibonacci Heap** is a loose collection of heap-ordered trees using circular doubly linked lists. It defers structural consolidation until `extract_min()`, providing $O(1)$ amortized running time for `insert`, `find_min`, and `decrease_key`.

### Key Mechanics

1. **Circular Doubly Linked Lists**:
   - Node attributes `left` and `right` allow constant-time $O(1)$ splicing of nodes into and out of root/child lists.
2. **Lazy Insertion**:
   - New keys are simply attached to the root circular list; no tree restructuring occurs immediately.
3. **Consolidation (`consolidate()`)**:
   - Executed during `extract_min()`. Uses an array/hash table keyed by tree degree to link trees of equal degrees until all root trees have distinct degrees.
4. **Cut & Cascading Cut (`cut`, `cascading_cut`)**:
   - **`cut`**: Detaches a modified node from its parent (when its key decreases below parent's key) and moves it to the root list.
   - **`cascading_cut`**: If a parent has already lost a child (`mark == True`), it is also cut and moved to the root list, propagating recursively upwards. This maintains bounding properties necessary for logarithmic height.

---

## Experiment 4: Red-Black Tree Implementation

**Source File:** [`exp4.py`](file:///Users/imadmac/school/code/Uni_Labs/daalab/exp4.py)

### Overview
A **Red-Black Tree** is a self-balancing binary search tree where every node contains an extra color bit (`RED` or `BLACK`). It guarantees that no path from root to leaf is more than twice as long as any other path.

### 5 Invariant Rules
1. Every node is either **RED** or **BLACK**.
2. The root is always **BLACK**.
3. Every leaf (`NIL`) is **BLACK**.
4. If a node is **RED**, both its children must be **BLACK** (no two adjacent RED nodes).
5. For each node, all simple paths from the node to descendant leaves contain the same number of **BLACK** nodes (Black-Height).

### Insertion Fixup Cases (`fix_insert`)

When inserting a node (always colored `RED` initially), potential red-red violations are resolved based on the uncle's color:

- **Case 1 (Uncle is RED)**:
  - Recolor parent and uncle to `BLACK`, grandparent to `RED`. Move pointer $k$ to grandparent.
- **Case 2 (Uncle is BLACK, $k$ is inner child - Zig-Zag)**:
  - Apply `left_rotate` (or `right_rotate`) on parent to transform into Case 3.
- **Case 3 (Uncle is BLACK, $k$ is outer child - Zig-Zig)**:
  - Recolor parent to `BLACK`, grandparent to `RED`, then perform rotation (`right_rotate` / `left_rotate`) on grandparent.

---

## Experiment 5: Greedy Algorithms

**Source File:** [`exp5.py`](file:///Users/imadmac/school/code/Uni_Labs/daalab/exp5.py)

### Overview
Greedy algorithms construct solutions piece by piece, always choosing the next piece that offers the most immediate (locally optimal) benefit, aiming to find a global optimum.

---

### 5(a) — Part 1: Fractional Knapsack Problem

- **Strategy**: Calculate the **profit-to-weight ratio** ($P_i / W_i$) for each item and sort items in descending order of ratio.
- **Greedy Choice**: Take as much of the item with the highest value density as possible. If the remaining capacity cannot take the whole item, take the fractional portion.
- **Time Complexity**: $O(n \log n)$ due to sorting $n$ items.

```
Given: Capacity W = 50, Items: (w, p) = [(10, 60), (20, 100), (30, 120)]
Ratios: [6.0, 5.0, 4.0]
Selection: Item 1 (full: 10w, 60p) + Item 2 (full: 20w, 100p) + Item 3 (20/30 frac: 20w, 80p)
Total Profit = 240.0
```

---

### 5(a) — Part 2: Activity Selection Problem

- **Strategy**: Given start times $S$ and finish times $F$ for $n$ activities, select the maximum number of mutually compatible activities.
- **Greedy Choice**: Sort activities by **finish time** in ascending order. Always pick the activity with the earliest finish time that starts after or when the previous activity ends.
- **Time Complexity**: $O(n \log n)$ for sorting finish times ($O(n)$ if already sorted).

```
Activities (Finish, Start): [(2, 1), (4, 3), (6, 0), (7, 5), (9, 8), (9, 5)]
Selected: Activity 1 [1-2], Activity 2 [3-4], Activity 4 [5-7], Activity 5 [8-9]
Maximum Activities = 4
```

---

### 5(b) — Huffman Coding & Complexity Analysis

- **Strategy**: A lossless data compression algorithm that assigns variable-length prefix codes to characters based on their frequencies.
- **Greedy Choice**: Use a **Min-Heap (Priority Queue)**. Repeatedly extract the two nodes with the lowest frequencies, combine them into an internal parent node with frequency sum, and insert the parent back into the heap.
- **Prefix Property**: No code is a prefix of another code, ensuring unambiguous decoding.

#### Time & Space Complexity Analysis:
- **Building the Min-Heap**: $O(n)$
- **Extracting minimums & inserting ($n-1$ iterations)**: Each step takes $O(\log n)$, so tree construction takes $O(n \log n)$.
- **Generating Codes (Tree Traversal)**: $O(n)$
- **Overall Time Complexity**: $O(n \log n)$
- **Auxiliary Space Complexity**: $O(n)$ to store tree nodes and heap.

---

## Experiment 6: Task Scheduling & Bellman-Ford Algorithm

**Source File:** [`exp6.py`](file:///Users/imadmac/school/code/Uni_Labs/daalab/exp6.py)

The script provides an interactive CLI runner (`main()`) to execute either experiment individually or both sequentially:
1. `6(a)` — Task Scheduling Problem (Greedy Approach)
2. `6(b)` — Bellman-Ford Algorithm (Shortest Path Demonstration)
3. Run Both Experiments

---

### 6(a) Task Scheduling Problem (Greedy Approach)

#### Overview
The **Task Scheduling Problem** (also referred to as **Interval Scheduling**) involves scheduling the maximum number of compatible tasks on a single execution resource (e.g., a single CPU or a shared resource). Each task $i$ has an index, a start time $s_i$, and a finish time $f_i$ ($s_i < f_i$). Two tasks $i$ and $j$ are mutually compatible if their execution intervals do not overlap ($s_j \ge f_i$ or $s_i \ge f_j$).

#### Algorithmic Workflow & Mechanics

1. **User Input Gathering**:
   - Reads the total count of tasks $n$.
   - Iteratively prompts the user for each task's start time and finish time.
   - Stores each task as a tuple: `(task_number, start_time, finish_time)`.
2. **Earliest Finish Time (EFT) Sorting**:
   - Sorts the tasks in ascending order of their completion/finish times:
     ```python
     tasks.sort(key=lambda x: x[2])
     ```
   - **Greedy Choice Invariant:** Choosing the task that finishes first leaves the largest feasible window of free time to accommodate subsequent tasks.
3. **Greedy Schedule Decision (`task_scheduling`)**:
   - Maintains a pointer `previous_finish` initialized to `0`.
   - Traverses each task in sorted order:
     - **Condition met (`start_time >= previous_finish`)**: The task is scheduled, printed with its start and finish time, and `previous_finish` is updated to `finish_time`.
     - **Overlap detected (`start_time < previous_finish`)**: The task is rejected, reporting that it conflicts with the previously scheduled task.

#### Step-by-Step Execution Trace

```text
Interactive Input:
Task 1: Start = 1, Finish = 3
Task 2: Start = 2, Finish = 5
Task 3: Start = 4, Finish = 7
Task 4: Start = 1, Finish = 8
Task 5: Start = 5, Finish = 9
Task 6: Start = 8, Finish = 10

Sorted by Finish Time (x[2]):
[Task 1 (1, 3), Task 2 (2, 5), Task 3 (4, 7), Task 4 (1, 8), Task 5 (5, 9), Task 6 (8, 10)]

Decision Flow:
• Task 1: start (1) >= prev (0)  -> SCHEDULED.    New prev = 3.
• Task 2: start (2) <  prev (3)  -> NOT SCHEDULED (overlaps with Task 1).
• Task 3: start (4) >= prev (3)  -> SCHEDULED.    New prev = 7.
• Task 4: start (1) <  prev (7)  -> NOT SCHEDULED (overlaps with Task 3).
• Task 5: start (5) <  prev (7)  -> NOT SCHEDULED (overlaps with Task 3).
• Task 6: start (8) >= prev (7)  -> SCHEDULED.    New prev = 10.

Total Scheduled Tasks: 3 (Task 1, Task 3, Task 6)
```

#### Complexity Analysis

- **Time Complexity**:
  - **Input Collection**: $O(n)$ for reading $n$ tasks.
  - **Sorting**: $O(n \log n)$ via Python's Timsort on task finish times.
  - **Greedy Linear Selection**: $O(n)$ single-pass iteration comparing start time with previous finish time.
  - **Overall Time Complexity**: $O(n \log n)$
- **Space Complexity**:
  - **Auxiliary Space**: $O(n)$ to hold the list of $n$ task tuples in memory.

---

### 6(b) Bellman-Ford Algorithm (Shortest Path Demonstration)

#### Overview
The **Bellman-Ford Algorithm** solves the Single-Source Shortest Path (SSSP) problem on directed/undirected weighted graphs, correctly handling graphs with negative edge weights and detecting negative weight cycles. 

In this lab module (`run_bellman_ford`), a canonical multi-path network between vertices $A, B, C, D$ is evaluated:
- **Path 1**: $\text{Source} \to B \to \text{Destination}$ with cumulative weight $w(\text{Source}, B) + w(B, \text{Destination})$
- **Path 2**: $\text{Source} \to C \to \text{Destination}$ with cumulative weight $w(\text{Source}, C) + w(C, \text{Destination})$

The program relaxes the two paths, compares their total accumulated distances, and outputs the optimal shortest path and its corresponding distance.

#### Step-by-Step Execution Trace

```text
Vertices: A, B, C, D
Source: A, Destination: D

Path 1: A -> B -> D (Weight AB = 4, Weight BD = 2) => Distance = 6
Path 2: A -> C -> D (Weight AC = 1, Weight CD = 8) => Distance = 9

Comparison: Distance(Path 1) < Distance(Path 2) => 6 < 9
Shortest Path: A -> B -> D
Shortest Distance: 6
```

#### Complexity Analysis

- **General Bellman-Ford Algorithm**:
  - **Time Complexity**: $O(V \cdot E)$ where $V$ is the number of vertices and $E$ is the number of edges ($|V|-1$ relaxation passes over all $E$ edges).
  - **Space Complexity**: $O(V)$ for the distance array and predecessor pointers.
- **Lab 6(b) Demo Implementation**:
  - **Time Complexity**: $O(1)$ constant time evaluation of the two candidate routes.
  - **Space Complexity**: $O(1)$ constant auxiliary space.

---

## Experiment 7: Minimum Spanning Tree (MST) Algorithms

**Source File:** [`exp7.py`](file:///Users/imadmac/school/code/Uni_Labs/daalab/exp7.py)

The script provides an interactive CLI runner (`main()`) to execute either experiment individually or both sequentially:
1. `7(a)` — Prim's Algorithm (Minimum Spanning Tree)
2. `7(b)` — Kruskal's Algorithm (Minimum Spanning Tree)
3. Run Both Experiments (Interactive)

---

### Minimum Spanning Tree (MST) Fundamentals

Given a connected, undirected, weighted graph $G = (V, E)$, a **Spanning Tree** is an acyclic subgraph connecting all $|V|$ vertices with exactly $|V| - 1$ edges. A **Minimum Spanning Tree (MST)** is a spanning tree whose cumulative edge weight is minimized:

$$w(T) = \sum_{(u, v) \in T} w(u, v) \quad \text{is minimal}$$

Both Prim's and Kruskal's algorithms are **Greedy Algorithms** governed by the **Cut Property**:
> **Cut Property:** For any cut $(S, V \setminus S)$ of a connected graph $G$, the minimum weight edge crossing the cut belongs to an MST.

---

### 7(a) Prim's Algorithm

#### Overview
**Prim's Algorithm** grows a single Minimum Spanning Tree outward starting from an arbitrary initial vertex $v_0$. At each step, it identifies all candidate cross-edges connecting the currently spanned vertices ($S$) to the remaining unvisited vertices ($V \setminus S$) and greedily selects the minimum weight edge, adding the newly discovered vertex into $S$.

#### Algorithmic Workflow & Mechanics

1. **Graph Input Gathering**:
   - Reads the total number of vertices $n$ and their string labels (e.g., `A B C D`).
   - Reads the total count of edges $e$.
   - Prompts for each undirected edge in `u-v` format and its integer weight $w$.
   - Stores each edge as a tuple `(u, v, weight)`.
2. **Initialization**:
   - Spanning set `selected = [vertices[0]]` starts with the first vertex.
   - Initializes empty MST edge list `mst = []` and `total = 0`.
3. **Iterative Cut Relaxation (`prims_algorithm`)**:
   - Loops while `len(selected) < n`:
     - Initializes `minimum = 999999` and `best = None`.
     - Scans all edges $(u, v, w)$:
       - If $u \in \text{selected}$ and $v \notin \text{selected}$ with $w < \text{minimum}$, records candidate edge $(u, v, w)$.
       - If $v \in \text{selected}$ and $u \notin \text{selected}$ with $w < \text{minimum}$, records candidate edge $(v, u, w)$.
     - If no connecting edge is found, reports that the graph is disconnected and halts.
     - Adds the newly reached vertex $v$ to `selected`.
     - Appends the chosen edge to `mst` and adds its weight to `total`.
4. **Display Output**:
   - Prints all edges selected in the MST and the total minimum cost.

#### Step-by-Step Execution Trace

```text
Vertices: A, B, C, D (n = 4)
Edges:
A-B = 5
A-C = 4
B-C = 10
B-D = 6
C-D = 8

Start Vertex: A (selected = [A])

Iteration 1:
- Candidate cross-edges from {A} to {B, C, D}:
  • A-B (weight 5)
  • A-C (weight 4)  <-- Minimum
- Select edge: A - C = 4
- selected = [A, C], MST = [A-C (4)], total = 4

Iteration 2:
- Candidate cross-edges from {A, C} to {B, D}:
  • A-B (weight 5)  <-- Minimum
  • C-D (weight 8)
- Select edge: A - B = 5
- selected = [A, C, B], MST = [A-C (4), A-B (5)], total = 9

Iteration 3:
- Candidate cross-edges from {A, C, B} to {D}:
  • B-D (weight 6)  <-- Minimum
  • C-D (weight 8)
- Select edge: B - D = 6
- selected = [A, C, B, D], MST = [A-C (4), A-B (5), B-D (6)], total = 15

Output:
Minimum Spanning Tree:
A - C = 4
A - B = 5
B - D = 6
Minimum cost = 15
```

#### Complexity Analysis

- **Time Complexity**:
  - **Lab Implementation**: At each of the $V - 1$ iterations, the algorithm iterates over all $E$ edges to find the minimum cross-edge. Total time is $O(V \cdot E)$.
  - **Standard Priority Queue (Min-Heap)**: $O(E \log V)$ with adjacency list and binary heap.
  - **Fibonacci Heap**: $O(E + V \log V)$ optimal for dense graphs.
- **Space Complexity**:
  - **Auxiliary Space**: $O(V + E)$ to store vertex labels, edge tuples, and the MST list.

---

### 7(b) Kruskal's Algorithm

#### Overview
**Kruskal's Algorithm** is an edge-based greedy algorithm that builds an MST by sorting all edges in the entire graph in non-decreasing order of weight. It iterates through the sorted edge list, greedily adding an edge if and only if it does not form a cycle with previously selected edges. Cycle detection is accomplished via the **Disjoint Set Union (DSU / Union-Find)** data structure.

#### Algorithmic Workflow & Mechanics

1. **Edge Sorting**:
   - Sorts all graph edges in ascending order of their weights:
     ```python
     edges_sorted = sorted(edges, key=lambda x: x[2])
     ```
2. **Disjoint Set Initialization**:
   - Each vertex starts in its own individual component / set:
     ```python
     parent = {v: v for v in vertices}
     ```
3. **Cycle Detection & Set Union (`find`)**:
   - For each edge $(u, v, w)$ in ascending order:
     - Finds the representative root of vertex $u$: `parent_u = find(u)`
     - Finds the representative root of vertex $v$: `parent_v = find(v)`
     - **Safe Edge Condition (`parent_u != parent_v`)**: Vertices belong to different connected components. Adding this edge will **not** create a cycle.
       - Edge is appended to `mst`.
       - Edge weight is added to `total`.
       - Sets are merged (union): `parent[parent_u] = parent_v`.
     - **Cycle Detected (`parent_u == parent_v`)**: Both vertices are already connected in the same component. The edge is discarded.
4. **Termination**:
   - Halts immediately when `len(mst) == n - 1` (since any spanning tree on $n$ vertices contains exactly $n-1$ edges).

#### Step-by-Step Execution Trace

```text
Vertices: A, B, C, D (n = 4)
Input Edges: C-D (1), A-D (2), B-D (4), A-B (5), B-C (6)

Sorted Edge List:
1. (C, D, 1)
2. (A, D, 2)
3. (B, D, 4)
4. (A, B, 5)
5. (B, C, 6)

Initial Parents: {A: A, B: B, C: C, D: D}

Step 1: Edge (C, D, weight 1)
- find(C) = C, find(D) = D (C != D) -> NO CYCLE
- Add C - D = 1 to MST
- Union: parent[C] = D
- Sets: {A}, {B}, {C, D}
- MST count: 1, Total: 1

Step 2: Edge (A, D, weight 2)
- find(A) = A, find(D) = D (A != D) -> NO CYCLE
- Add A - D = 2 to MST
- Union: parent[A] = D
- Sets: {B}, {A, C, D}
- MST count: 2, Total: 3

Step 3: Edge (B, D, weight 4)
- find(B) = B, find(D) = D (B != D) -> NO CYCLE
- Add B - D = 4 to MST
- Union: parent[B] = D
- Sets: {A, B, C, D}
- MST count: 3 (equals n - 1 = 3) -> BREAK!
- Edges (A-B, 5) and (B-C, 6) are skipped.

Output:
Minimum Spanning Tree:
C - D = 1
A - D = 2
B - D = 4
Minimum cost = 7
```

#### Complexity Analysis

- **Time Complexity**:
  - **Edge Sorting**: $O(E \log E) = O(E \log V)$ (since $E \le V^2$, $\log E \le 2 \log V$).
  - **Union-Find Operations**: With $E$ edge queries, simple path traversal takes $O(E \cdot V)$ worst-case; with path compression and rank heuristics, it runs in nearly linear $O(E \cdot \alpha(V))$.
  - **Overall Time Complexity**: $O(E \log E) = O(E \log V)$, dominated by the sorting stage.
- **Space Complexity**:
  - **Auxiliary Space**: $O(V)$ for the parent dictionary + $O(E)$ for edge storage = $O(V + E)$.

---

### Prim's vs. Kruskal's Comparative Analysis

| Feature | Prim's Algorithm | Kruskal's Algorithm |
|---|---|---|
| **Strategy** | Grows a single tree vertex-by-vertex from a start node | Grows a forest by adding edges in global sorted order |
| **Primary Data Structure** | Min-Heap / Priority Queue or candidate list | Disjoint Set Union (DSU / Union-Find) & Edge List |
| **Cycle Prevention** | Never adds a vertex already in the selected set | Checks if edge endpoints belong to the same component (`find`) |
| **Graph Suitability** | **Dense Graphs** ($E \approx V^2$): $O(V^2)$ or $O(E + V \log V)$ | **Sparse Graphs** ($E \ll V^2$): $O(E \log V)$ |
| **Disconnected Graphs** | Traverses only the component containing the starting vertex | Computes a **Minimum Spanning Forest (MSF)** across all components |
| **Edge Sorting Required** | No global sort needed | Yes, requires sorting all $E$ edges upfront |

---

## Comprehensive Time & Space Complexity Matrix

| Structure / Algorithm | Search / Find Min | Insert (Worst Case) | Insert (Amortized) | Extract Min / Delete | Overall Time Complexity | Space Complexity |
|---|---|---|---|---|---|---|
| **B-Tree ($t$)** | $O(\log n)$ | $O(\log n)$ | $O(\log n)$ | $O(\log n)$ | $O(\log n)$ | $O(n)$ |
| **Binomial Heap** | $O(\log n)$ | $O(\log n)$ | $O(1)$ | $O(\log n)$ | $O(\log n)$ | $O(n)$ |
| **Fibonacci Heap** | $O(1)$ | $O(1)$ | $O(1)$ | $O(\log n)$ amortized | $O(1)$ amortized | $O(n)$ |
| **Red-Black Tree** | $O(\log n)$ | $O(\log n)$ | $O(\log n)$ | $O(\log n)$ | $O(\log n)$ | $O(n)$ |
| **Fractional Knapsack** | N/A | N/A | N/A | N/A | $O(n \log n)$ | $O(n)$ |
| **Activity Selection** | N/A | N/A | N/A | N/A | $O(n \log n)$ | $O(n)$ |
| **Huffman Coding** | N/A | $O(\log n)$ | $O(\log n)$ | $O(\log n)$ | $O(n \log n)$ | $O(n)$ |
| **Task Scheduling (Greedy 6a)** | N/A | N/A | N/A | N/A | $O(n \log n)$ | $O(n)$ |
| **Bellman-Ford (SSSP 6b Demo)** | N/A | N/A | N/A | N/A | $O(1)$ demo / $O(V \cdot E)$ gen | $O(1)$ demo / $O(V)$ gen |
| **Prim's Algorithm (MST 7a)** | N/A | N/A | N/A | N/A | $O(V \cdot E)$ lab / $O(E \log V)$ heap | $O(V + E)$ |
| **Kruskal's Algorithm (MST 7b)** | N/A | N/A | N/A | N/A | $O(E \log E) = O(E \log V)$ | $O(V + E)$ |

---

## Viva Questions & Answers

### Q1: Why does Greedy work for Fractional Knapsack but fail for 0/1 Knapsack?
Fractional Knapsack allows breaking items; taking the item with the highest profit density ($P/W$) leaves the remaining capacity optimal. In 0/1 Knapsack, taking a high-density item might leave empty space that cannot be filled, so Dynamic Programming is required.

### Q2: Why must activities be sorted by finish time rather than start time or duration?
Sorting by earliest finish time leaves the maximum possible remaining time for subsequent activities. Sorting by start time or duration can block longer optimal activity schedules.

### Q3: What is the Prefix Rule in Huffman Coding and why is it crucial?
The prefix rule states that no character's codeword can be a prefix of another character's codeword. This enables unambiguous left-to-right decoding without separators/delimiters.

### Q4: What is the time complexity of Huffman Coding if characters are already sorted by frequency?
If frequencies are pre-sorted, we can maintain two standard queues (one for initial leaf nodes and one for combined internal nodes), allowing tree construction in linear $O(n)$ time.

### Q5: What makes B-Trees ideal for File Systems and Database Systems?
B-Trees have large branching factors (high degree $t$). This keeps the height of the tree small, minimizing the number of disk accesses required to find a record. Entire B-Tree nodes can be aligned with disk block sizes.

### Q6: Why are new nodes in a Red-Black Tree always inserted as RED?
Inserting a RED node preserves Rule 5 (Black-Height invariant) across all paths. Inserting a BLACK node would immediately violate black-height on that branch and require complex global updates.

### Q7: What is the purpose of the `mark` field in Fibonacci Heap nodes?
The `mark` boolean indicates whether a node has lost a child since it became a child of its current parent. It triggers a **cascading cut** when a second child is lost, preventing trees from becoming excessively deep and preserving $O(1)$ amortized efficiency.

### Q8: Why does the Earliest Finish Time (EFT) greedy strategy guarantee an optimal solution for task/interval scheduling?
By mathematical induction ("Greedy Stays Ahead" proof): Let the greedy schedule select activities $i_1, i_2, \dots, i_k$ and an optimal schedule select $j_1, j_2, \dots, j_m$. By definition of the greedy choice, $f(i_1) \le f(j_1)$. Substituting $i_1$ for $j_1$ keeps all remaining activities in the optimal schedule compatible. Repeating this establishes that the greedy schedule finishes each step at or before the optimal schedule, proving $k = m$ (optimality).

### Q9: What is the difference between Interval Scheduling (`exp6.py`) and Interval Partitioning (Minimum Machine Scheduling)?
- **Interval Scheduling** aims to find the **maximum number of mutually compatible tasks** on a single machine/resource ($O(n \log n)$ by sorting finish times).
- **Interval Partitioning** aims to schedule **all given tasks** using the **minimum number of machines/processors** such that no two overlapping tasks run on the same machine (solved greedily by sorting start times and managing active machines with a min-heap in $O(n \log n)$ time).

### Q10: How does Bellman-Ford handle negative weight edges and detect negative cycles?
Unlike Dijkstra's algorithm (which fails on negative edges due to greedy finality), Bellman-Ford relaxes all $|E|$ edges $|V|-1$ times. If a further relaxation in the $|V|$-th pass still yields a shorter distance (`dist[u] + weight < dist[v]`), it proves the graph contains a negative-weight cycle reachable from the source.

### Q11: What is the fundamental difference in approach between Prim's and Kruskal's algorithms?
- **Prim's algorithm** is **vertex-centric** and grows a single tree continuously starting from an arbitrary root, always adding the cheapest edge crossing the cut between visited and unvisited vertices.
- **Kruskal's algorithm** is **edge-centric** and considers edges in globally sorted order, adding edges that connect different disjoint components (growing a forest until it merges into a single tree).

### Q12: What is the "Cut Property" and why does it guarantee the correctness of greedy MST algorithms?
The Cut Property states that for any partition of the graph's vertices into two disjoint sets $S$ and $V \setminus S$, the lightest edge crossing the cut must belong to some MST. If we assume an MST $T$ does not include this minimum cross-edge $e$, adding $e$ to $T$ creates a cycle containing another edge $e'$ crossing the same cut. Since $w(e) \le w(e')$, replacing $e'$ with $e$ yields a spanning tree of equal or lesser weight, proving optimality.

### Q13: Why is Kruskal's algorithm generally preferred for sparse graphs while Prim's is preferred for dense graphs?
- In **sparse graphs** ($E \approx V$), Kruskal's sorting step takes $O(E \log E) \approx O(V \log V)$, which is extremely fast, and disjoint-set operations have virtually constant amortized cost.
- In **dense graphs** ($E \approx V^2$), Kruskal sorts $O(V^2)$ edges ($O(V^2 \log V)$), whereas Prim's algorithm using an adjacency matrix or Fibonacci heap runs in $O(V^2)$ or $O(E + V \log V)$, avoiding the cost of sorting all $O(V^2)$ edges.

### Q14: What happens if all edge weights in a connected undirected graph are unique?
If all edge weights in the graph are distinct, the Minimum Spanning Tree is **strictly unique**. Both Prim's and Kruskal's algorithms will discover the exact same tree regardless of tie-breaking or starting vertex.

### Q15: How does Kruskal's algorithm detect cycles, and what is the role of Union-Find?
Kruskal's algorithm maintains a Disjoint Set Union (DSU) structure where each connected component is a disjoint set represented by a root. For an edge $(u, v)$, it queries `find(u)` and `find(v)`. If `find(u) == find(v)`, both vertices already belong to the same component, so adding the edge would close a cycle. If they differ, the edge is safe to add, and `union(u, v)` merges the two components.

---

*Prepared for DAA Laboratory — Unit Experiments 1–7*