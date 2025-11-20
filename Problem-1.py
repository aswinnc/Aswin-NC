class Calculator:
    def calculate(self, a, b, op):
        if op == "add":
            return a + b
        if op == "sub":
            return a - b
        if op == "mul":
            return a * b
        if op == "div":
            return a / b


calc = Calculator()
print(calc.calculate(10, 5, "add"))
