def flip_horizontal_axis(matrix):
    matrix[0], matrix[-1] = matrix[-1], matrix[0]
    return matrix
