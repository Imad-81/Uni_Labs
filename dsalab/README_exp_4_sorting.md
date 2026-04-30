# Experiment 4: Product Sorting System

**Aim:** To implement a Python program that sorts a collection of products based on various criteria such as price, popularity, and alphabetical order.

**Algorithm:**
1. Define a `Product` class with `name`, `price`, and `popularity` attributes.
2. Implement a `sort_products` function that takes a list of products and a sorting criterion.
3. Use Python's built-in `sorted()` function with custom `lambda` keys to perform sorting:
   - **Price**: Sort by the `price` attribute.
   - **Popularity**: Sort by the `popularity` attribute.
   - **Alphabetical**: Sort by the `name` attribute.
4. Display the original and sorted lists to verify the results.

**Key Features:**
- Dynamic sorting criteria selection.
- Object-oriented approach using the `Product` class.
- Efficient sorting using Timsort (Python's default `sorted` implementation).
