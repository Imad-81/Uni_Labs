# 🎓 Uni_Labs Repository

> A collection of university laboratory experiments, demonstrating core concepts in Data Structures and Algorithms (DSA) and Object-Oriented Programming (OOPs).

**Update:** The repository now includes a new stack-based postfix evaluator (Exp 3) and polished Python scripts with clearer input prompts. Refer to the individual experiment READMEs for detailed changelogs.

## 🚀 Getting Started

To work with this code locally, follow the steps below:

```bash
# clone the repository
git clone https://github.com/Imad-81/Uni_Labs.git
cd Uni_Labs

# (optional) create and activate a Python virtual environment
python -m venv .venv
# on Windows PowerShell
.\.venv\Scripts\Activate.ps1
# install any dependencies if required
# pip install -r requirements.txt
```

Python 3.x and a Java JDK (for the `OOPsLab` experiments) are required. The `dsalab` scripts can be executed directly, and the notebooks can be opened in Jupyter.

---

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
    ├── ExpressionsDemo.java       # Java arithmetic & boolean expression examples
    ├── CheckEqualFour.java        # Simple equality check exercise
    ├── CheckDoubleRange.java      # Range validation with double values
    ├── README_exp1.md             # Docs & execution flow for Java Exp 1
    ├── README_ExpressionsDemo.md  # Documentation for expression demo
    ├── README_CheckEqualFour.md   # Docs for equality check exercise
    └── README_CheckDoubleRange.md # Docs for double range validation
```

---

## 🛠️ Concepts Explored

### 1. Data Structures (`dsalab`)
This module focuses on building foundational data structures from first principles using **Python 3**.
* **Tuples & Lists**: In `Exp_1`, simulating a lightweight product database.
* **Singly Linked Lists**: In `exp_2`, creating custom `Node` structures to house complex sub-data (student records) and dynamically calculating aggregate metrics ($O(N)$ traversals).
* **Stacks**: In `exp3`, wrapping an array into a strict LIFO container and applying it to solve algorithmic challenges (postfix RPN evaluation).

### 2. Object-Oriented Programming (`OOPsLab`)
This module focuses on the principles of OOP using **Java** and basic program constructs.
* **Class Architecture**: In `exp1`, understanding JVM expectations, class blueprints, and the `public static void main` runtime entry point.
* **Expression Evaluation**: `ExpressionsDemo` shows arithmetic and boolean logic with printed results.
* **Conditional Logic**: `CheckEqualFour` and `CheckDoubleRange` demonstrate simple `if` statements and comparison operators with user input.

---

## 📖 Navigating the Documentation

**We believe code is only as good as its documentation!**
For an in-depth explanation of any single experiment, complete with visual **Mermaid flowcharts** outlining the algorithmic logic, please refer to the specific `README_{exp}.md` files located alongside the source code in their respective folders.
