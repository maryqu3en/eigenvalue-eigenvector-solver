# Eigenvalue and Eigenvector Solver

## Introduction

Welcome to our Eigenvalue and Eigenvector Solver! This Python program utilizes the Iterative Power Method to compute eigenvalues and eigenvectors of a given matrix. The program prompts you to enter the matrix elements, tolerance, and the maximum number of iterations. Subsequently, it displays the results for the three largest eigenvalues and their corresponding eigenvectors.

## How to Use

1. **Welcome and Guide:**
   - Upon execution, the program welcomes you and provides information about its purpose.
   
2. **Input Matrix:**
   - You will be prompted to enter the size of the matrix and its elements.

3. **Display Matrix:**
   - The program displays the entered matrix.

4. **Enter Tolerance and Maximum Iterations:**
   - You will be asked to input the tolerance and the maximum number of iterations.

5. **Eigenvalue and Eigenvector Computation:**
   - The program applies the Power Iteration algorithm to compute eigenvalues and eigenvectors.

6. **Display Results:**
   - The program displays the computed eigenvalues and eigenvectors.

## Functions Overview

1. **`welcomeAndGuide()`:**
   - Displays a welcome message and provides an introduction to the program.

2. **`fillMatrix(size)`:**
   - Prompts the user to fill the matrix with values.

3. **`displayMatrix(matrix)`:**
   - Displays the provided matrix.

4. **`displayResult(label, eigenvalue, eigenvector)`:**
   - Displays the computed eigenvalue and eigenvector.

5. **`powerIteration(A, tolerance, max_iterations)`:**
   - Implements the Power Iteration algorithm to compute eigenvalues and eigenvectors.

6. **`deflation(A, lambda_val, eigenvector, tolerance, max_iterations)`:**
   - Implements the deflation step to compute subsequent eigenvalues and eigenvectors.

## Main Program Execution

1. Calls `welcomeAndGuide()` to display the welcome message.
2. Prompts the user for the size of the matrix and fills the matrix.
3. Displays the entered matrix.
4. Prompts the user to enter the tolerance and maximum iterations.
5. Calls the Power Iteration algorithm to compute the three largest eigenvalues and eigenvectors.
6. Displays the results.

## Usage Tips

- Ensure to input a valid size for the matrix.
- Provide numeric values for matrix elements.
- Choose appropriate values for tolerance and maximum iterations.
- The program computes the three largest eigenvalues and eigenvectors.

## Dependencies
- This program requires `numpy` for numerical computations.

Feel free to explore and analyze matrices using this Eigenvalue and Eigenvector Solver!