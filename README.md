# 🎓 Uni_Labs Repository

> A collection of university laboratory experiments, demonstrating core concepts in Data Structures and Algorithms (DSA) and Object-Oriented Programming (OOPs).

---

## 🗂️ Directory Structure

The repository is modularized into two primary domains, each with its own interactive code and dedicated documentation.

```text
Uni_Labs/
├── dsalab/                        # Data Structures and Algorithms Laboratory
│   ├── Exp_1.ipynb                # Exp 1: Linear search & tuple list manipulation
│   ├── README_Exp_1.md            # Docs & logic flow for Exp 1
│   ├── exp_2_linkedlist.ipynb     # Exp 2: Interactive linked list demonstration
│   ├── exp_2_linkedlist.py        # Exp 2: Executable linked list GPA calculator
│   ├── README_exp_2_linkedlist.md # Docs & architecture flow for Exp 2
│   ├── exp3_stack.py              # Exp 3: Stack-based postfix expression evaluator
│   └── README_exp3_stack.md       # Docs & architecture flow for Exp 3
│
└── OOPsLab/                       # Object-Oriented Programming Laboratory
    ├── exp1.java                  # Java Basics: JVM entry points and main methods
    └── README_exp1.md             # Docs & execution flow for Java Exp 1
```

---

## 🛠️ Concepts Explored

### 1. Data Structures (`dsalab`)
This module focuses on building foundational data structures from first principles using **Python 3**.
* **Tuples & Lists**: In `Exp_1`, simulating a lightweight product database.
* **Singly Linked Lists**: In `exp_2`, creating custom `Node` structures to house complex sub-data (student records) and dynamically calculating aggregate metrics ($O(N)$ traversals).
* **Stacks**: In `exp3`, wrapping an array into a strict LIFO container and applying it to solve algorithmic challenges (postfix RPN evaluation).

### 2. Object-Oriented Programming (`OOPsLab`)
This module focuses on the principles of OOP using **Java**.
* **Class Architecture**: In `exp1`, understanding JVM expectations, class blueprints, and the `public static void main` runtime entry point.

---

## 📖 Navigating the Documentation

**We believe code is only as good as its documentation!**
For an in-depth explanation of any single experiment, complete with visual **Mermaid flowcharts** outlining the algorithmic logic, please refer to the specific `README_{exp}.md` files located alongside the source code in their respective folders.
