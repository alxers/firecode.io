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


def dec_to_bin(number):
    stack = []
    while(number != 0):
        stack.append(number % 2)
        number = number // 2
        
    stack.reverse()
    return ''.join(str(num) for num in stack)


def flip_vertical_axis(matrix):
    for row, index in enumerate(matrix):
        matrix[row][0], matrix[row][-1] = matrix[row][-1], matrix[row][0]
        
    return matrix


def reverse_string(a_string):
    return a_string[::-1]


def duplicate_items(list_numbers):
    dup = []
    for ind, el in enumerate(list_numbers):
        if el in list_numbers[ind+1::]:
            dup.append(el)


    dup.sort()
    return dup
