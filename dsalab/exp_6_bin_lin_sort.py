class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"({self.name}, ${self.price})"


def linear_search(products, target_name):
    """Traverses the list one by one to find the product name."""
    for index, product in enumerate(products):
        if product.name.lower() == target_name.lower():
            return index
    return -1


def binary_search(products, target_name):
    """Sorts the list by name and performs binary search."""
    # Algorithm step 5: Sort list based on name
    sorted_products = sorted(products, key=lambda x: x.name.lower())
    
    low = 0
    high = len(sorted_products) - 1
    target_name = target_name.lower()

    while low <= high:
        mid = (low + high) // 2
        mid_name = sorted_products[mid].name.lower()

        if mid_name == target_name:
            return mid, sorted_products # Return index in sorted list and the list itself
        elif mid_name < target_name:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1, sorted_products


def main():
    # Initial list of products
    products = [
        Product("Laptop", 1200),
        Product("Smartphone", 800),
        Product("Headphones", 150),
        Product("Mouse", 25),
        Product("Keyboard", 75)
    ]

    print("--- Experiment 6: Linear and Binary Search ---")
    print(f"Original Products: {products}")

    # Step 6: Input product name to search
    query = input("\nEnter product name to search: ")

    # Step 7: Apply Linear Search
    lin_index = linear_search(products, query)
    if lin_index != -1:
        print(f"Linear Search: Found at index {lin_index}")
    else:
        print("Linear Search: Product not found.")

    # Step 7: Apply Binary Search
    bin_index, sorted_list = binary_search(products, query)
    if bin_index != -1:
        print(f"Binary Search: Found at index {bin_index} (in sorted list)")
        print(f"Sorted List for Binary Search: {sorted_list}")
    else:
        print("Binary Search: Product not found.")


if __name__ == "__main__":
    main()
