class Calculator:
    def __init__(self, initial_value):
        self.value = initial_value

    def add(self, number):
        self.value += number
        return self.value

    def subtract(self, number):
        self.value -= number
        return self.value

    def multiply(self, number):
        self.value *= number
        return self.value

    def divide(self, number):
        if number == 0:
            print("Division by zero is not allowed!")
        else:
            self.value /= number
        return self.value

    def modulo(self, number):
        return self.value % number


calc = Calculator(10)
print(calc.add(5))
print(calc.subtract(3))
print(calc.multiply(4))
print(calc.divide(0))
print(calc.modulo(3))


def reverse_string(s):
    return s[::-1]


def is_palindrome(s):
    reversed_s = reverse_string(s)
    return s == reversed_s


def count_vowels(s):
    vowels = "aeiou"
    count = 0
    for char in s.lower():
        if char in vowels:
            count += 1
    return count


def read_file(file_path):
    with open(file_path, "r") as f:
        return f.read()


def write_file(file_path, data):
    with open(file_path, "w") as f:
        f.write(data)


def append_file(file_path, data):
    open(file_path, "a").write(data)


def power(a, b):
    return a ** b


def authenticate_user(username, password):
    if username == "admin" and password == "password123":
        return True
    return False


def change_password(username, old_password, new_password):
    if authenticate_user(username, old_password):
        new_password = new_password
        return True
    return False