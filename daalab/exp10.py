# ---------------------------------------------------------
# EXPERIMENT 10: SAT PROBLEM AND REDUCTIONS
# ---------------------------------------------------------

# Function to evaluate one literal using the given assignment
def evaluate_literal(literal, assignment):

    # Check whether the literal is a negated variable
    if literal.startswith("~"):

        # Get the variable name after '~'
        variable = literal[1:]

        # Return the opposite of the variable's value
        return not assignment[variable]

    # If the literal is not negated, return its assigned value
    return assignment[literal]


# Function to evaluate one clause
def evaluate_clause(clause, assignment):

    # Check every literal present in the clause
    for literal in clause:

        # If any literal is True, the entire OR clause is True
        if evaluate_literal(literal, assignment):

            # Return True because the clause is satisfied
            return True

    # Return False if all literals are False
    return False


# Function to evaluate the complete CNF formula
def evaluate_formula(formula, assignment):

    # Check every clause in the formula
    for clause in formula:

        # If any clause is False, the complete AND formula is False
        if not evaluate_clause(clause, assignment):

            # Return False because the formula is not satisfied
            return False

    # Return True when all clauses are satisfied
    return True


# Function to solve the SAT problem using backtracking
def solve_sat(formula, variables, index, assignment):

    # Check whether all variables have been assigned
    if index == len(variables):

        # Evaluate the complete formula
        if evaluate_formula(formula, assignment):

            # Return the satisfying assignment
            return assignment.copy()

        # Return None if the formula is not satisfied
        return None

    # Select the current variable
    variable = variables[index]

    # Try assigning False to the current variable
    assignment[variable] = False

    # Recursively solve the problem with this assignment
    result = solve_sat(formula, variables, index + 1, assignment)

    # Check whether a solution was found
    if result is not None:

        # Return the satisfying assignment
        return result

    # Try assigning True to the current variable
    assignment[variable] = True

    # Recursively solve the problem with this assignment
    result = solve_sat(formula, variables, index + 1, assignment)

    # Check whether a solution was found
    if result is not None:

        # Return the satisfying assignment
        return result

    # Remove the variable while backtracking
    del assignment[variable]

    # Return None when no assignment works
    return None


# ---------------------------------------------------------
# REDUCTION PART
# ---------------------------------------------------------

# Function to convert a CNF formula into a 3-SAT formula
def reduce_to_3sat(formula):

    # Create an empty list to store the reduced formula
    reduced_formula = []

    # Counter used for creating new auxiliary variables
    new_variable_count = 1

    # Process each clause of the original formula
    for clause in formula:

        # Find the number of literals in the clause
        length = len(clause)

        # If the clause already contains 3 literals
        if length == 3:

            # Add the clause directly to the reduced formula
            reduced_formula.append(clause)

        # If the clause contains only 2 literals
        elif length == 2:

            # Create a new auxiliary variable
            new_variable = "X" + str(new_variable_count)

            # Increase the auxiliary variable counter
            new_variable_count += 1

            # Convert (A OR B) into:
            # (A OR B OR X) AND (A OR B OR ~X)
            reduced_formula.append(
                [clause[0], clause[1], new_variable]
            )

            # Add the second clause with the negated auxiliary variable
            reduced_formula.append(
                [clause[0], clause[1], "~" + new_variable]
            )

        # If the clause contains only 1 literal
        elif length == 1:

            # Create a new auxiliary variable
            new_variable = "X" + str(new_variable_count)

            # Increase the auxiliary variable counter
            new_variable_count += 1

            # Convert (A) into:
            # (A OR X OR ~X)
            reduced_formula.append(
                [clause[0], new_variable, "~" + new_variable]
            )

        # Handle clauses containing more than 3 literals
        else:

            # Store the first two literals
            first = clause[0]
            second = clause[1]

            # Store the remaining literals
            remaining = clause[2:]

            # Create a variable for the reduction
            previous = "X" + str(new_variable_count)

            # Increase the auxiliary variable counter
            new_variable_count += 1

            # Add the first 3-SAT clause
            reduced_formula.append(
                [first, second, previous]
            )

            # Process the remaining literals
            for i in range(len(remaining) - 1):

                # Create another auxiliary variable
                current = "X" + str(new_variable_count)

                # Increase the auxiliary variable counter
                new_variable_count += 1

                # Add a 3-SAT clause connecting the variables
                reduced_formula.append(
                    ["~" + previous, remaining[i], current]
                )

                # Move to the next auxiliary variable
                previous = current

            # Add the final 3-SAT clause
            reduced_formula.append(
                ["~" + previous, remaining[-1], remaining[-1]]
            )

    # Return the converted 3-SAT formula
    return reduced_formula


# ---------------------------------------------------------
# INPUT SECTION
# ---------------------------------------------------------

def main():
    # Display the title of the experiment
    print("======================================")

    # Display the experiment name
    print("       SAT PROBLEM AND REDUCTIONS")

    # Display a separator
    print("======================================")


    # Read the number of clauses from the user
    n = int(input("Enter number of clauses: "))


    # Create an empty list to store the formula
    formula = []


    # Read every clause from the user
    for i in range(n):

        # Read the literals of the clause
        clause = input(
            "Enter clause " + str(i + 1) +
            " (example: A B ~C): "
        ).split()

        # Add the clause to the formula
        formula.append(clause)


    # Read all variables from the user
    variables = input(
        "Enter variables separated by spaces: "
    ).split()


    # ---------------------------------------------------------
    # SAT SOLUTION
    # ---------------------------------------------------------

    # Create an empty dictionary for storing assignments
    assignment = {}


    # Call the SAT solver
    solution = solve_sat(
        formula,
        variables,
        0,
        assignment
    )


    # Display a separator
    print("\n======================================")

    # Check whether the formula is satisfiable
    if solution is not None:

        # Display SAT result
        print("The given formula is SATISFIABLE.")

        # Display the satisfying assignment
        print("\nSatisfying Assignment:")

        # Display each variable and its value
        for variable in variables:

            # Print the variable and its Boolean value
            print(variable, "=", solution[variable])

    else:

        # Display UNSAT result
        print("The given formula is NOT SATISFIABLE.")


    # ---------------------------------------------------------
    # REDUCTION TO 3-SAT
    # ---------------------------------------------------------

    # Display the reduction heading
    print("\n======================================")

    # Display the reduction operation
    print("Reduction of SAT to 3-SAT")

    # Display a separator
    print("======================================")


    # Convert the original formula into 3-SAT form
    three_sat_formula = reduce_to_3sat(formula)


    # Display the resulting 3-SAT formula
    print("\n3-SAT Formula:")


    # Display every clause of the converted formula
    for clause in three_sat_formula:

        # Join the literals using OR
        print("(" + " OR ".join(clause) + ")")


    # ---------------------------------------------------------
    # VERIFY THE REDUCED FORMULA
    # ---------------------------------------------------------

    # Create a set containing all variables
    all_variables = set(variables)


    # Find auxiliary variables created during reduction
    for clause in three_sat_formula:

        # Check every literal in the clause
        for literal in clause:

            # Remove '~' from a negated variable
            variable = literal.replace("~", "")

            # Add the variable to the set
            all_variables.add(variable)


    # Convert the set into a list
    all_variables = list(all_variables)


    # Create an empty assignment for the reduced formula
    reduced_assignment = {}


    # Solve the 3-SAT formula
    reduced_solution = solve_sat(
        three_sat_formula,
        all_variables,
        0,
        reduced_assignment
    )


    # Check whether the reduced formula is satisfiable
    if reduced_solution is not None:

        # Display that the reduced formula is SAT
        print("\nReduced 3-SAT formula is SATISFIABLE.")

    else:

        # Display that the reduced formula is UNSAT
        print("\nReduced 3-SAT formula is NOT SATISFIABLE.")


if __name__ == "__main__":
    main()
