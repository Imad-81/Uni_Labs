"""
E-commerce Product Sorting System
Demonstrates Merge Sort for organizing products by price, popularity, or name.
"""

class Product:
    def __init__(self, name, price, popularity):
        self.name = name
        self.price = price
        self.popularity = popularity  # Higher index means more popular

    def __repr__(self):
        return f"Product(name='{self.name}', price=${self.price}, popularity={self.popularity} stars)"

def merge_sort(product_list, attribute):
    """
    Sorts a list of Product objects based on the specified attribute.
    Complexity: O(n log n)
    """
    if len(product_list) <= 1:
        return product_list

    mid = len(product_list) // 2
    left_half = merge_sort(product_list[:mid], attribute)
    right_half = merge_sort(product_list[mid:], attribute)

    return merge(left_half, right_half, attribute)

def merge(left, right, attribute):
    sorted_list = []
    i = j = 0

    while i < len(left) and j < len(right):
        # Using getattr to dynamically access the specified attribute
        if getattr(left[i], attribute) <= getattr(right[j], attribute):
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list

def display_products(products, header):
    print(f"\n--- {header} ---")
    for product in products:
        print(product)

def main():
    # Sample product data
    products = [
        Product("Laptop", 1200, 4.8),
        Product("Smartphone", 800, 4.5),
        Product("Headphones", 150, 4.2),
        Product("Smartwatch", 250, 4.7),
        Product("Tablet", 600, 4.3),
        Product("Bluetooth Speaker", 100, 4.1)
    ]

    display_products(products, "Original Product List")

    # Sort by Price
    price_sorted = merge_sort(products, 'price')
    display_products(price_sorted, "Products Sorted by Price (Low to High)")

    # Sort by Popularity
    popularity_sorted = merge_sort(products, 'popularity')
    # Note: merge_sort by default is ascending. For popularity, descending might be preferred.
    # We can reverse it or modify the comparison in merge.
    display_products(popularity_sorted[::-1], "Products Sorted by Popularity (High to Low)")

    # Sort by Name (Alphabetical)
    name_sorted = merge_sort(products, 'name')
    display_products(name_sorted, "Products Sorted by Name (Alphabetical)")

if __name__ == "__main__":
    main()
