import numpy as np

# ------------------------ display welcome and guide message ------------------------
def welcomeAndGuide():
    """Display welcome message and program guide."""
    print("\n\n\t\t\t\t<<-------- Welcome to our program -------->>\n")
    print("\n-> This program performs eigenvalue and eigenvector computations using the Iterative Power Method.")
    print("\n-> You will be prompted to enter the matrix elements, tolerance, and the maximum number of iterations.")
    print("\n-> The program will then display the results for the three largest eigenvalues and eigenvectors.")


# ------------------------ fill matrix with input values ----------------------------
def fillMatrix(size):
    """Prompt the user to fill the matrix."""

    matrix = []
    for y in range(size):
        row = []
        for x in range(size):
            value = float(input(f"\tEnter value for [{y}][{x}]: "))
            row.append(value)
        matrix.append(row)
    return matrix


# ---------------------------- display matrix ---------------------------------------
def displayMatrix(matrix):

    """Display the matrix."""

    for row in matrix:
        print("\t", end="")
        print("\t".join(f"{elem}" for elem in row))


# ---------------------------- display result ---------------------------------------
def displayResult(label, eigenvalue, eigenvector):
    eigenvector = "\t".join(map(str, eigenvector))
    print(f"\n{label} Eigenvalue: {eigenvalue}")
    print(f"{label} Eigenvector: {eigenvector}")


# -------------------------- POWER ITERATIONS ALGORITHM -----------------------------
def powerIteration(A, tolerance, max_iterations):
    n = len(A)
    initial_vector = np.random.rand(n)
    prev_lambda = 0

    for iteration in range(1, max_iterations + 1):
        estimated_vector = np.dot(A, initial_vector)
        estimated_lambda = np.dot(initial_vector, estimated_vector)
        initial_vector = estimated_vector / np.linalg.norm(estimated_vector)

        if abs(estimated_lambda - prev_lambda) < tolerance:
            return estimated_lambda, initial_vector

        prev_lambda = estimated_lambda

    return estimated_lambda, initial_vector


def deflation(A, lambda_val, eigenvector, tolerance, max_iterations):
    n = len(A)
    B = A - lambda_val * np.outer(eigenvector, eigenvector)

    deflated_lambda, deflated_vector = powerIteration(B, tolerance, max_iterations)

    return deflated_lambda, deflated_vector


# ------------------------------ MAIN PROMGRAM --------------------------------------
welcomeAndGuide()

size = int(input("\n\tEnter the size of the matrix: "))
while size <= 0:
    print ("\nPlease enter a positive integer")
    size = input("\n\tEnter the number of equations of the system: ")
matrix_A = fillMatrix(size)

if matrix_A is not None:
    displayMatrix(matrix_A)
    tolerance = float(input("Enter the tolerance: "))
    max_iterations = int(input("Enter the number of iterations: "))

    lambda1, vector1 = powerIteration(matrix_A, tolerance, max_iterations)
    matrix_B = matrix_A - lambda1 * np.outer(vector1, vector1)
    lambda2, vector2 = deflation(matrix_A, lambda1, vector1, tolerance, max_iterations)
    lambda3, vector3 = deflation(matrix_B, lambda2, vector2, tolerance, max_iterations)

    print("\nResults:")
    displayResult("1st", lambda1, vector1)
    displayResult("2nd", lambda2, vector2)
    displayResult("3rd", lambda3, vector3)
