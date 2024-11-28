import string
import random

def sum_with_while(start, end):
    """
    Calculate the sum of all numbers between start and end (inclusive) using a while loop.
    """
    numbers = range(start, end+1)
    n = 0
    sum = 0
    while n<len(numbers):
        sum += numbers[n]
        n+=1
    return sum

def count_vowels_in_string(input_string):
    """
    Count the number of vowels in a given string using a for loop.
    """
    vowels = 'aeiouAEIOU'
    number_of_vowels = 0
    for charracter in vowels:
        number_of_vowels += input_string.count(charracter)
    return number_of_vowels

def filter_numbers(numbers):
    """
    Filter a list of numbers based on specific conditions using a for loop and conditionals.
    """
    positive_numbers = []
    negative_numbers = []
    even_numbers = []
    odd_numbers = []
    dict = {}

    for number in numbers:
        if number > 0:
            positive_numbers.append(number)
        if number < 0:
            negative_numbers.append(number)
        if number%2 == 0:
            even_numbers.append(number)
        if number%2 != 0:
            odd_numbers.append(number)
    
    dict['positive'] = positive_numbers
    dict['negative'] = negative_numbers
    dict['even'] = even_numbers
    dict['odd'] = odd_numbers

    return dict

def fibonacci_sequence(n):
    """
    Generate Fibonacci sequence up to n terms using a while loop.
    """
    fib_sequence = []
    if n > 0:
        while True:
            leading_up_to_n = list(range(n))
            for number in leading_up_to_n:
                    if number <= 1:
                        fib_sequence.append(number)
                    else:
                        index_number = leading_up_to_n.index(number)
                        a = fib_sequence[index_number-2]
                        b = fib_sequence[index_number-1]
                        c = a + b
                        fib_sequence.append(c)
            break
        return fib_sequence
    else:
        return []
    
def pascals_triangle(rows):
    """
    Generate Pascal's Triangle up to a given number of rows.
    """
    triangle = []
    triangle_row = [1]
    triangle.append(triangle_row)
    all_rows = list(range(1,rows))

    for row in all_rows:
        row_index = all_rows.index(row)
        sum = 0
        if row_index == 0:
            for number in triangle[row_index]:
                sum+=number
                row = triangle_row[:]
                row.append(sum)
                triangle.append(row)
                sum = 0
        else:
            ending_one = 1
            n = 0
            row_= [1]
            while True:
                try:
                    sum = triangle[-1][n] + triangle[-1][n+1]
                except IndexError:
                    row_.append(ending_one)
                    triangle.append(row_)
                    break
                else:
                    row_.append(sum)
                    sum = 0
                    n+=1
    return triangle

def tower_of_hanoi(n, source, target, auxiliary):
    """
    Solve the Tower of Hanoi problem recursively.
    """
    pass

def find_dna_sequence(dna, sequence):
    """
    Find the first occurrence of a DNA subsequence within a larger DNA string.
    """
    pass

def is_palindrome(input_string):
    """
    Check if a given string is a palindrome (ignoring spaces, capitalization, and punctuation).
    """
    input_string = input_string.lower()
    punctuation = string.punctuation
    space = ' '
    if space in input_string:
        input_string = input_string.replace(space,'')
    
    for mark in punctuation:
        if mark in input_string:
            input_string = input_string.replace(mark,'')

    reversed_string = input_string[::-1]
    return input_string == reversed_string
    

def generate_permutations(input_string):
    """
    Return all possible permutations of a given string.
    """
    permutations = [input_string]
    input_string = list(input_string)
    n = 0
    while n<5:
        rearranged_input_string = ''
        while len(rearranged_input_string) < len(input_string):
            rearranged_input_string += random.choice(input_string)

        for char in rearranged_input_string:
            if rearranged_input_string.count(char) >1:
                rearranged_input_string = ''
                break

        if rearranged_input_string in permutations:
            rearranged_input_string = ''

        if not rearranged_input_string:
            continue
        elif rearranged_input_string and rearranged_input_string not in permutations:
            permutations.append(rearranged_input_string)

        n+=1
    return sorted(permutations)

#print(generate_permutations('abc'))

def is_valid_sudoku(board):
    """
    Validate a given 9x9 Sudoku board.
    """
    viable = True

    for row in board:
        for number in row:
            if number.isdigit():
                if row.count(number) > 1:
                    viable = False
                    break
        if not viable:
            break

    if viable:
        column = []
        n = 0
        while n<10:
            for row in board:
                column.append(row[n])
            for number in column:
                if number.isdigit():
                    if column.count(number) > 1:
                        viable = False
                        break
            if not viable:
                break
            n+=1
    return viable

board = [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"]
        ]
print(is_valid_sudoku(board))
def solve_n_queens(n):
    """
    Find all possible solutions to the N-Queens problem.
    """
    pass

def longest_common_subsequence(str1, str2):
    """
    Find the length of the longest subsequence common to both strings.
    """
    pass

if __name__ == "__main__":
    pass
