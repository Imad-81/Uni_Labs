class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"({self.name}, ${self.price})"


class HashTable:
    def __init__(self, size=5, threshold=0.7):
        self.size = size
        self.threshold = threshold
        self.count = 0
        self.table = [[] for _ in range(self.size)]

    def _hash_function(self, key):
        # Custom hash function: sum of ASCII values of the name
        return sum(ord(char) for char in key) % self.size

    def get_load_factor(self):
        return self.count / self.size

    def insert(self, product):
        if self.get_load_factor() >= self.threshold:
            print(f"\n--- Load factor {self.get_load_factor():.2f} exceeded threshold {self.threshold}. Rehashing... ---")
            self._rehash()

        index = self._hash_function(product.name)
        
        # Check if product already exists to update it (optional, but good practice)
        for item in self.table[index]:
            if item.name == product.name:
                item.price = product.price
                print(f"Updated product: {product.name}")
                return

        self.table[index].append(product)
        self.count += 1
        print(f"Inserted: {product}")

    def _rehash(self):
        old_table = self.table
        self.size *= 2
        self.table = [[] for _ in range(self.size)]
        self.count = 0  # Reset count as insert will increment it

        for bucket in old_table:
            for product in bucket:
                self.insert(product)

    def search(self, name):
        index = self._hash_function(name)
        for product in self.table[index]:
            if product.name == name:
                return product
        return None

    def update_price(self, name, new_price):
        product = self.search(name)
        if product:
            product.price = new_price
            print(f"Price updated for {name} to ${new_price}")
            return True
        print(f"Product '{name}' not found.")
        return False

    def display(self):
        print("\n--- Hash Table Contents ---")
        for i in range(self.size):
            print(f"Bucket {i}: {self.table[i]}")
        print(f"Current Load Factor: {self.get_load_factor():.2f}")
        print("---------------------------\n")


def main():
    # Initialize Hash Table
    ht = HashTable(size=4, threshold=0.75)

    print("--- Experiment 7: Hash Table with Chaining and Rehashing ---")
    
    # Insert initial products
    ht.insert(Product("Laptop", 1200))
    ht.insert(Product("Mouse", 25))
    ht.insert(Product("Keyboard", 75))
    ht.display()

    # This insertion should trigger rehashing (3/4 = 0.75 >= 0.75)
    ht.insert(Product("Monitor", 300))
    ht.display()

    ht.insert(Product("USB Cable", 10))
    ht.insert(Product("Webcam", 50))
    ht.display()

    # Search for a product
    search_name = "Mouse"
    found = ht.search(search_name)
    if found:
        print(f"Found product: {found}")
    else:
        print(f"Product {search_name} not found.")

    # Update a product
    ht.update_price("Laptop", 1100)
    ht.display()


if __name__ == "__main__":
    main()
