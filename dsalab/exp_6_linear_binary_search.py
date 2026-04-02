class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

def linear_search(dataset, target):

    for i, product in enumerate(dataset):
        if product.name == target:
            return i  # Return the index if found
    return -1  # Return -1 if not found

def binary_search(dataset, target):
    """
    Binary search algorithm to find a product in the sorted dataset.
    """
    low, high = 0, len(dataset) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_product = dataset[mid].name
        if mid_product == target:
            return mid  # Return the index if found
        elif mid_product < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1  # Return -1 if not found

# Sample dataset (assuming it's a list of Product instances)
dataset = [
    Product('Product1', 10.99),
    Product('Product2', 24.99),
    Product('Product3', 34.99),
    Product('Product4', 14.99),
    Product('Product5', 19.99),
]

# Perform linear search
target_product = 'Product3'
linear_result = linear_search(dataset, target_product)
if linear_result != -1:
    print(f"Linear Search: {target_product} found at index {linear_result}")
else:
    print(f"Linear Search: {target_product} not found in the dataset")

# Sort dataset for binary search (assuming the 'name' field is sortable)
dataset.sort(key=lambda x: x.name)

# Perform binary search
binary_result = binary_search(dataset, target_product)
if binary_result != -1:
    print(f"Binary Search: {target_product} found at index {binary_result}")
else:
    print(f"Binary Search: {target_product} not found in the dataset")