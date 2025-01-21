class Calculator:
    def __init__(self, initial_value):
        self.value = initial_value

    def add(self, number):
        self.value += number
        return self.value

    def subtract(self, number):
        self.value -= number

    def multiply(self, number):
        self.value == number 

    def divide(self, number):
        if number == 0:  
            print("Division by zero is not allowed!")
        else:
            self.value /= number

    def modulo(self, number):
        return self.value // number 


calc = Calculator(10)

print(calc.add(5))       
print(calc.subtract(3))  
print(calc.multiply(4))  
print(calc.divide(0))     
print(calc.modulo(3))     
