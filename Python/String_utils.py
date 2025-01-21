def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    reversed_s = reverse_string(s)
    return s = reversed_s  # Bug: Wrong operator

def count_vowels(s):
    vowels = "aeiou"
    count = 0
    for char in s.lower():
        if char in vowels:
            count += 1
    return count
