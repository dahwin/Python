import numpy as np
import argparse

def matrix_multiply(a, b):
    # Set the seed for reproducibility
    np.random.seed(42)

    # Generate random matrices
    rows_a, cols_a = map(int, a.split(','))
    rows_b, cols_b = map(int, b.split(','))

    matrix_a = np.random.rand(rows_a, cols_a)
    matrix_b = np.random.rand(rows_b, cols_b)

    # Perform matrix multiplication
    result = np.dot(matrix_a, matrix_b)

    return matrix_a, matrix_b, result

def main():
    parser = argparse.ArgumentParser(description='Matrix multiplication with NumPy and random matrices.')
    parser.add_argument('--matrix_a', type=str, required=True, help='Dimensions of matrix A as two integers separated by a comma (e.g., "2,3").')
    parser.add_argument('--matrix_b', type=str, required=True, help='Dimensions of matrix B as two integers separated by a comma (e.g., "3,2").')

    args = parser.parse_args()

    matrix_a, matrix_b, result = matrix_multiply(args.matrix_a, args.matrix_b)

    print("Matrix A:")
    print(matrix_a)

    print("\nMatrix B:")
    print(matrix_b)

    print("\nResult of Matrix Multiplication (A x B):")
    print(result)

if __name__ == "__main__":
    main()
