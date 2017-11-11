def flip_horizontal_axis(matrix):
    matrix[0], matrix[-1] = matrix[-1], matrix[0]
    return matrix

def is_palindrome(input_string):
    return input_string == input_string[::-1]
