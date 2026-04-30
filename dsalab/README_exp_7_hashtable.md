# Experiment 7: Hash Table with Chaining and Rehashing

**Aim:** To implement a robust Hash Table data structure that handles collisions using chaining and maintains performance via dynamic rehashing.

**Algorithm:**
1. **Hash Function**: Calculate the sum of ASCII values of the product name and take the modulo with the table size.
2. **Collision Handling**: Use **Chaining** (linked lists/arrays in each bucket) to store multiple items with the same hash index.
3. **Insertion**: Add new products to the appropriate bucket. Update the price if the product already exists.
4. **Dynamic Rehashing**:
   - Monitor the **Load Factor** (number of items / table size).
   - If the load factor exceeds a threshold (e.g., 0.7), double the table size and re-insert all existing elements.
5. **Search**: Quickly locate products using the hash function.

**Key Features:**
- Dynamic table resizing (Rehashing).
- Efficient collision management.
- Load factor monitoring for performance optimization.
