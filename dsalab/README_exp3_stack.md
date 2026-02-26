# 🥞 Stack Data Structure & Postfix Evaluator

> A clean, elegant Python implementation of a Stack with a real-world application: evaluating postfix mathematical expressions.

---

## 🎯 Overview

This project (`exp3_stack.py`) demonstrates the fundamental operations of a **Stack** (LIFO - Last In, First Out) data structure. To showcase its utility, the stack is used to build a **Postfix Expression Evaluator** capable of computing mathematical results from raw string inputs.

## ✨ Features

- **Core Stack Operations**: Fully functional methods for `push()`, `pop()`, and `is_empty()`.
- **Postfix Evaluation**: A robust algorithm to evaluate postfix (Reverse Polish Notation) expressions (for single-digit operands).
- **Interactive CLI**: Run the script directly to enter your own expressions and get instant results!
- **Zero Dependencies**: Pure Python implementation with no external libraries required.

---

## 🚀 Getting Started

### Prerequisites

All you need is Python 3.x installed on your machine.

### Running the Code

1. Navigate to the project directory:
   ```bash
   cd dsalab
   ```
2. Execute the script:
   ```bash
   python exp3_stack.py
   ```
3. Enter your postfix expression when prompted!

---

## 🧠 How It Works

### The Stack Implementation
The `Stack` class wraps a standard Python list, exposing only the safe operations required for a strict LIFO structure:

| Method | Description | Time Complexity |
| :--- | :--- | :---: |
| `push(item)` | Adds a new element to the top of the stack | **O(1)** |
| `pop()` | Removes and returns the top element | **O(1)** |
| `is_empty()` | Checks if the stack contains any elements | **O(1)** |

### Postfix Evaluation Algorithm
When you input an expression (e.g., `53+2*`):
1. **Numbers** are immediately pushed onto the stack.
2. **Operators (`+`, `-`, `*`, `/`)** trigger the script to pop the top two numbers.
3. The operator is applied to these numbers, and the result is pushed *back* onto the stack.
4. Once the expression is fully parsed, the final result remaining on the stack is returned!

---

## 💻 Example Usage

```bash
$ python exp3_stack.py
Enter the expression: 23*5+
Result of the expression 23*5+ is 11
```
*(Explanation: `2 * 3 = 6`, then `6 + 5 = 11`)*

---

## 🛠️ Built With

* **Python 3** - The language used for implementation.
* **Love for Data Structures** ❤️
