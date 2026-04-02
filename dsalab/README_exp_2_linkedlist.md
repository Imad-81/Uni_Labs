# Experiment 2: Student GPA Management with Linked Lists

**Aim:** To implement a Singly Linked List in Python to manage student records and calculate their aggregate GPA.

**Algorithm:**
1. Define a `Node` class with `name`, `roll_number`, `marks`, and a `next` pointer.
2. Define a `LinkedList` class with a `head` attribute and `add_student()` method.
3. For `calculate_gpa()`, traverse the linked list to compute the total marks and total count.
4. Return the average marks or an alphabetic grade (A-F) based on the computed average.

**Output:**
List of Students:
Name: Charlie, Roll Number: A003, Marks: 78
Name: Bob, Roll Number: A002, Marks: 92
Name: Alice, Roll Number: A001, Marks: 85
Calculated GPA: B
