products = [
    (101, "Mobile", "Electronics", 20000),
    (102, "Laptop", "Electronics", 55000),
    (103, "Shoes", "Fashion", 3000),
    (104, "Watch", "Fashion", 2500),
    (105, "Headphones", "Electronics", 1500)
]
purchases = [
    ("User1", 101, 1),
    ("User2", 103, 2),
    ("User1", 102, 1),
    ("User3", 101, 1),
    ("User2", 105, 3)
]
searches = ["Mobile", "Shoes", "Mobile", "Laptop", "Mobile", "Watch"]

print("--- Q1 ---")
names = [p[1] for p in products]
print(f"Names: {names}")
costliest = max(products, key=lambda x: x[3])
print(f"Costliest: {costliest[1]} ({costliest[3]})")
cat_counts = {c: [p[2] for p in products].count(c) for c in {p[2] for p in products}}
print(f"Category Counts: {cat_counts}")

print("\n--- Q2 ---")
user_items = {}
for u, _, q in purchases: user_items[u] = user_items.get(u, 0) + q
print(f"User Items: {user_items}")
top_user = max(user_items, key=user_items.get)
print(f"Top User: {top_user} ({user_items[top_user]})")
prod_sales = {p[0]: sum(q for u, pid, q in purchases if pid == p[0]) for p in products}
print(f"Product Sales: {prod_sales}")

print("\n--- Q3 ---")
prod_prices = {p[0]: p[3] for p in products}
revenues = {p[1]: prod_sales[p[0]] * prod_prices[p[0]] for p in products}
print(f"Revenues: {revenues}")
print(f"Total Revenue: {sum(revenues.values())}")

print("\n--- Q4 ---")
search_counts = {s: searches.count(s) for s in set(searches)}
print(f"Search Counts: {search_counts}")
print(f"Most Searched: {max(search_counts, key=search_counts.get)}")

print("\n--- Q5 ---")
cat_sales = {c: sum(q for u, pid, q in purchases if next(p[2] for p in products if p[0] == pid) == c) for c in {p[2] for p in products}}
print(f"Category Sales: {cat_sales}")
print(f"Top Category: {max(cat_sales, key=cat_sales.get)}")
