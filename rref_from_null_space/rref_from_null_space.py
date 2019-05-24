# rref_from_null_space is (poorly) designed to take a given null space, reduce it if needed,
# and from the reduced null space, to determine the RREF of the matrix that produced
# the given null space.

from sympy import *

def main():

    # Acquire amount of columns in the null space, each column's contents, and number of rows desired in target matrix

    null_columns = int(input("Enter the number of columns in the given null space:  "))
    rows_desired = int(input("Enter the desired number of rows in the target matrix:  "))
    null_given = []

    print("\nTo enter square roots, use the format sqrt(n).")
    print("To enter other roots or exponents, use the format x**(a/b).")
    print("To enter rational numbers, use the format n/m.\n")

    for i in range(0, null_columns):

        if i == 0:

            null_column = input("Enter first column of null space, separating entries with only spaces:  ")

        else:

            null_column = input("Enter next column of null space, separating entries with only spaces:  ")

        null_column_str = null_column.split()

        null_column_converted = []

        for i in range(0, len(null_column_str)):

            null_column_converted.append(sympify(null_column_str[i]))

        null_given.append(null_column_converted)

    # Put the null space into a matrix A.

    for i in range(0, null_columns):

        if i == 0:

            A = Matrix(null_given[i]).T

        else:
            
            A = A.row_insert(i, Matrix(null_given[i]).T)

    # Put A into RREF. Assign it to rref_A.

    rref_A = A.rref()

    # Determine the null space of the matrix A and assign it to a null_A.

    null_A = A.nullspace()

    # Initialize a matrix B. Make B have the right amount of columns first.

    B = Matrix([0])

    for i in range(0, len(null_A[0]) - 1):

        B = B.col_insert(i, Matrix([0]))

    # Put null_A into a matrix B.

    row = []

    for i in range(0, len(null_A)):

        row.clear()

        for j in range(0, len(null_A[0])):

            row.append(null_A[i][j])

        B = B.row_insert(i, Matrix([row]))

        if i == 0:

            B.row_del(1)

    # Fill B with rows of zeroes, as needed, to fulfill the desired amount of rows.

    B_dimensions = B.shape

    if B_dimensions[0] < rows_desired:        

        rows_to_add = rows_desired - B_dimensions[0]
        
        #  Make a row of all zeroes to fill out the rest of the matrix.

        adding = zeros(1, B_dimensions[1])

        for i in range(0, rows_to_add):

            B = B.row_insert(B_dimensions[0], adding)

    # Put B in RREF, and assign it to rref_B.

    rref_B = B.rref()

    # Print for display until I'm no longer too lazy to clean up this code.

    pprint(rref_B[0])

    # Return rref_B's matrix component, as this is also the original matrix.

    return rref_B[0]

main()