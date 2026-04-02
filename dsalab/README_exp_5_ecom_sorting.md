# Experiment 5: E-commerce Product Sorting

**Aim:** To develop a Python program that efficiently sorts a list of products based on multi-criteria: price, popularity, and alphabetical order.

**Algorithm:**
1. Define a `Product` class to encapsulate attributes like name, price, and popularity.
2. Implement **Merge Sort**, a divide-and-conquer algorithm ($O(n \log n)$).
3. **Divide**: Recursively split the list into two halves until single-element sublists remain.
4. **Conquer**: Merge the sublists back together in the desired order (ascending/descending).
5. Use `getattr()` to dynamically access product attributes based on the sorting criteria.

**Output:**
--- Products Sorted by Popularity (High to Low) ---
Product(name='Laptop', price=$1200, popularity=4.8 stars)
Product(name='Smartwatch', price=$250, popularity=4.7 stars)
Product(name='Smartphone', price=$800, popularity=4.5 stars)
Product(name='Tablet', price=$600, popularity=4.3 stars)
Product(name='Headphones', price=$150, popularity=4.2 stars)
Product(name='Bluetooth Speaker', price=$100, popularity=4.1 stars)

--- Products Sorted by Name (Alphabetical) ---
Product(name='Bluetooth Speaker', price=$100, popularity=4.1 stars)
Product(name='Headphones', price=$150, popularity=4.2 stars)
Product(name='Laptop', price=$1200, popularity=4.8 stars)
Product(name='Smartphone', price=$800, popularity=4.5 stars)
Product(name='Smartwatch', price=$250, popularity=4.7 stars)
Product(name='Tablet', price=$600, popularity=4.3 stars)
