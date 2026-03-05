# Experiment 4: Ticketing System using Priority Queue

## Objective
To design and implement a simple ticketing system for a customer support department that handles inquiries in a first-come-first-served (FCFS) manner, while prioritizing urgent issues using a **Priority Queue**.

## Core Concepts Used

### 1. Queue (First-In-First-Out)
A basic queue follows the **FIFO** principle: the first element added is the first one removed. In this ticketing system, if all tickets had the same priority, it would behave like a standard queue.

### 2. Priority Queue
A Priority Queue is an abstract data type where each element has a "priority" associated with it. Elements with higher priority are served before elements with lower priority. 
- In our implementation, we used:
    - **Priority 1**: Urgent
    - **Priority 2**: Normal
    - **Priority 3**: Low

### 3. Heap Data Structure
Python's `heapq` module implement a **Min-Heap**. 
- In a Min-Heap, the smallest element is always at the root (index 0).
- Since we assigned `1` to Urgent and `3` to Low, the Min-Heap naturally processes "1" before "3".

### 4. Maintaining FCFS for Equal Priorities
To ensure that two tickets with the same priority are processed in the order they arrived (FCFS), we used a **timestamp**.
- The `Ticket` class stores `time.time()`.
- The comparison logic (`__lt__`) first checks the priority. If priorities are equal, it compares timestamps.

### 5. Implementation Details (Python)
- **`heapq.heappush(list, item)`**: Adds a ticket to the heap while maintaining the heap property.
- **`heapq.heappop(list)`**: Removes and returns the smallest (highest priority) item.
- **`__lt__` (Less Than Magic Method)**: Customizes how Python compares two `Ticket` objects, which is critical for the heap to know which ticket comes "first".

## Logic Flow
1. **Submit**: Create a `Ticket` object with Name, Issue, Priority, and Timestamp. Push to Heap.
2. **Display**: Sort the heap temporarily and print pending tickets.
3. **Process**: Pop the root of the heap (highest priority/oldest) and mark as resolved.

## Conclusion
By combining a Heap (for priority) and a Timestamp (for FCFS), we created an efficient system that balances urgency with fairness.
