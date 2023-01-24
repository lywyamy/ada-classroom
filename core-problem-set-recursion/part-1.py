# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n < 0:
        raise ValueError("The number must be positive.")
    if n == 0:
        return 1
    return n * factorial(n - 1)

# factorial w/ tail recursion
def factorial_tail_recursion(n):
    if n < 0:
        raise ValueError("The number must be positive.")
    return factorial_tail_recursion_helper(1, n)

def factorial_tail_recursion_helper(so_far, n):
    if n == 0:
        return so_far
    return factorial_tail_recursion_helper(so_far * n, n - 1)

# reverse
def reverse(string):
    s_list = list(string)
    return reverse_helper(s_list, 0, len(string) - 1)

def reverse_helper(s_list, left, right):
    if left >= right:
        string = ""
        return string.join(s_list)
    else:
        s_list[left], s_list[right] = s_list[right], s_list[left]
        return reverse_helper(s_list, left + 1, right - 1)

# bunny
def bunny(count):
    if count == 0:
        return 0
    return 2 + bunny(count - 1)
    
# bunny w/ tail recursion
def bunny_tail_recursion(count):
    return bunny_tail_recursion_helper(0, count)

def bunny_tail_recursion_helper(so_far, count):
    if count == 0:
        return so_far
    return bunny_tail_recursion_helper(so_far + 2, count - 1)

# is_nested_parens
def is_nested_parens(parens):
    if len(parens) == 0:
        return True
    elif parens[0] != '(' or parens[-1] != ')':
        return False
    else:
        return is_nested_parens(parens[1:-1])