# Experiment 8: Simple Hash Table Implementation

**Aim:** To implement a basic Hash Table for product management focusing on fundamental hashing and collision resolution.

**Algorithm:**
1. **Hash Function**: Uses the length of the product name as the key for hashing.
2. **Add Product**:
   - Compute the hash index.
   - If a collision occurs, append to the chain at that index.
   - If the key exists, update the product information.
3. **Rehashing**:
   - If the load factor exceeds 0.7, the table size is doubled.
   - All entries are re-distributed into the new, larger table.
4. **Search**: Find a product by its name using the hash index.

**Key Features:**
- Demonstrates basic chaining for collision resolution.
- Illustrates the concept of load-factor-triggered resizing.
- Simple hash function based on key length.
