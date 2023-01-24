# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(search_list, target):
    if len(search_list) == 0:
        return False
    return search_list[0] == target or search(search_list[1:], target)

# is_palindrome
def is_palindrome(string):
    if len(string) == 0 or len(string) == 1:
        return True
    return string[0] == string[-1] and is_palindrome(string[1:-1])

# digit_match
def digit_match(num_a, num_b):
    if num_a < 0 or num_b < 0:
         raise ValueError("The integers must be non-negative")
         
    if num_a == 0 and num_b == 0:
        return 1
    elif num_a < 10 or num_b < 10:
        if num_a % 10 == num_b % 10:
            return 1
        else:
            return 0
    elif num_a % 10 == num_b % 10:
        return 1 + digit_match(num_a // 10, num_b // 10)
    else:
        return digit_match(num_a // 10, num_b // 10)