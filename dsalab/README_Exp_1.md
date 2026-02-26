# 📦 Experiment 1: Data Filtering & Operations

> A Python experiment handling lists of tuples to extract subsets of data, specifically extracting item categories and identifying the most expensive product.

---

## 🎯 Overview

This file (`Exp_1.ipynb`) simulates a basic product database, purchase history, and search history using Python lists and tuples. It demonstrates introductory concepts in Python programming, such as looping over arrays, accessing tuple elements by index, and basic maximum value calculations.

## ✨ Concepts Explained

### 1. Lists of Tuples as Data Structures
The script defines initial data as lists of tuples, similar to rows in a relational database.
```python
products = [
    (101, "Mobile", "Electronics", 20000), ...
]
```
Each tuple in `products` represents `(ProductID, Name, Category, Price)`.

### 2. Iteration and Data Extraction
The logic cycles through these arrays to extract specific columns of data (like plucking the `Category` from the `products` list).

### 3. Finding the Maximum Value
The script applies a standard $O(N)$ linear search algorithm to find the costliest item. It initializes a `max` variable with the first item's price and updates it by comparing against subsequent elements.

---

## 🔄 Logic Flowchart

```mermaid
flowchart TD
    A([Start]) --> B[Initialize 'products' list of tuples]
    B --> C[Initialize 'prod_names' empty list]
    C --> D{Loop through each product P}
    D -- Yes --> E[Extract Category/Name at P[2]]
    E --> F[Append to 'prod_names']
    F --> D
    D -- No --> G[Set 'cp' = Price of first product]
    G --> H{Loop through each product P again}
    H -- Yes --> I{Is P[3] > cp?}
    I -- Yes --> J[Update cp = P[3]]
    I -- No --> H
    J --> H
    H -- No --> K[Print cp 'Costliest Price']
    K --> L([End])
```

---

## 🚀 Running the Notebook

To view and run this experiment:
1. Open the Jupyter Notebook file `Exp_1.ipynb` in your preferred editor (VS Code, Jupyter Lab, etc.).
2. Execute the cells sequentially.
3. Observe the outputs displaying the array of product categories and the printed costliest item value.
