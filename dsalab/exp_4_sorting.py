class Product:
    def __init__(self, name, price, popularity):
        self.name = name
        self.price = price
        self.popularity = popularity

    def __repr__(self):
        return f"{self.name} - Price: {self.price}, Popularity: {self.popularity}"

def sort_products(products, criteria):
    """
    Sort the list of products based on the specified criteria.
    """
    if criteria == "price":
        return sorted(products, key=lambda x: x.price)
    elif criteria == "popularity":
        return sorted(products, key=lambda x: x.popularity)
    elif criteria == "alphabetical":
        return sorted(products, key=lambda x: x.name)
    else:
        raise ValueError("Invalid sorting criteria")

# Create a list of products
products = [
    Product("Laptop", 999.99, 8),
    Product("Smartphone", 599.99, 10),
    Product("Headphones", 89.99, 7),
    Product("Tablet", 299.99, 5),
]

# Display original list of products
print("Original List of Products:")
for product in products:
    print(product)

# Sort products by price
sorted_by_price = sort_products(products, "price")
print("\nSorted by Price:")
for product in sorted_by_price:
    print(product)

# Sort products by popularity
sorted_by_popularity = sort_products(products, "popularity")
print("\nSorted by Popularity:")
for product in sorted_by_popularity:
    print(product)

# Sort products alphabetically
sorted_alphabetically = sort_products(products, "alphabetical")
print("\nSorted Alphabetically:")
for product in sorted_alphabetically:
    print(product)
