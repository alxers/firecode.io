def flip_horizontal_axis(matrix):
    matrix[0], matrix[-1] = matrix[-1], matrix[0]
    return matrix


def fib(n):
    if n == 0:
        return 0
    if (n == 1) or (n == 2):
        return 1
    
    return fib(n - 1) + fib(n - 2)


def is_palindrome(input_string):
    return input_string == input_string[::-1]
