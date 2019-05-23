# rref_from_null_space is designed to take a given null space, reduce it if needed,
# and from the reduced null space, to determine the RREF of the matrix that produced
# the given null space.

from __future__ import division # not sure if necessary
from sympy import *

def main():

    # Acquire null space, null_given, from user (for testing, working with hardcoded one)

    null_given = 0

    # Put the null space into a matrix A.

    A = Matrix([[1, 2, 3, 4], [5, 6, 7, 8]])

    # Put A into RREF. Assign it to rref_A.

    rref_A = A.rref()

    pprint(A.rref())
    pprint(A.nullspace())

    # Determine the null space of the matrix A and assign it to a null_A.

    null_A = A.nullspace()

    print("null_A is \n")
    pprint(null_A)

    print("len(null_A[0]) is \n")
    pprint(len(null_A[0]))

    # Initialize a matrix B. Make B have the right amount of columns first.

    B = Matrix([0])

    for i in range(0, len(null_A[0]) - 1):

        B = B.col_insert(i, Matrix([0]))

    print("B after resizing is: \n")
    pprint(B)

    # Put null_A into a matrix B. Working on this section right now.

    row = []

    for i in range(0, len(null_A[0])):

        row.append(null_A[otheriteratorneeded[i]])

    print("\n\n Row to be inserted:\n")

    pprint(row)

    print("\n\n Inserting row... \n\n")

    B = B.row_insert(i, Matrix([row]))

    #pprint("\nB is: \n", B)
    #pprint("\n")

    # Put B in RREF, and assign it to rref_B.
    
    rref_B = B.rref()

    # Return rref_B, as this is the matrix of the original matrix.

    pprint(rref_B)

    return rref_B

main()