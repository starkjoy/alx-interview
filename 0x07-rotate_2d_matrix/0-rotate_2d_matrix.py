#!/usr/bin/python3

def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise in-place.
    
    Args:
        matrix (list of list): The input 2D matrix to be rotated.
        
    Returns:
        None: The function operates on the input matrix in-place and does not return anything.
    """
    n = len(matrix)

    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row of the transposed matrix
    for i in range(n):
        matrix[i] = matrix[i][::-1]
        