def robust_calculator(func):
    def wrapper(expression):
        try:
            result = func(expression)
            return result
        except Exception as e:
            return f"Помилка: {e}"
    return wrapper

@robust_calculator
def calculate(expression):
    return eval(expression)


result = calculate("5 + 5")
print(result) 

result = calculate("5 / 0")
print(result) 
